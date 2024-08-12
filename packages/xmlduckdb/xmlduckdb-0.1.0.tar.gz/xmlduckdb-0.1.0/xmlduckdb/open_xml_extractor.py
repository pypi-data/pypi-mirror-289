import zipfile
import time
import logging
from lxml import etree
import duckdb
from io import BytesIO
from typing import Optional, Tuple, Generator, Set, Dict, Union, TextIO, BinaryIO, List, Iterable

class OpenXMLExtractor:
    def __init__(self, table_name: str, conn: duckdb.DuckDBPyConnection, config: Optional[Dict[str, Union[List[str], str]]] = None, logger: Optional[logging.Logger] = None):
        self.table_name: str = table_name
        self.conn: duckdb.DuckDBPyConnection = conn
        self.hashed_xpaths: Set[str] = set()
        self.hashed_file_paths: Set[int] = set()
        self.config: Dict[str, Union[List[str], str]] = config or {"exclude_xpaths": [], "exclude_files": []}
        self.logger: Optional[logging.Logger] = logger

        # Create the DuckDB table if it doesn't exist
        self._create_table()

    def _create_table(self) -> None:
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            AttributeName VARCHAR,
            AttributeValue VARCHAR,
            PathHash UBIGINT,
            NodeNumber UBIGINT,
            FilePathHash UBIGINT
        );
        """
        self.conn.execute(create_table_query)
        if self.logger:
            self.logger.info(f"Table '{self.table_name}' created or already exists.")

    def extract(self, xml_input: Union[str, BytesIO, TextIO, BinaryIO], original_file_path: str, zip_file_name: Optional[str] = None, absolute_parent_path_for_xpath: Optional[str] = None) -> None:
        self.node_counter: int = 0

        if zip_file_name and any(pattern in zip_file_name for pattern in self.config["exclude_files"]):
            return

        base_path: str = absolute_parent_path_for_xpath or ""
        if zip_file_name:
            file_base_path: str = f"file_name={zip_file_name}"
            base_path = f"{absolute_parent_path_for_xpath}/{file_base_path}" if absolute_parent_path_for_xpath else file_base_path

        start_time: Optional[float] = time.time() if self.logger else None

        file_path_hash: int = self.conn.execute("SELECT hash(?)", (original_file_path,)).fetchone()[0]
        self.hashed_file_paths.add(file_path_hash)

        tree = etree.parse(xml_input)
        root = tree.getroot()
        records: List[Tuple[str, str, str, int, int]] = self._parse_element(root, f"{base_path}/{root.tag}".lstrip('/'), file_path_hash)

        self.conn.executemany(f"INSERT INTO {self.table_name} VALUES (?, ?, hash(?), ?, ?)", records)

        if self.logger:
            end_time = time.time()
            self.logger.info(f"Processed file: {zip_file_name or 'pure_xml'} in {end_time - start_time:.4f} seconds. File Path Hash: {file_path_hash}")

    def _parse_element(self, element: etree.Element, path: str, file_path_hash: int) -> List[Tuple[str, str, str, int, int]]:
        current_node_number: int = self.node_counter
        self.node_counter += 1

        if any(excluded_xpath in path for excluded_xpath in self.config["exclude_xpaths"]):
            return []

        records: List[Tuple[str, str, str, int, int]] = [(key, value, path, current_node_number, file_path_hash) for key, value in element.attrib.items()]
        self.hashed_xpaths.add(path)

        for child in element:
            child_path = f"{path}/{child.tag}"
            records.extend(self._parse_element(child, child_path, file_path_hash))

        return records

    def insert_from_zip(self, zip_file_path: str, absolute_parent_path_for_xpath: Optional[str] = None) -> Tuple[Set[str], Set[int]]:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.endswith(('.xml', '.rels')):
                    with zip_ref.open(file_name) as file:
                        self.extract(file, original_file_path=zip_file_path, zip_file_name=file_name, absolute_parent_path_for_xpath=absolute_parent_path_for_xpath)

        return self.hashed_xpaths, self.hashed_file_paths

    @property
    def media(self) -> Generator[Tuple[str, BytesIO], None, None]:
        def media_generator() -> Generator[Tuple[str, BytesIO], None, None]:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                for file_name in zip_ref.namelist():
                    if file_name.startswith('media/') and not file_name.endswith('/'):
                        with zip_ref.open(file_name) as file:
                            media_name_xpath = f"{self.absolute_parent_path_for_xpath}/file_name={file_name}".lstrip('/')
                            yield media_name_xpath, BytesIO(file.read())

        return media_generator() if 'media/' in zipfile.ZipFile(self.zip_path, 'r').namelist() else iter([])

class OpenXMLProcessor:
    def __init__(self, 
                 table_name_prefix: str, 
                 conn: duckdb.DuckDBPyConnection, 
                 file_paths: Iterable[str], 
                 process_limit: Optional[int] = None, 
                 logger: Optional[logging.Logger] = None):
        self.table_name_prefix = table_name_prefix
        self.conn = conn
        self.file_paths = file_paths
        self.process_limit = process_limit
        self.logger = logger
        self.processed_count = 0

        self.xpath_table_name = f"{self.table_name_prefix}_xpaths"
        self.filepath_table_name = f"{self.table_name_prefix}_file_paths"
        
        self._create_tables()

    def _create_tables(self) -> None:
        create_xpath_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.xpath_table_name} (
            PathHash UBIGINT PRIMARY KEY,
            XPath VARCHAR
        );
        """
        create_filepath_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.filepath_table_name} (
            FilePathHash UBIGINT PRIMARY KEY,
            FilePath VARCHAR
        );
        """
        self.conn.execute(create_xpath_table_query)
        self.conn.execute(create_filepath_table_query)
        if self.logger:
            self.logger.info(f"Tables '{self.xpath_table_name}' and '{self.filepath_table_name}' created or already exist.")

    def _is_file_processed(self, file_path_hash: int) -> bool:
        result = self.conn.execute(f"SELECT 1 FROM {self.filepath_table_name} WHERE FilePathHash = ?", (file_path_hash,)).fetchone()
        return result is not None

    def _insert_new_xpaths(self, hashed_xpaths: Set[str]) -> None:
        for path in hashed_xpaths:
            self.conn.execute(f"""
            INSERT INTO {self.xpath_table_name} (PathHash, XPath)
            SELECT hash(?), ? 
            WHERE NOT EXISTS (
                SELECT 1 FROM {self.xpath_table_name} WHERE PathHash = hash(?)
            );
            """, (path, path, path))

    def _insert_new_file_path(self, file_path_hash: int, original_file_path: str) -> None:
        self.conn.execute(f"""
        INSERT INTO {self.filepath_table_name} (FilePathHash, FilePath)
        SELECT ?, ? 
        WHERE NOT EXISTS (
            SELECT 1 FROM {self.filepath_table_name} WHERE FilePathHash = ?
        );
        """, (file_path_hash, original_file_path, file_path_hash))

    def _process_file(self, file_path: str) -> None:
        try:
            extractor = OpenXMLExtractor(table_name=f"{self.table_name_prefix}_data", conn=self.conn, logger=self.logger)
            hashed_xpaths, hashed_file_paths = extractor.insert_from_zip(file_path, absolute_parent_path_for_xpath=file_path)
            
            for file_path_hash in hashed_file_paths:
                if not self._is_file_processed(file_path_hash):
                    self._insert_new_file_path(file_path_hash, file_path)
                    self._insert_new_xpaths(hashed_xpaths)
                    self.processed_count += 1
                else:
                    if self.logger:
                        self.logger.info(f"Skipping file '{file_path}' - already processed.")
        except (zipfile.BadZipFile, etree.XMLSyntaxError, Exception) as e:
            if self.logger:
                self.logger.error(f"Error processing file '{file_path}': {e}")

    def __enter__(self):
        if self.logger:
            self.logger.info("Starting file processing...")

        for i, file_path in enumerate(self.file_paths):
            if self.process_limit and i >= self.process_limit:
                break
            self._process_file(file_path)

        if self.logger:
            self.logger.info(f"Processed {self.processed_count} files.")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.logger:
            self.logger.info("Finished processing files.")
        self.conn.close()  # Optional: Close the DuckDB connection

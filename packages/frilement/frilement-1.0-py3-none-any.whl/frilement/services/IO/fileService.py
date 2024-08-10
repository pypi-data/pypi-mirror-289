from pathlib import Path
from pandas import read_csv, read_parquet
from pandas.io.parsers import TextFileReader
from csv import Sniffer

from ...enums.fileFormat import FileFormat
from ...models.config.frilementConfig import FrilementConfig


class FileService:
    """
    Class to load file datas
    """
    def create_reader(file_path: str, config: FrilementConfig) -> tuple[TextFileReader, FileFormat]:
        file = Path(file_path)

        if not file.is_file():
            raise Exception("Specified path isn't a file...")
        
        file_extension = file.suffix[1:].lower()
        
        if file_extension == FileFormat.CSV:
            with open(file_path, 'r', encoding="utf-8") as f:
                return (read_csv(
                    file_path,
                    delimiter = Sniffer().sniff(
                        f.read(config.file_analyzer_chunk_size)
                    ).delimiter,
                    chunksize = config.data_chunk_size
                ), FileFormat.CSV)
        elif file_extension == FileFormat.PARQUET:
            return (read_parquet(file_path, engine="fastparquet"), FileFormat.PARQUET)
            
        raise Exception(f"Unsupported file format '{file_extension}'...")
#Entity : return type of any function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)   #dataclass is a deocrator that can be assignd to any function to make it an entity. Its  not exactly a class but behaves like a class
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path
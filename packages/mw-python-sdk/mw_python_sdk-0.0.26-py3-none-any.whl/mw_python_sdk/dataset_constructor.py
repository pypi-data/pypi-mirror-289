from dataclasses import dataclass
from typing import Set
from os import path, walk


@dataclass(frozen=True)
class DatasetFileForUpload:
    local_path: str
    remote_path: str


@dataclass
class DatasetConstructor:
    title: str
    short_description: str
    data_files: Set[DatasetFileForUpload]

    def add_file(self, source: str, destination: str):
        """
        将文件添加到待上传的数据集中
        
        Args:
            source (str): 文件源路径
            destination (str): 文件目标路径
        
        Returns:
            None
        """
        self.data_files.add(DatasetFileForUpload(source, destination))
    def add_dir(self, local_dir: str, remote_dir: str):
        """
        递归遍历本地目录，将文件添加到远程数据集中。

        Args:
            local_dir (str): 本地目录路径。
            remote_dir (str): 远程数据集目录路径。

        Returns:
            None

        """
        for root, _dirs, files in walk(local_dir):
            for file in files:
                file_path = path.join(root, file)
                rel_path = path.relpath(path.join(root, file), local_dir)
                path_in_dataset = path.join(remote_dir, rel_path)
                self.add_file(file_path, path_in_dataset)

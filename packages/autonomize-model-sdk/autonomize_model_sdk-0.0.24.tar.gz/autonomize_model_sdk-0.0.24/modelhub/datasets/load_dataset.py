""" This module contains the function to load a dataset from the ModelHub dataset client. """

from typing import Optional, Union, Dict
from datasets import DatasetDict
from ..clients import DatasetClient


def load_dataset(name: str,
                 version: Optional[int] = None,
                 split: Optional[str] = "train",
                 folder_name: Optional[str] = None,
                 load_all_folders: bool = False
                 ) -> Union[DatasetDict, Dict[str, DatasetDict]]:
    """
    Load a dataset from the ModelHub dataset client.
    Args:
        name (str): The name of the dataset.
        version (Optional[int], optional): The version of the dataset. Defaults to None.
        split (Optional[str]): The split of the dataset. Defaults to "train".
        folder_name (Optional[str], optional): The name of the folder to load. Defaults to None.
        load_all_folders (bool, optional): Whether to load all folders as separate datasets. Defaults to False.
        list_files (bool, optional): Whether to list files in the dataset version. Defaults to False.
    Returns:
        Union[DatasetDict, Dict[str, DatasetDict], List[str]]: The loaded dataset(s) or list of files.
    """
    
    client = DatasetClient()
    
    if folder_name:
        return client.load_dataset_by_folder_name(dataset_name=name, folder_name=folder_name, version=version)
    
    if load_all_folders:
        return client.load_datasets_by_folders(dataset_name=name, version=version)
    
    return client.load_dataset(dataset_name=name, version=version, split=split)
""" This module contains the function to load a dataset from the ModelHub dataset client. """

from typing import Optional
from datasets import DatasetDict
from ..clients import DatasetClient


def load_dataset(name: str,
                    version: Optional[int] = None,
                    split: Optional[str] = "train") -> DatasetDict:
    """
    Load a dataset from the ModelHub dataset client.
    Args:
        name (str): The name of the dataset.
        version (Optional[int], optional): The version of the dataset. Defaults to None.
        split (Optional[str]): The split of the dataset. Defaults to None.
    Returns:
        DatasetDict: The loaded dataset.
    """
    
    client = DatasetClient()
    datasets = client.load_dataset(dataset_name=name, version=version, split=split)
    return datasets
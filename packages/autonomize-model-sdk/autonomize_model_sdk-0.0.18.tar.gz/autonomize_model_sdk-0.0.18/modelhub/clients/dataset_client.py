""" Client for interacting with datasets. """
from typing import List, Optional, Dict, Any
from datasets import load_dataset, DatasetDict
from ..core import BaseClient
from ..utils import setup_logger

logger = setup_logger(__name__)

class DatasetClient(BaseClient):
    """Client for interacting with datasets."""

    def __init__(self, base_url=None, client_id=None, client_secret=None, token=None):
        """
        Initialize the DatasetClient.

        Args:
            base_url (str): The base URL of the Dataset server.
            client_id (str, optional): The client ID for authentication. Defaults to None.
            client_secret (str, optional): The client secret for authentication. Defaults to None.
            token (str, optional): The access token for authentication. Defaults to None.
        """
        super().__init__(base_url, client_id, client_secret, token)

    def list_datasets(self) -> List[Dict[str, Any]]:
        """
        List all available datasets.

        Returns:
            List[Dict[str, Any]]: A list of available datasets.
        """
        response = self.get("datasets")
        return response["data"]

    def get_dataset_versions(self, dataset_id: str) -> List[Dict[str, Any]]:
        """
        Get all versions of a specific dataset.

        Args:
            dataset_id (str): The ID of the dataset.

        Returns:
            List[Dict[str, Any]]: A list of dataset versions.
        """
        response = self.get(f"datasets/{dataset_id}")
        return response["data"]["versions"]

    def get_signed_url(self, file_path: str, is_read: bool = True) -> str:
        """
        Get a signed URL for a file.

        Args:
            file_path (str): The path to the file.
            is_read (bool): Whether the URL is for reading. Defaults to True.

        Returns:
            str: The signed URL.
        """
        endpoint = "datasets/signedurl/read" if is_read else "signedurl/upload"
        response = self.post(endpoint, json={"file_path": file_path})
        return response["data"]["url"]

    def load_dataset(self, dataset_name: str, version: Optional[int] = None, split: Optional[str] = "train") -> DatasetDict:
        """
        Load a dataset by name and version.

        Args:
            dataset_name (str): The name of the dataset.
            version (int, optional): The version of the dataset. Defaults to None.
            split (str, optional): The split to load (e.g., "train", "validation"). Defaults to "train".

        Returns:
            DatasetDict: The loaded dataset.
        """
        datasets = self.list_datasets()
        dataset = next((ds for ds in datasets if ds["name"] == dataset_name), None)
        if not dataset:
            raise ValueError(f"Dataset {dataset_name} not found.")

        dataset_id = dataset["id"]
        versions = self.get_dataset_versions(dataset_id)
        if version:
            version_data = next((v for v in versions if v["version_id"] == version), None)
        else:
            version_data = versions[0]  # Default to latest version

        if not version_data:
            raise ValueError(f"Version {version} not found for dataset {dataset_name}.")

        # Collect file URLs
        file_urls = [self.get_signed_url(file["file_path"]) for file in version_data["files"]]

        # Load dataset using the `datasets` library
        return self._load_dataset_by_format(file_urls, split)

    def _load_dataset_by_format(self, file_urls: List[str], split: str) -> DatasetDict:
        """
        Load a dataset from file URLs, determining the format and handling nested paths.

        Args:
            file_urls (List[str]): The list of file URLs.
            split (str): The split to load (e.g., "train", "validation").

        Returns:
            DatasetDict: The loaded dataset.
        """
        data_files = {split: file_urls}
        if any(file.endswith(".csv") for file in file_urls):
            return load_dataset("csv", data_files=data_files)
        elif any(file.endswith(".json") for file in file_urls):
            return load_dataset("json", data_files=data_files)
        elif any(file.endswith(".parquet") for file in file_urls):
            return load_dataset("parquet", data_files=data_files)
        elif any(file.endswith(".txt") for file in file_urls):
            return load_dataset("text", data_files=data_files)
        else:
            raise ValueError("Unsupported file format. Supported formats are CSV, JSON, Parquet, and Text.")

    def load_dataset_files(self, dataset_name: str, version: Optional[int] = None) -> List[str]:
        """
        List files in a dataset version.

        Args:
            dataset_name (str): The name of the dataset.
            version (int, optional): The version of the dataset. Defaults to None.

        Returns:
            List[str]: A list of file URLs.
        """
        datasets = self.list_datasets()
        dataset = next((ds for ds in datasets if ds["name"] == dataset_name), None)
        if not dataset:
            raise ValueError(f"Dataset {dataset_name} not found.")

        dataset_id = dataset["id"]
        versions = self.get_dataset_versions(dataset_id)
        if version:
            version_data = next((v for v in versions if v["version_id"] == version), None)
        else:
            version_data = versions[0]  # Default to latest version

        if not version_data:
            raise ValueError(f"Version {version} not found for dataset {dataset_name}.")

        return [self.get_signed_url(file["file_path"]) for file in version_data["files"]]


# NOTE: Need to give a more descriptive name to the function
def load_au_dataset(name: str,
                    split: Optional[str] = None,
                    version: Optional[int] = None) -> DatasetDict:
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

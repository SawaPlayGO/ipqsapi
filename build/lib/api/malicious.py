from typing import Optional
from ..data.malicious_data import MaliciousData

class Malicious:
    def __init__(self, api) -> None:
        """
        Initializes the Malicious class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api

    def get_info(
        self, 
        file_path_or_url: str,
        type: str = "scan",
        is_url: Optional[bool] = None
    ) -> MaliciousData:
        """
        Scans a file for malware or looks up its previous scan result.
        
        Parameters:
        - file_path_or_url :class:`str` - Path to the file to be scanned or URL of the file.
        - type :class:`str` - Type of the request, "scan" for a full scan or "lookup" for a lookup in recent scans.
        - is_url :class:`bool`, optional - Whether the provided `file_path_or_url` is a URL (True) or SHA-256 hash (False). If None, it is assumed to be a URL.
        
        Returns:
        - MaliciousData: An instance of the MaliciousData class containing the scan result.
        """
        endpoint = f"malware/{type}/{self.api.key}"
        
        if type == "scan":
            # Определяем тип запроса: POST для загрузки файла или GET для URL
            if is_url:
                params = {"file_url": file_path_or_url}
                data = self.api._request("GET", endpoint, params=params)
            else:
                with open(file_path_or_url, "rb") as file:
                    files = {"file": file}
                    data = self.api._request("POST", endpoint, files=files)
        elif type == "lookup":
            # Если тип "lookup", предполагается, что это URL или SHA-256 хеш
            params = {"file_url": file_path_or_url} if is_url else {"file_hash": file_path_or_url}
            data = self.api._request("GET", endpoint, params=params)
        
        return MaliciousData(data)

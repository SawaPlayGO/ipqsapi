from typing import Optional
from ..data.url_data import UrlData  # Импортируем класс UrlData

class Url:
    def __init__(self, api) -> None:
        """
        Initializes the Url class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api

    def get_info(
        self, 
        url: str,
        strictness: Optional[int] = None,
        fast: Optional[bool] = None,
        timeout: Optional[int] = None
    ) -> UrlData:
        """
        Retrieves information about a URL.
        
        Parameters:
        - url :class:`str` - The URL to be checked.
        - strictness :class:`int`, optional - Strictness level for scanning the URL (0 to 2).
        - fast :class:`bool`, optional - Whether to perform a faster check with lighter analysis.
        - timeout :class:`int`, optional - Maximum number of seconds to wait for the response (1-10).
        
        Returns:
        - UrlData: An instance of the UrlData class containing the URL information.
        """
        endpoint = f"url/{self.api.key}/{url}"
        params = {
            "strictness": strictness,
            "fast": fast,
            "timeout": timeout
        }
        
        data = self.api._request("GET", endpoint, params=params)
        return UrlData(data)

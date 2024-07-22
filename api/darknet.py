from typing import Optional
from ..data.darknet_data import DarknetData  # Импортируем класс DarknetData

class Darknet:
    def __init__(self, api) -> None:
        """
        Initializes the Darknet class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api

    def get_info(
        self, 
        type: str,
        data: str,
    ) -> DarknetData:
        """
        Retrieves information about data found in the darknet.
        
        Parameters:
        - type :class:`str` - "username", "email", "password"
        - data :class:`str` - Data to be checked (could be an email, username or password).
        
        Returns:
        - DarknetData: An instance of the DarknetData class containing the darknet information.
        """
        endpoint = f"leaked/{type}/{self.api.key}/{data}"
        data = self.api._request("GET", endpoint)
        return DarknetData(data)

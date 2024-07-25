from typing import Optional, Dict, Any
from ..data.account_data import AccountData  # Импортируем класс AccountData

class Account:
    def __init__(self, api) -> None:
        """
        Initializes the Account class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api

    def get_info(self) -> AccountData:
        """
        Retrieves the account credit and usage information.
        
        Returns:
        - AccountData: An instance of the AccountData class containing the account credit and usage information.
        """
        endpoint = f"account/{self.api.key}"
        data = self.api._request("GET", endpoint)
        return AccountData(data)

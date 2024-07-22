from typing import Optional
from ..data.email_data import EmailData

class Email:
    def __init__(self, api) -> None:
        """
        Initializes the Email class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api
        
    def get_info(
        self, 
        email: str,
        fast: Optional[bool] = None,
        timeout: Optional[int] = None,
        suggest_domain: Optional[bool] = None,
        strictness: Optional[int] = None,
        abuse_strictness: Optional[int] = None
    ) -> EmailData:
        """
        Retrieves information about an email address.
        
        Parameters:
        - email :class:`str` - The email address to be checked.
        - fast :class:`bool`, optional - Whether to skip SMTP validation for faster response.
        - timeout :class:`int`, optional - Maximum number of seconds to wait for the response (1-60).
        - suggest_domain :class:`bool`, optional - Whether to suggest domain corrections.
        - strictness :class:`int`, optional - Strictness level for detecting spam traps (0 to 2).
        - abuse_strictness :class:`int`, optional - Strictness level for recognizing abusive patterns (0 to 2).
        
        Returns:
        - EmailData: An instance of the EmailData class containing the email information.
        """
        endpoint = f"email/{self.api.key}/{email}"
        params = {
            "fast": fast,
            "timeout": timeout,
            "suggest_domain": suggest_domain,
            "strictness": strictness,
            "abuse_strictness": abuse_strictness
        }
        
        data = self.api._request("GET", endpoint, params=params)
        return EmailData(data)

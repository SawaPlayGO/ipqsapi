from ..data.phone_data import PhoneData


class Phone:
    def __init__(self, api) -> None:
        """
        Initializes the Phone class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api
        
    def get_info(
        
        self, 
        phone_number: str,
        strictness: int = None,
        country: str = None, 
        enhanced_line_check: bool = None, 
        enhanced_name_check: bool = None
        
    ) -> PhoneData:
        """
        Retrieves information about a phone number.

        Parameters:
        - phone_number :class:`str` - The phone number to be checked.
        - strictness :class:`int`, optional - Level of strictness for the check (0 to 2). 
          Higher values mean more stringent checks and possibly more false positives.
        - country :class:`str`, optional - Default country or countries this phone number is suspected to be associated with.
        - enhanced_line_check :class:`bool`, optional - Enables more advanced line checks to determine if the phone number is active or disconnected.
        - enhanced_name_check :class:`bool`, optional - Enables enhanced name appending for the phone number.

        Returns:
        - PhoneData: An instance of the PhoneData class containing the phone number information.
        """
        endpoint = f"phone/{self.api.key}/{phone_number}"
        params = {
            "strictness": strictness,
            "country": country,
            "enhanced_line_check": enhanced_line_check,
            "enhanced_name_check": enhanced_name_check,
        }
        
        data = self.api._request("GET", endpoint, params=params)
        return PhoneData(data)
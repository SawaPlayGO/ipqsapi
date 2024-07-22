from ..data.proxyvpn_data import ProxyVPNData

class ProxyVPN:
    def __init__(self, api) -> None:
        self.api = api
        
    def get_info(
        
        self, 
        ip_address: str,
        allow_public_access_points: bool = None,
        mobile: bool = None, 
        fast: bool = None, 
        strictness: int = None,
        lighter_penalties: bool = None,
        user_agent: str = None,
        user_language: str = None
        
        ) -> ProxyVPNData:
        """
        Docs
        -
        https://www.ipqualityscore.com/documentation/proxy-detection-api/overview
        
        Parameters
        -
        ip_address :class:`str` - Checked IP
        allow_public_access_points :class:`bool` - Allows corporate and public connections
        mobile :class:`bool` - Forces the IP to be scored as a mobile device
        fast :class:`bool` - Speeds up the API response time
        strictness :class:`int` - Fraud scoring strictness level
        lighter_penalties :class:`bool` - Lowers scoring and proxy detection
        user_language :class:`str` - Further enhances scoring based on the user's device.
        user_agent :class:`str` - It is strongly recommended to pass the "user_agent" string associated with the IP address. This data point allows our scoring algorithms to better detect bots, abusive users, and high risk IPs by analyzing the browser information.
        
        Return
        -
        :class:`ProxyVPNData`
        """
        endpoint = f"ip/{self.api.key}/{ip_address}"
        params = {
            "strictness": strictness,
            "allow_public_access_points": allow_public_access_points,
            "fast": fast,
            "lighter_penalties": lighter_penalties,
            "mobile": mobile,
            "user_agent": user_agent,
            "user_language": user_language,
            
        }
        
        data = self.api._request("GET", endpoint, params=params)
        
        return ProxyVPNData(data)

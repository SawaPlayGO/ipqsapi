import json
from typing import Dict, Any

class AccountData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - success: :class:`bool` - Indicates if the request was successful
    - message: :class:`str` - Status message from the API
    - credits: :class:`int` - Total number of credits available
    - usage: :class:`int` - Number of credits used in the current billing period
    - proxy_usage: :class:`int` - Number of proxy credits used
    - email_usage: :class:`int` - Number of email credits used
    - mobile_sdk_usage: :class:`int` - Number of mobile SDK credits used
    - phone_usage: :class:`int` - Number of phone credits used
    - url_usage: :class:`int` - Number of URL credits used
    - fingerprint_usage: :class:`int` - Number of fingerprint credits used
    - request_id: :class:`str` - Unique request ID
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.success: bool = data.get("success", False)
        self.message: str = data.get("message", "")
        self.credits: int = data.get("credits", 0)
        self.usage: int = data.get("usage", 0)
        self.proxy_usage: int = data.get("proxy_usage", 0)
        self.email_usage: int = data.get("email_usage", 0)
        self.mobile_sdk_usage: int = data.get("mobile_sdk_usage", 0)
        self.phone_usage: int = data.get("phone_usage", 0)
        self.url_usage: int = data.get("url_usage", 0)
        self.fingerprint_usage: int = data.get("fingerprint_usage", 0)
        self.request_id: str = data.get("request_id", "")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "credits": self.credits,
            "usage": self.usage,
            "proxy_usage": self.proxy_usage,
            "email_usage": self.email_usage,
            "mobile_sdk_usage": self.mobile_sdk_usage,
            "phone_usage": self.phone_usage,
            "url_usage": self.url_usage,
            "fingerprint_usage": self.fingerprint_usage,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

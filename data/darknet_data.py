import json
from typing import Dict, Any, List

class DarknetData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - success: :class:`bool` - Indicates if the request was successful
    - message: :class:`str` - Potential error message
    - source: :class:`List[str]` - List of sources where data was exposed
    - exposed: :class:`bool` - Whether the data was found in a data breach
    - first_seen: :class:`Dict[str, Any]` - Date when the data was first seen
    - plain_text_password: :class:`bool` - Indicates if the password was found in plain text
    - request_id: :class:`str` - Unique request ID
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.success: bool = data.get("success", False)
        self.message: str = data.get("message", "")
        self.source: List[str] = data.get("source", [])
        self.exposed: bool = data.get("exposed", False)
        self.first_seen: Dict[str, Any] = data.get("first_seen", {})
        self.plain_text_password: bool = data.get("plain_text_password", False)
        self.request_id: str = data.get("request_id", "")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "source": self.source,
            "exposed": self.exposed,
            "first_seen": self.first_seen,
            "plain_text_password": self.plain_text_password,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

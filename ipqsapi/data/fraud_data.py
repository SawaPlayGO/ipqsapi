import json
from typing import Dict, Any

class FraudData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - success: :class:`bool` - Indicates if the request was successful
    - message: :class:`str` - Potential error message
    - request_id: :class:`str` - Unique request ID
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.success: bool = data.get("success", False)
        self.message: str = data.get("message", "")
        self.request_id: str = data.get("request_id", "")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

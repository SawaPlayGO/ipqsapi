import json
from typing import Dict, Any

class MaliciousData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - success: :class:`bool` - Indicates if the request was successful
    - message: :class:`str` - Response message from the API
    - file_hash: :class:`str` - Hash of the scanned file
    - type: :class:`str` - Type of the scan ("scan" or "lookup")
    - status: :class:`str` - Status of the scan
    - result: :class:`list` - List of scan results from different threat detectors
    - update_url: :class:`str` - URL to check the update status
    - request_id: :class:`str` - Unique request ID
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.success: bool = data.get("success", False)
        self.message: str = data.get("message", "")
        self.file_hash: str = data.get("file_hash", "")
        self.type: str = data.get("type", "")
        self.status: str = data.get("status", "")
        self.result: list = data.get("result", [])
        self.update_url: str = data.get("update_url", "")
        self.request_id: str = data.get("request_id", "")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "file_hash": self.file_hash,
            "type": self.type,
            "status": self.status,
            "result": self.result,
            "update_url": self.update_url,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

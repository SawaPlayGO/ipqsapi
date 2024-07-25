import json
from typing import Dict, Any

class ProxyVPNData:
    """
    Parameters
    -
    data :class:`Dict[str, Any]` - list json request
    
    Return
    - 
    message: :class:`str` - Сообщение об успешном/безуспешном запрос
    success: :class:`bool` - Успешный/Безуспешный запрос
    proxy: :class:`bool` - Является ли IP адресс прокси
    """
    def __init__(self, data: Dict[str, Any]):
        self.message: str = data.get("message")
        self.success: bool = data.get("success")
        self.proxy: bool = data.get("proxy")
        self.isp: str = data.get("ISP")
        self.organization: str = data.get("organization")
        self.asn: int = data.get("ASN")
        self.host: str = data.get("host")
        self.country_code: str = data.get("country_code")
        self.city: str = data.get("city")
        self.region: str = data.get("region")
        self.is_crawler: bool = data.get("is_crawler")
        self.connection_type: str = data.get("connection_type")
        self.latitude: float = data.get("latitude")
        self.longitude: float = data.get("longitude")
        self.zip_code: str = data.get("zip_code")
        self.timezone: str = data.get("timezone")
        self.vpn: bool = data.get("vpn")
        self.tor: bool = data.get("tor")
        self.active_vpn: bool = data.get("active_vpn")
        self.active_tor: bool = data.get("active_tor")
        self.recent_abuse: bool = data.get("recent_abuse")
        self.frequent_abuser: bool = data.get("frequent_abuser")
        self.high_risk_attacks: bool = data.get("high_risk_attacks")
        self.abuse_velocity: str = data.get("abuse_velocity")
        self.bot_status: bool = data.get("bot_status")
        self.shared_connection: bool = data.get("shared_connection")
        self.dynamic_connection: bool = data.get("dynamic_connection")
        self.security_scanner: bool = data.get("security_scanner")
        self.trusted_network: bool = data.get("trusted_network")
        self.mobile: bool = data.get("mobile")
        self.fraud_score: int = data.get("fraud_score")
        self.operating_system: str = data.get("operating_system")
        self.browser: str = data.get("browser")
        self.device_model: str = data.get("device_model")
        self.device_brand: str = data.get("device_brand")
        self.transaction_details: dict = data.get("transaction_details")
        self.request_id: str = data.get("request_id")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "success": self.success,
            "proxy": self.proxy,
            "isp": self.isp,
            "organization": self.organization,
            "asn": self.asn,
            "host": self.host,
            "country_code": self.country_code,
            "city": self.city,
            "region": self.region,
            "is_crawler": self.is_crawler,
            "connection_type": self.connection_type,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "zip_code": self.zip_code,
            "timezone": self.timezone,
            "vpn": self.vpn,
            "tor": self.tor,
            "active_vpn": self.active_vpn,
            "active_tor": self.active_tor,
            "recent_abuse": self.recent_abuse,
            "frequent_abuser": self.frequent_abuser,
            "high_risk_attacks": self.high_risk_attacks,
            "abuse_velocity": self.abuse_velocity,
            "bot_status": self.bot_status,
            "shared_connection": self.shared_connection,
            "dynamic_connection": self.dynamic_connection,
            "security_scanner": self.security_scanner,
            "trusted_network": self.trusted_network,
            "mobile": self.mobile,
            "fraud_score": self.fraud_score,
            "operating_system": self.operating_system,
            "browser": self.browser,
            "device_model": self.device_model,
            "device_brand": self.device_brand,
            "transaction_details": self.transaction_details,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

import json
from typing import Dict, Any

class PhoneData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - message: :class:`str` - Message indicating the success or failure of the request
    - success: :class:`bool` - Indicates whether the request was successful
    - formatted: :class:`str` - Formatted phone number
    - local_format: :class:`str` - Local format of the phone number
    - valid: :class:`bool` - Indicates whether the phone number is valid
    - fraud_score: :class:`int` - Fraud probability score
    - recent_abuse: :class:`bool` - Indicates recent abuse of the phone number
    - VOIP: :class:`bool` - Indicates if the phone number is a VOIP number
    - prepaid: :class:`bool` - Indicates if the phone number is a prepaid number
    - risky: :class:`bool` - Indicates if the phone number is considered risky
    - active: :class:`bool` - Indicates if the phone number is active
    - carrier: :class:`str` - Phone carrier
    - line_type: :class:`str` - Type of phone line (e.g., wireless, landline)
    - country: :class:`str` - Country associated with the phone number
    - city: :class:`str` - City associated with the phone number
    - zip_code: :class:`str` - Zip code associated with the phone number
    - region: :class:`str` - Region associated with the phone number
    - dialing_code: :class:`int` - Country dialing code
    - active_status: :class:`str` - Active status of the phone number
    - sms_domain: :class:`str` - SMS domain associated with the phone number
    - associated_email_addresses: :class:dict - Associated email addresses with the phone number
    - user_activity: :class:`str` - User activity associated with the phone number
    - mnc: :class:`str` - Mobile network code
    - mcc: :class:`str` - Mobile country code
    - leaked: :class:`bool` - Indicates if the phone number is leaked
    - spammer: :class:`bool` - Indicates if the phone number is used by a spammer
    - request_id: :class:`str` - Unique request ID
    - name: :class:`str` - Name associated with the phone number
    - timezone: :class:`str` - Timezone associated with the phone number
    - do_not_call: :class:`bool` - Indicates if the phone number is on a do-not-call list
    - accurate_country_code: :class:`bool` - Indicates if the country code is accurate
    - sms_email: :class:`str` - SMS email associated with the phone number
    """
    def __init__(self, data: Dict[str, Any]):
        self.message: str = data.get("message")
        self.success: bool = data.get("success")
        self.formatted: str = data.get("formatted")
        self.local_format: str = data.get("local_format")
        self.valid: bool = data.get("valid")
        self.fraud_score: int = data.get("fraud_score")
        self.recent_abuse: bool = data.get("recent_abuse")
        self.VOIP: bool = data.get("VOIP")
        self.prepaid: bool = data.get("prepaid")
        self.risky: bool = data.get("risky")
        self.active: bool = data.get("active")
        self.carrier: str = data.get("carrier")
        self.line_type: str = data.get("line_type")
        self.country: str = data.get("country")
        self.city: str = data.get("city")
        self.zip_code: str = data.get("zip_code")
        self.region: str = data.get("region")
        self.dialing_code: int = data.get("dialing_code")
        self.active_status: str = data.get("active_status")
        self.sms_domain: str = data.get("sms_domain")
        self.associated_email_addresses: dict = data.get("associated_email_addresses")
        self.user_activity: str = data.get("user_activity")
        self.mnc: str = data.get("mnc")
        self.mcc: str = data.get("mcc")
        self.leaked: bool = data.get("leaked")
        self.spammer: bool = data.get("spammer")
        self.request_id: str = data.get("request_id")
        self.name: str = data.get("name")
        self.timezone: str = data.get("timezone")
        self.do_not_call: bool = data.get("do_not_call")
        self.accurate_country_code: bool = data.get("accurate_country_code")
        self.sms_email: str = data.get("sms_email")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "success": self.success,
            "formatted": self.formatted,
            "local_format": self.local_format,
            "valid": self.valid,
            "fraud_score": self.fraud_score,
            "recent_abuse": self.recent_abuse,
            "VOIP": self.VOIP,
            "prepaid": self.prepaid,
            "risky": self.risky,
            "active": self.active,
            "carrier": self.carrier,
            "line_type": self.line_type,
            "country": self.country,
            "city": self.city,
            "zip_code": self.zip_code,
            "region": self.region,
            "dialing_code": self.dialing_code,
            "active_status": self.active_status,
            "sms_domain": self.sms_domain,
            "associated_email_addresses": self.associated_email_addresses,
            "user_activity": self.user_activity,
            "mnc": self.mnc,
            "mcc": self.mcc,
            "leaked": self.leaked,
            "spammer": self.spammer,
            "request_id": self.request_id,
            "name": self.name,
            "timezone": self.timezone,
            "do_not_call": self.do_not_call,
            "accurate_country_code": self.accurate_country_code,
            "sms_email": self.sms_email
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
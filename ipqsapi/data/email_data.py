import json
from typing import Dict, Any

class EmailData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - valid: :class:`bool` - Indicates if the email address is valid
    - timed_out: :class:`bool` - Indicates if the request timed out
    - disposable: :class:`bool` - Indicates if the email address is from a disposable email provider
    - first_name: :class:`str` - First name associated with the email address
    - deliverability: :class:`str` - Deliverability status of the email address
    - smtp_score: :class:`int` - SMTP validation score
    - overall_score: :class:`int` - Overall validation score
    - catch_all: :class:`bool` - Indicates if the domain is a catch-all domain
    - generic: :class:`bool` - Indicates if the email address is from a generic provider
    - common: :class:`bool` - Indicates if the domain is common
    - dns_valid: :class:`bool` - Indicates if DNS records are valid
    - honeypot: :class:`bool` - Indicates if the email address is associated with a honeypot
    - frequent_complainer: :class:`bool` - Indicates if the email address is frequently reported
    - suspect: :class:`bool` - Indicates if the email address is suspicious
    - recent_abuse: :class:`bool` - Indicates if the email address has recent abuse reports
    - fraud_score: :class:`int` - Fraud score associated with the email address
    - leaked: :class:`bool` - Indicates if the email address has been leaked in data breaches
    - suggested_domain: :class:`str` - Suggested domain if there was a typo in the domain part
    - domain_velocity: :class:`str` - Velocity of the domain
    - domain_trust: :class:`str` - Trust level of the domain
    - user_activity: :class:`str` - User activity level
    - associated_names: :class:`dict` - Associated names with the email address
    - associated_phone_numbers: :class:`dict` - Associated phone numbers with the email address
    - first_seen: :class:`dict` - Date when the email address was first seen
    - domain_age: :class:`dict` - Age of the domain
    - success: :class:`bool` - Indicates if the request was successful
    - spam_trap_score: :class:`str` - Spam trap score
    - risky_tld: :class:`bool` - Indicates if the top-level domain is risky
    - spf_record: :class:`bool` - Indicates if there is a valid SPF record
    - dmarc_record: :class:`bool` - Indicates if there is a valid DMARC record
    - sanitized_email: :class:`str` - Sanitized version of the email address
    - mx_records: :class:`list` - List of MX records for the domain
    - request_id: :class:`str` - Unique request ID
    - a_records: :class:`list` - List of A records for the domain
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.valid: bool = data.get("valid", False)
        self.timed_out: bool = data.get("timed_out", False)
        self.disposable: bool = data.get("disposable", False)
        self.first_name: str = data.get("first_name", "Unknown")
        self.deliverability: str = data.get("deliverability", "unknown")
        self.smtp_score: int = data.get("smtp_score", 0)
        self.overall_score: int = data.get("overall_score", 0)
        self.catch_all: bool = data.get("catch_all", False)
        self.generic: bool = data.get("generic", False)
        self.common: bool = data.get("common", False)
        self.dns_valid: bool = data.get("dns_valid", False)
        self.honeypot: bool = data.get("honeypot", False)
        self.frequent_complainer: bool = data.get("frequent_complainer", False)
        self.suspect: bool = data.get("suspect", False)
        self.recent_abuse: bool = data.get("recent_abuse", False)
        self.fraud_score: int = data.get("fraud_score", 0)
        self.leaked: bool = data.get("leaked", False)
        self.suggested_domain: str = data.get("suggested_domain", "N/A")
        self.domain_velocity: str = data.get("domain_velocity", "unknown")
        self.domain_trust: str = data.get("domain_trust", "unknown")
        self.user_activity: str = data.get("user_activity", "unknown")
        self.associated_names: Dict[str, Any] = data.get("associated_names", {})
        self.associated_phone_numbers: Dict[str, Any] = data.get("associated_phone_numbers", {})
        self.first_seen: Dict[str, Any] = data.get("first_seen", {})
        self.domain_age: Dict[str, Any] = data.get("domain_age", {})
        self.success: bool = data.get("success", False)
        self.spam_trap_score: str = data.get("spam_trap_score", "none")
        self.risky_tld: bool = data.get("risky_tld", False)
        self.spf_record: bool = data.get("spf_record", False)
        self.dmarc_record: bool = data.get("dmarc_record", False)
        self.sanitized_email: str = data.get("sanitized_email", "")
        self.mx_records: list = data.get("mx_records", [])
        self.request_id: str = data.get("request_id", "")
        self.a_records: list = data.get("a_records", [])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "valid": self.valid,
            "timed_out": self.timed_out,
            "disposable": self.disposable,
            "first_name": self.first_name,
            "deliverability": self.deliverability,
            "smtp_score": self.smtp_score,
            "overall_score": self.overall_score,
            "catch_all": self.catch_all,
            "generic": self.generic,
            "common": self.common,
            "dns_valid": self.dns_valid,
            "honeypot": self.honeypot,
            "frequent_complainer": self.frequent_complainer,
            "suspect": self.suspect,
            "recent_abuse": self.recent_abuse,
            "fraud_score": self.fraud_score,
            "leaked": self.leaked,
            "suggested_domain": self.suggested_domain,
            "domain_velocity": self.domain_velocity,
            "domain_trust": self.domain_trust,
            "user_activity": self.user_activity,
            "associated_names": self.associated_names,
            "associated_phone_numbers": self.associated_phone_numbers,
            "first_seen": self.first_seen,
            "domain_age": self.domain_age,
            "success": self.success,
            "spam_trap_score": self.spam_trap_score,
            "risky_tld": self.risky_tld,
            "spf_record": self.spf_record,
            "dmarc_record": self.dmarc_record,
            "sanitized_email": self.sanitized_email,
            "mx_records": self.mx_records,
            "request_id": self.request_id,
            "a_records": self.a_records
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

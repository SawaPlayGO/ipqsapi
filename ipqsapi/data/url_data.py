import json
from typing import Dict, Any

class UrlData:
    """
    Parameters:
    - data :class:`Dict[str, Any]` - JSON response data

    Attributes:
    - message: :class:`str` - Response message from the API
    - success: :class:`bool` - Indicates if the request was successful
    - unsafe: :class:`bool` - Indicates if the URL is considered unsafe
    - domain: :class:`str` - Domain of the URL
    - root_domain: :class:`str` - Root domain of the URL
    - ip_address: :class:`str` - IP address of the URL
    - country_code: :class:`str` - Country code of the server
    - language_code: :class:`str` - Language code of the server
    - server: :class:`str` - Server type
    - content_type: :class:`str` - Content type of the URL
    - status_code: :class:`int` - HTTP status code of the URL
    - page_size: :class:`int` - Size of the page in bytes
    - domain_rank: :class:`int` - Rank of the domain
    - dns_valid: :class:`bool` - Indicates if DNS records are valid
    - parking: :class:`bool` - Indicates if the domain is parked
    - spamming: :class:`bool` - Indicates if the domain is involved in spamming
    - malware: :class:`bool` - Indicates if the domain is associated with malware
    - phishing: :class:`bool` - Indicates if the domain is associated with phishing
    - suspicious: :class:`bool` - Indicates if the domain is suspicious
    - domain_trust: :class:`str` - Trust level of the domain
    - short_link_redirect: :class:`bool` - Indicates if the URL is a short link redirect
    - hosted_content: :class:`bool` - Indicates if the content is hosted
    - page_title: :class:`str` - Title of the page
    - risky_tld: :class:`bool` - Indicates if the top-level domain is risky
    - spf_record: :class:`bool` - Indicates if there is a valid SPF record
    - dmarc_record: :class:`bool` - Indicates if there is a valid DMARC record
    - technologies: :class:`list` - List of technologies used by the website
    - a_records: :class:`list` - List of A records for the domain
    - mx_records: :class:`list` - List of MX records for the domain
    - ns_records: :class:`list` - List of NS records for the domain
    - adult: :class:`bool` - Indicates if the content is adult
    - risk_score: :class:`int` - Risk score of the URL
    - domain_age: :class:`dict` - Age of the domain
    - category: :class:`str` - Category of the website
    - redirected: :class:`bool` - Indicates if the URL was redirected
    - scanned_url: :class:`str` - Scanned URL
    - final_url: :class:`str` - Final URL after redirects
    - request_id: :class:`str` - Unique request ID
    """
    
    def __init__(self, data: Dict[str, Any]):
        self.message: str = data.get("message", "")
        self.success: bool = data.get("success", False)
        self.unsafe: bool = data.get("unsafe", False)
        self.domain: str = data.get("domain", "N/A")
        self.root_domain: str = data.get("root_domain", "N/A")
        self.ip_address: str = data.get("ip_address", "N/A")
        self.country_code: str = data.get("country_code", "N/A")
        self.language_code: str = data.get("language_code", "N/A")
        self.server: str = data.get("server", "N/A")
        self.content_type: str = data.get("content_type", "N/A")
        self.status_code: int = data.get("status_code", 0)
        self.page_size: int = data.get("page_size", 0)
        self.domain_rank: int = data.get("domain_rank", 0)
        self.dns_valid: bool = data.get("dns_valid", False)
        self.parking: bool = data.get("parking", False)
        self.spamming: bool = data.get("spamming", False)
        self.malware: bool = data.get("malware", False)
        self.phishing: bool = data.get("phishing", False)
        self.suspicious: bool = data.get("suspicious", False)
        self.domain_trust: str = data.get("domain_trust", "unknown")
        self.short_link_redirect: bool = data.get("short_link_redirect", False)
        self.hosted_content: bool = data.get("hosted_content", False)
        self.page_title: str = data.get("page_title", "N/A")
        self.risky_tld: bool = data.get("risky_tld", False)
        self.spf_record: bool = data.get("spf_record", False)
        self.dmarc_record: bool = data.get("dmarc_record", False)
        self.technologies: list = data.get("technologies", [])
        self.a_records: list = data.get("a_records", [])
        self.mx_records: list = data.get("mx_records", [])
        self.ns_records: list = data.get("ns_records", [])
        self.adult: bool = data.get("adult", False)
        self.risk_score: int = data.get("risk_score", 0)
        self.domain_age: Dict[str, Any] = data.get("domain_age", {})
        self.category: str = data.get("category", "N/A")
        self.redirected: bool = data.get("redirected", False)
        self.scanned_url: str = data.get("scanned_url", "N/A")
        self.final_url: str = data.get("final_url", "N/A")
        self.request_id: str = data.get("request_id", "N/A")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "success": self.success,
            "unsafe": self.unsafe,
            "domain": self.domain,
            "root_domain": self.root_domain,
            "ip_address": self.ip_address,
            "country_code": self.country_code,
            "language_code": self.language_code,
            "server": self.server,
            "content_type": self.content_type,
            "status_code": self.status_code,
            "page_size": self.page_size,
            "domain_rank": self.domain_rank,
            "dns_valid": self.dns_valid,
            "parking": self.parking,
            "spamming": self.spamming,
            "malware": self.malware,
            "phishing": self.phishing,
            "suspicious": self.suspicious,
            "domain_trust": self.domain_trust,
            "short_link_redirect": self.short_link_redirect,
            "hosted_content": self.hosted_content,
            "page_title": self.page_title,
            "risky_tld": self.risky_tld,
            "spf_record": self.spf_record,
            "dmarc_record": self.dmarc_record,
            "technologies": self.technologies,
            "a_records": self.a_records,
            "mx_records": self.mx_records,
            "ns_records": self.ns_records,
            "adult": self.adult,
            "risk_score": self.risk_score,
            "domain_age": self.domain_age,
            "category": self.category,
            "redirected": self.redirected,
            "scanned_url": self.scanned_url,
            "final_url": self.final_url,
            "request_id": self.request_id
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

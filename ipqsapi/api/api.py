# Default
from typing import Optional, Dict, Any
import requests

# Const
API_URL = "https://www.ipqualityscore.com/api/json/"

class API:
    """
    API url - https://www.ipqualityscore.com/
    -----
    key: :class:`str` - API key
    """
    def __init__(self, key: str) -> None:
        self.key = key
        
        # Catalogs
        self.proxyvpn_check = self._create_proxy_vpn()
        self.phone_check = self._create_phone()
        self.email_check = self._create_email()
        self.url_check = self._create_url()
        self.malicious_check = self._create_malicious()
        self.darknet_check = self._create_darknet()
        self.fraud_send = self._create_fraud()
        self.account_check = self._create_account()

    def _create_proxy_vpn(self):
        from .proxyvpn import ProxyVPN
        return ProxyVPN(self)
    
    def _create_phone(self):
        from .phone import Phone
        return Phone(self)
    
    def _create_email(self):
        from .email import Email
        return Email(self)
    
    def _create_url(self):
        from .url import Url
        return Url(self)
    
    def _create_malicious(self):
        from .malicious import Malicious
        return Malicious(self)
    
    def _create_darknet(self):
        from .darknet import Darknet
        return Darknet(self)
    
    def _create_fraud(self):
        from .fraud import Fraud
        return Fraud(self)
    
    def _create_account(self):
        from .account import Account
        return Account(self)
        

    def _request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        url = f"{API_URL}{endpoint}"
        headers = {"Authorization": f"Bearer {self.key}"}
        
        try:
            # Отправка запроса с файлами, если таковые имеются
            response = requests.request(method, url, headers=headers, params=params, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

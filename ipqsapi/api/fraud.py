from typing import Optional, Dict, Any
from ..data.fraud_data import FraudData  # Импортируем класс FraudData

class Fraud:
    def __init__(self, api) -> None:
        """
        Initializes the Fraud class with an API object.
        
        Parameters:
        - api :class:`API` - The API object used to make requests.
        """
        self.api = api

    def send_info(
        self,
        ip: Optional[str] = None,
        email: Optional[str] = None,
        request_id: Optional[str] = None,
        phone: Optional[str] = None,
        country: Optional[str] = None,
        **additional_params
    ) -> FraudData:
        """
        Sends fraud report data to the API.
        
        Parameters:
        - ip :class:`Optional[str]` - The IPv4 or IPv6 address to report.
        - email :class:`Optional[str]` - The email address to report.
        - request_id :class:`Optional[str]` - The request ID to report.
        - phone :class:`Optional[str]` - The phone number to report.
        - country :class:`Optional[str]` - The 2 letter country code or full name of the phone number's country.
        - additional_params :class:`Dict[str, Any]` - Additional optional parameters.
        
        Returns:
        - FraudData: An instance of the FraudData class containing the result of the fraud report submission.
        """
        # Собираем параметры запроса
        params = {
            "ip": ip,
            "email": email,
            "request_id": request_id,
            "phone": phone,
            "country": country
        }
        # Удаляем None значения
        params = {key: value for key, value in params.items() if value is not None}
        # Добавляем дополнительные параметры
        params.update(additional_params)
        
        endpoint = f"report/{self.api.key}"
        data = self.api._request("GET", endpoint, params=params)
        return FraudData(data)

## IPQualityScore API Python Wrapper

This Python wrapper provides an easy-to-use interface to interact with the IPQualityScore API. It supports various endpoints including proxy and VPN checks, email validation, phone number validation, URL validation, file scanning for malware, darknet data checks, fraud reporting, and account usage information.

**API DOCS**: [Fraud Prevention API | IPQS Fraud Detection API Documentation | IPQualityScore](https://www.ipqualityscore.com/documentation/overview)

You can switch between English and Russian documentation using the links below:

- [🇺🇸 English](#English)
- [🇷🇺 Русский](#Русский)

## English

### Overview

The `ipqsapi` library provides an easy-to-use interface for interacting with the IPQualityScore API. The library includes methods for checking proxy/VPN usage, phone numbers, email addresses, URLs, malware, darknet data, and reporting fraud.

### Installation

To install the library, use pip:

```bash
pip install ipqsapi
```

## Usage

Here's a brief overview of how to use the `ipqsapi` library with various endpoints:

### Initialize the API

First, you need to initialize the API with your IPQualityScore API key:

```python
import ipqsapi

api = ipqsapi.API("YOUR_API_KEY_HERE")
```
### Proxy and VPN Check

To check if an IP address is a proxy or VPN, use the `proxyvpn_check` endpoint:

```python
from ipqsapi.data.proxyvpn_data import ProxyVPNData

proxy_vpn = api.proxyvpn_check
response: ProxyVPNData = proxy_vpn.get_info(
    ip_address="23.106.56.43",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    user_language="en-US",
    allow_public_access_points=True,
    mobile=True,
    fast=True,
    strictness=0,
    lighter_penalties=False
)

print(response)

```

### Phone Check

To validate a phone number, use the `phone_check` endpoint:

```python
from ipqsapi.data.phone_data import PhoneData

phone = api.phone_check
response: PhoneData = phone.get_info(
    phone_number="15172938623",
    country="US",
    strictness=1
)

print(response)

```

### Email Check

To validate an email address, use the `email_check` endpoint:

```python
from ipqsapi.data.email_data import EmailData

email = api.email_check
response: EmailData = email.get_info(
    email="sawaglumov2006@gmail.com",
    fast=True,
    timeout=5,
    strictness=1
)

print(response)

```

### URL Check

To check a URL, use the `url_check` endpoint:

```python
from ipqsapi.data.url_data import UrlData

url = api.url_check
response: UrlData = url.get_info(
    url="google.com",
    fast=True,
    timeout=5,
    strictness=1
)

print(response)

```

### Malicious File Check

To scan a file for malware or check a file's previous scan result, use the `malicious_check` endpoint:

```python
https://drive.usercontent.google.com/download?id=1a8n_HxT7QYw-8YOOCH0BnNKQQqdpB4HE&export=download&authuser=0&confirm=t&uuid=1883796e-6f0b-4fc2-b784-ce0f94da9291&at=APZUnTV_A-yM1WjkP04-9qjMynwb:1721654626905from ipqsapi.data.malicious_data import MaliciousData

malicious = api.malicious_check
response: MaliciousData = malicious.get_info(
    file_path_or_url="file.py",
    is_url=False
)

print(response)

# For URL-based file checks
malicious = api.malicious_check
response: MaliciousData = malicious.get_info(
    file_path_or_url="https://drive.usercontent.google.com/download?id=1a8n_HxT7QYw-8YOOCH0BnNKQQqdpB4HE&export=download&authuser=0&confirm=t&uuid=1883796e-6f0b-4fc2-b784-ce0f94da9291&at=APZUnTV_A-yM1WjkP04-9qjMynwb:1721654626905",
    is_url=True
)

print(response)

```

### Darknet Data Check

To check if data has appeared in a darknet leak, use the `darknet_check` endpoint:

```python
from ipqsapi.data.darknet_data import DarknetData

darknet = api.darknet_check
response: DarknetData = darknet.get_info(
    data="SawaPlayGO",
    type="username"
)

print(response)

```

### Fraud Reporting

To report fraudulent data, use the `fraud_send` endpoint:

```python
from ipqsapi.data.fraud_data import FraudData

fraud = api.fraud_send
response: FraudData = fraud.send_info(
    ip="23.106.56.43"
)

print(response)

```

### Account Usage

To get account usage information, use the `account_check` endpoint:

```python
from ipqsapi.data.account_data import AccountData

account = api.account_check
response: AccountData = account.get_info()

print(response)

```

## API Key

Replace `"YOUR_API_KEY_HERE"` with your actual IPQualityScore API key. You can obtain your API key from the [IPQualityScore website](https://www.ipqualityscore.com).

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.

## Contributing

Feel free to submit issues or pull requests. We welcome contributions from the community.

# Русский

## Обзор

Библиотека `ipqsapi` предоставляет удобный интерфейс для взаимодействия с API IPQualityScore. Библиотека включает методы для проверки использования прокси/VPN, телефонных номеров, email-адресов, URL, вредоносного ПО, данных из Даркнета и отчетов о мошенничестве.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ipqsapi
```

## Использование

Вот краткий обзор использования библиотеки `ipqsapi` с различными конечными точками:

### Инициализация API

Сначала нужно инициализировать API с вашим ключом API IPQualityScore:

```python
import ipqsapi

api = ipqsapi.API("ВАШ_API_КЛЮЧ")
```

### Проверка прокси/VPN

Для проверки, является ли IP-адрес прокси или VPN, используйте конечную точку `proxyvpn_check`:

```python
from ipqsapi.data.proxyvpn_data import ProxyVPNData

proxy_vpn = api.proxyvpn_check
response: ProxyVPNData = proxy_vpn.get_info(
    ip_address="23.106.56.43",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    user_language="ru-RU",
    allow_public_access_points=True,
    mobile=True,
    fast=True,
    strictness=0,
    lighter_penalties=False
)

print(response)

```

### Проверка телефона

Для проверки телефонного номера используйте конечную точку `phone_check`:

```python
from ipqsapi.data.phone_data import PhoneData

phone = api.phone_check
response: PhoneData = phone.get_info(
    phone_number="15172938623",
    country="US",
    strictness=1
)

print(response)

```

### Проверка email

Для проверки email-адреса используйте конечную точку `email_check`:

```python
from ipqsapi.data.email_data import EmailData

email = api.email_check
response: EmailData = email.get_info(
    email="sawaglumov2006@gmail.com",
    fast=True,
    timeout=5,
    strictness=1
)

print(response)

```

### Проверка URL

Для проверки URL используйте конечную точку `url_check`:

```python
from ipqsapi.data.url_data import UrlData

url = api.url_check
response: UrlData = url.get_info(
    url="google.com",
    fast=True,
    timeout=5,
    strictness=1
)

print(response)

```

### Проверка вредоносного ПО

Для сканирования файла на наличие вредоносного ПО или проверки предыдущего сканирования файла используйте конечную точку `malicious_check`:

```python
from ipqsapi.data.malicious_data import MaliciousData

# Локальный файл
malicious = api.malicious_check
response: MaliciousData = malicious.get_info(
    file_path_or_url="file.py",
    is_url=False
)

print(response)

# Проверка файла по URL
malicious = api.malicious_check
response: MaliciousData = malicious.get_info(
    file_path_or_url="https://drive.usercontent.google.com/download?id=1a8n_HxT7QYw-8YOOCH0BnNKQQqdpB4HE&export=download&authuser=0&confirm=t&uuid=1883796e-6f0b-4fc2-b784-ce0f94da9291&at=APZUnTV_A-yM1WjkP04-9qjMynwb:1721654626905",
    is_url=True
)

print(response)

```

### Проверка данных из Даркнета

Для проверки, появились ли данные в утечке из Даркнета, используйте конечную точку `darknet_check`:

```python
from ipqsapi.data.darknet_data import DarknetData

darknet = api.darknet_check
response: DarknetData = darknet.get_info(
    data="SawaPlayGO",
    type="username"
)

print(response)

```

### Отчёт о мошенничестве

Для сообщения о мошенничестве используйте конечную точку `fraud_send`:

```python
from ipqsapi.data.fraud_data import FraudData

fraud = api.fraud_send
response: FraudData = fraud.send_info(
    ip="23.106.56.43"
)

print(response)

```

### Информация о использовании аккаунта

Для получения информации о использовании аккаунта используйте конечную точку `account_check`:

```python
from ipqsapi.data.account_data import AccountData

account = api.account_check
response: AccountData = account.get_info()

print(response)

```

## API Ключ

Замените `"ВАШ_API_КЛЮЧ"` на ваш реальный ключ API IPQualityScore. Вы можете получить ваш API ключ на [веб-сайте IPQualityScore](https://www.ipqualityscore.com).

## Лицензия

Этот проект лицензируется под лицензией MIT - смотрите файл [LICENSE](LICENSE) для деталей.

## Участие

Не стесняйтесь сообщать об ошибках или отправлять pull-запросы. Мы приветствуем вклад от сообщества.


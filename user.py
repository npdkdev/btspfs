from dataclasses import dataclass
from typing import Final
import requests

@dataclass
class Address:
    address: str
    city: str
    country: str
    district: str
    formatted_address: str
    geo_string: str
    id: int
    name: str
    phone: str
    state: str
    town: str
    zipcode: int


@dataclass
class User:
    userid: int
    shopid: int
    name: str
    email: str
    phone: str
    phone_verified: bool
    default_address: Address
    cookie: str
    csrf_token: str
    with open("user_agent.txt", 'r') as __user_agent:
        USER_AGENT: Final[str] = __user_agent.read()

    @staticmethod
    def exec(cookie: str):
        csrf_token = cookie.split("csrftoken=")[1].split(";")[0]
        header = {
            "Host": "shopee.co.id",
            "X-Shopee-Language": "id",
            "If-None-Match-": "8001",
            "X-API-SOURCE": "pc",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://shopee.co.id/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Cookie": cookie.strip(),
            "X-Csrftoken": csrf_token
        }
        resp = requests.get("https://shopee.co.id/api/v1/account_info/?need_cart=0&skip_address=0",headers=header)
        data = resp.json()

        if len(data) == 0:
            raise Exception("failed to login, invalid cookie")

        return User(
            userid=data["userid"],
            shopid=data["shopid"],
            name=data["username"],
            email=data["email"],
            phone=data["phone"],
            phone_verified=data["phone_verified"],
            default_address=Address(
                address=data["default_address"]["address"],
                city=data["default_address"]["city"],
                country=data["default_address"]["country"],
                district=data["default_address"]["district"],
                formatted_address=data["default_address"]["formattedAddress"],
                geo_string=data["default_address"]["geoString"],
                id=data["default_address"]["id"],
                name=data["default_address"]["name"],
                phone=data["default_address"]["phone"],
                state=data["default_address"]["state"],
                town=data["default_address"]["town"],
                zipcode=data["default_address"]["zipcode"]
            ),
            cookie=cookie,
            csrf_token=csrf_token
        )
         

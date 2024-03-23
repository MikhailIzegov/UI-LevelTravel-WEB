import os
import dataclasses
from dotenv import load_dotenv


def load_env():
    load_dotenv()


load_env()


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    phone_number: str
    email: str
    password: str
    destination: str
    start_date: str
    end_date: str
    stars: str


test_user = User(
        first_name='Михаил',
        last_name='Изегов',
        phone_number='0000',
        email=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD'),
        destination='Дубай',
        start_date='001',
        end_date='028',
        stars='5'
        )

# class DataForTests:
#     def __init__(self):
#         self.login = os.getenv('LOGIN')
#         self.password = os.getenv('PASSWORD')


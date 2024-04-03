import os
import dataclasses
from dotenv import load_dotenv


def load_env():
    load_dotenv()


load_env()


@dataclasses.dataclass
class User:
    first_name_ru: str
    last_name_ru: str
    first_name_en: str
    last_name_en: str
    phone_number: str
    email: str
    password: str
    destination: str
    start_date: str
    end_date: str
    stars: str
    rating: str
    regions: list
    budget_from: str


test_user = User(
        first_name_ru='Михаил',
        last_name_ru='Изегов',
        first_name_en='Mikhail',
        last_name_en='Izegov',
        phone_number=os.getenv('PHONE_NUMBER'),
        email=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD'),
        destination='Дубай',
        start_date='015',
        end_date='028',
        stars='5',
        rating='9',
        regions=['Бар Дубай', 'Джебель-Али'],
        budget_from='100000'
        )

# class DataForTests:
#     def __init__(self):
#         self.login = os.getenv('LOGIN')
#         self.password = os.getenv('PASSWORD')


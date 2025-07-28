import dataclasses
import os
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    MUSIC = "Music"
    READING = "Reading"


class State (Enum):
    NCR = "NCR"
    UTTAR_PRADESH = "Uttar Pradesh"
    HARYANA = "Haryana"
    RAJASTHAN = "Rajasthan"


@dataclasses.dataclass
class User:
    first_name: str = 'Test'
    last_name: str = 'Testov'
    email: str = 'test.testov@gmail.com'
    gender: Gender = Gender.MALE
    phone_number: str = '9839583958'
    birth_year: str = '1996'
    birth_month: str = 'July'
    birth_day: str = '08'
    subject: str = 'Computer Science'
    hobbies: Hobby = Hobby.SPORTS
    picture: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'demoqa.jpg'))
    address: str = 'St. Petersburg, Lomanosovskaya street'
    state: State = State.UTTAR_PRADESH
    city: str = 'Agra'

import enum
from dataclasses import dataclass
from typing import Optional


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobbies(enum.Enum):
    SPORTS = "Sports"
    MUSIC = "Music"
    READING = "Reading"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    day: str
    month: str
    year: str
    subject: Optional[str]
    hobby: Optional[Hobbies]
    picture: Optional[str]
    address: Optional[str]
    state: Optional[str]
    city: Optional[str]

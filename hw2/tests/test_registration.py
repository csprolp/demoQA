from hw2.models.user import User, Gender, Hobbies
from hw2.pages.RegistrationForm import RegistrationForm


def test_registration():
    registrate_user = User(
        first_name="Imya",
        last_name="Familiya",
        email="test@test.ru",
        number="1234567890",
        gender=Gender.MALE,
        day="19",
        month="4",
        year="1996",
        subject="Math",
        hobby=Hobbies.MUSIC,
        picture="picture.jpg",
        address="Any address",
        state="Uttar Pradesh",
        city="Agra",
    )
    form_for_register = RegistrationForm()
    form_for_register.open()

    form_for_register.register(registrate_user)
    form_for_register.register_user(registrate_user)

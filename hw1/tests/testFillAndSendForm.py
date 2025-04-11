from hw1.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    (
        (registration_page.open().fill_first_name("Imya"))
        .fill_last_name("Familiya")
        .fill_email("test@test.ru")
        .choice_gender("Male")
        .fill_number("1234567890")
        .choice_date_of_birth("4", "1996", "09")
        .fill_subjects("Commerce", "Maths")
        .choice_hobbies("Sports", "Music")
        .upload_picture("picture.jpg")
        .fill_address("Unique address")
        .select_state("Uttar Pradesh")
        .select_city("Agra")
        .submit_form()
    )
    registration_page.should_have_registered(
        "Imya Familiya",
        "test@test.ru",
        "Male",
        "1234567890",
        "09 May,1996",
        "Commerce, Maths",
        "Sports, Music",
        "picture.jpg",
        "Unique address",
        "Uttar Pradesh Agra",
    )

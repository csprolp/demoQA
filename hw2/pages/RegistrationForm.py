import calendar
import os

from selene import browser, have, command

from hw2.models.user import User


class RegistrationForm:

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def register(self, user: User):
        browser.element("#firstName").type(user.first_name)
        browser.element("#lastName").type(user.last_name)
        browser.element("#userEmail").type(user.email)
        browser.all("[name=gender]").element_by(have.value(user.gender.value)).element(
            ".."
        ).click()
        browser.element("#userNumber").type(user.number)

        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(
            f'[value="{user.month}"]'
        ).click()
        browser.element(".react-datepicker__year-select").click().element(
            f'option[value="{user.year}"]'
        ).click()
        browser.element(f".react-datepicker__day--0{user.day}").click()

        if user.subject:
            browser.element("#subjectsInput").type(user.subject).press_enter()

        if user.hobby:
            browser.all(f'[for^="hobbies-checkbox-"]').element_by(
                have.exact_text(user.hobby.value)
            ).perform(command.js.click)

        if user.picture:
            browser.element("#uploadPicture").send_keys(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), f"../../files/{user.picture}"
                    )
                )
            )

        if user.address:
            browser.element("#currentAddress").type(user.address)

        if user.state:
            browser.element("#state").click()
            browser.all("[id^=react-select][id*=option]").element_by(
                have.exact_text(user.state)
            ).click()

        if user.city:
            browser.element("#city").click()
            browser.all("[id^=react-select][id*=option]").element_by(
                have.exact_text(user.city)
            ).click()

        browser.element("#submit").click()

    def register_user(self, user: User):
        result = browser.element(".table").all("td").even
        result.should(
            have.texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender.value,
                user.number,
                f"{user.day} {calendar.month_name[int(user.month)+1]},{user.year}",
                user.subject if user.subject else "",
                user.hobby.value if user.hobby else "",
                user.picture,
                user.address,
                user.state + " " + user.city,
            )
        )

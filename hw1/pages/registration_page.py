import os.path

from selene import browser, have, command


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def choice_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()
        return self

    def fill_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def choice_date_of_birth(self, month, year, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(
            f'[value="{month}"]'
        ).click()
        browser.element(".react-datepicker__year-select").click().element(
            f'option[value="{year}"]'
        ).click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, *values):
        for value in values:
            browser.element("#subjectsInput").type(value).press_enter()
        return self

    def choice_hobbies(self, *values):
        for value in values:
            browser.all(f'[for^="hobbies-checkbox-"]').element_by(
                have.exact_text(value)
            ).perform(command.js.click)
        return self

    def upload_picture(self, filename):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), f"../../files/{filename}")
            )
        )
        return self

    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def select_state(self, value):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    def select_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit_form(self):
        browser.element("#submit").click()
        return self

    def should_have_registered(
        self,
        full_name,
        email,
        gender,
        phone,
        date_of_birth,
        subject,
        hobbies,
        picture,
        current_address,
        state_and_city,
    ):

        browser.element(".table").all("td").even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobbies,
                picture,
                current_address,
                state_and_city,
            )
        )

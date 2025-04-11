import os.path

import allure
from selene import browser, have, command


def testFillAndSendForm():
    with allure.step("Заполнение формы"):
        browser.open("/automation-practice-form")
        browser.element("#firstName").type("Imya")
        browser.element("#lastName").type("Familiya")
        browser.element("#userEmail").type("checkemail@mail.tst")
        browser.element("#genterWrapper").element("#gender-radio-1").perform(
            command.js.click
        )
        browser.element("#userNumber").type("1234565432")
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(
            'option[value="4"]'
        ).click()
        browser.element(".react-datepicker__year-select").click().element(
            'option[value="1996"]'
        ).click()
        browser.element(".react-datepicker__day--001").click()
        browser.element("#subjectsInput").type("Commerce")
        browser.element(".subjects-auto-complete__menu").click()
        browser.element("#hobbies-checkbox-1").perform(command.js.click)
        browser.element("#uploadPicture").send_keys(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../../files/picture.jpg"
            )
        )
        browser.element("#currentAddress").type("Unique address")
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element("#state").click().element("#react-select-3-option-0").click()
        browser.element("#city").click().element("#react-select-4-option-0").click()
        browser.element("#submit").click()
    with allure.step("Проверка формы"):
        browser.element("#example-modal-sizes-title-lg").should(
            have.exact_text("Thanks for submitting the form")
        )
        browser.all(".table td:nth-child(2)").should(
            have.exact_texts(
                "Imya Familiya",
                "checkemail@mail.tst",
                "Male",
                "1234565432",
                "01 May,1996",
                "Commerce",
                "Sports",
                "picture.jpg",
                "Unique address",
                "NCR Delhi",
            )
        )

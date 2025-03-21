import os.path

from selene import browser, have, command
from selene.support.conditions.have import exact_text


def testFillAndSendForm():
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
    browser.element("#uploadPicture").send_keys(os.path.abspath("../files/picture.jpg"))
    browser.element("#currentAddress").type("Unique address")
    browser.element("#state").click().element("#react-select-3-option-0").click()
    # разобраться почему не работает такой поиск элемента(выбирает с другим текстом)
    # browser.all(".css-26l3qy-menu").element_by(have.text("NCR")).click()
    browser.element("#city").click().element("#react-select-4-option-0").click()
    browser.element("#submit").click()

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

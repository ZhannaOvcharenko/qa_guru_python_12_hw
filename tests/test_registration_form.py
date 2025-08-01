import allure
from allure_commons.types import Severity
from data.users import User
from pages.registration_page import RegistrationPage


@allure.tag("demo_qa")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.feature("Проверка успешной регистрации студента")
@allure.story("Проверки для формы регистрации студентов")
@allure.link("http://demoqa.com/automation-practice-form", name="Testing")
def test_registration_form():
    registration_page = RegistrationPage()
    est_user = User()

    with allure.step("Открыть форму регистрации студента"):
        registration_page.open()

    with allure.step("Заполнить поля формы регистрации"):
        registration_page.register_user(test_user)

    with allure.step("Проверить результат заполнения формы регистрации"):
        registration_page.should_registered_user_with(test_user)

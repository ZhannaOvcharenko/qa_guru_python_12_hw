import os
from selene import browser, have, be, command
from data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.all('#hobbiesWrapper label')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.registered_user = browser.all('.table-responsive tbody tr td:nth-of-type(2)')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def choose_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def fill_phone_number(self, value):
        self.phone.type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choose_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def choose_hobbies(self, value):
        self.hobby.element_by(have.exact_text(value)).should(be.visible).perform(command.js.scroll_into_view).click()
        return self

    def upload_picture(self, value):
        self.picture.send_keys(os.path.abspath(value))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def choose_state(self, value):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(value)
        browser.element('div[id^="react-select-3-option"]').should(have.exact_text(value)).click()
        return self

    def choose_city(self, value):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(value)
        browser.element('div[id^="react-select-4-option"]').should(have.exact_text(value)).click()
        return self

    def submit_form(self):
        self.submit.click()
        return self

    def register_user(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender.value)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.birth_day, user.birth_month, user.birth_year)
        self.choose_subject(user.subject)
        self.choose_hobbies(user.hobbies.value)
        self.upload_picture(user.picture)
        self.fill_current_address(user.address)
        self.choose_state(user.state.value)
        self.choose_city(user.city)
        self.submit_form()
        return self

    def should_registered_user_with(self, user: User):
        self.registered_user.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                f'{user.email}',
                f'{user.gender.value}',
                f'{user.phone_number}',
                f'{user.birth_day} {user.birth_month},{user.birth_year}',
                f'{user.subject}',
                f'{user.hobbies.value}',
                os.path.basename(user.picture),
                f'{user.address}',
                f'{user.state.value} {user.city}'
            )
        )
        return self

from steps.PersonalDataSteps import PersonalDataSteps, InputAnnotationsErrors
from .BasePage import *


class Data_page(Page):
    BASE_URL = "https://id.mail.ru/profile"
    PATH = ""

    @property
    def personal_data_steps(self):
        return PersonalDataSteps(self.driver)

    def change_avatar(self, path):
        self.personal_data_steps.upload_avatar(path)
        self.personal_data_steps.click_submit_avatar_btn()
        return self.personal_data_steps.check_if_uploaded()

    def fill_form(
            self, name: str, last_name: str, nickname: str, city: str, collect_err_about: str = ""
    ) -> InputAnnotationsErrors:
        self.personal_data_steps.fill_name(name)
        self.personal_data_steps.fill_last_name(last_name)
        self.personal_data_steps.fill_nickanme(nickname)
        self.personal_data_steps.fill_city(city)
        self.personal_data_steps.click_submit()
        return self.personal_data_steps.collect_errors(collect_err_about)

    def reload(self):
        self.open(self.BASE_URL)

from steps.BaseSteps import BaseSteps


class AttachmentSelect(BaseSteps):
    OPEN_BUTTON = '//span[@data-test-id="createFolder-select-value"]'
    FOLDER_TOP_SELECT = '//div[@data-test-id="select-value:-1"]'
    INCOMING_SELECT = '//div[@data-test-id="select-value:0"]'
    SENT_SELECT = '//div[@data-test-id="select-value:500000"]'
    DRAFTS_SELECT = '//div[@data-test-id="select-value:500001"]'

    def open(self):
        self.wait_until_and_get_elem_by_xpath(self.OPEN_BUTTON).click()

    def select_folder_top(self):
        self.wait_to_be_clickable_by_xpath(self.FOLDER_TOP_SELECT).click()

    def select_incoming(self):
        self.wait_to_be_clickable_by_xpath(self.INCOMING_SELECT).click()

    def select_sent(self):
        self.wait_to_be_clickable_by_xpath(self.SENT_SELECT).click()

    def select_drafts(self):
        self.wait_to_be_clickable_by_xpath(self.DRAFTS_SELECT).click()

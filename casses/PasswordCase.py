import unittest

from casses.base.BaseTest import BaseTest
from pages.PasswordPopup import PasswordPopup


class PasswordTest(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        super(PasswordTest, self).setUp()
        password_page = PasswordPopup(self.driver)
        password_page.open()
        self.page = PasswordPopup(self.driver)

    def test_send_empty_form(self) -> None:
        self.page.send_empty_form()
        self.assertTrue(
            self.page.is_new_password_error()
            and self.page.is_current_password_error()
            and self.page.is_repeat_password_error()
        )

    def test_change_password(self) -> None:
        NEW_PASSWORD = '12893490278kek'
        self.page.change_password(self.PASSWORD, NEW_PASSWORD)
        changed = self.page.is_password_changed()
        self.page.open()

        self.page.change_password(NEW_PASSWORD, self.PASSWORD)
        changed_again = self.page.is_password_changed()
        self.assertTrue(changed and changed_again)

    def test_change_password_with_invalid_repeat_password(self) -> None:
        NEW_PASSWORD = '12893490278kek'

        self.page.send_form_with_uncorrect_repeat(NEW_PASSWORD, self.PASSWORD)
        self.assertTrue(self.page.is_repeat_password_equal())

    def test_generate_password(self) -> None:
        self.page.generate_password()
        self.assertEqual(
            self.page.get_repeat_password_value(), self.page.get_new_password_value()
        )

    def test_long_new_password(self) -> None:
        self.page.set_new_password("12345678aB12345678aB12345678aB12345678aB1")
        self.assertTrue(self.page.check_password_security_value_equal('block'))

    def test_numeric_new_password(self) -> None:
        self.page.set_new_password("1234567890")
        self.assertTrue(self.page.check_password_security_value_equal('error'))

    def test_small_new_password(self) -> None:
        self.page.set_new_password("aa12A")
        self.assertTrue(self.page.check_password_security_value_equal('error'))

    def test_close_popup(self) -> None:
        self.page.close_popup()
        self.assertFalse(self.page.is_popup_open())

    def test_cancel_popup(self) -> None:
        self.page.cancel()
        self.assertFalse(self.page.is_popup_open())

    def test_password_visibility(self) -> None:
        self.page.change_fields(self.PASSWORD, "PASSW0RdD")
        self.page.change_new_password_visibility()
        self.page.change_old_password_visibility()
        is_success = self.page.is_new_password_visible() and self.page.is_old_password_visibile()
        self.page.change_new_password_visibility()
        self.page.change_old_password_visibility()
        self.assertTrue(
            not (self.page.is_new_password_visible() or self.page.is_old_password_visibile()) and is_success)

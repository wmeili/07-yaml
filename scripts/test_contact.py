import time
import pytest
import yaml

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"), analyze_file("contact_data", "test_add_contact"))
    def test_add_contact(self, name, phone):
        self.page.contact_list.click_add_contact()
        self.page.add_contact.input_name(name)
        self.page.add_contact.input_phone(phone)

    @pytest.mark.parametrize(("nickname", "phone"), analyze_file("contact_data", "test_add_nickname"))
    def test_add_nickname(self, nickname, phone):
        self.page.contact_list.click_add_contact()
        self.page.add_contact.input_nickname(nickname)
        self.page.add_contact.input_phone(phone)

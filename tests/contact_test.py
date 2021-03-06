import pytest
from applitools.selenium import Target

from base.conftest import Setup
from pages.BasePage import BasePage
from base.read_json_data import read_data
from time import sleep
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@pytest.mark.usefixtures('set_up')
class TestContact(Setup):
    @pytest.mark.demoblaze
    @pytest.mark.usefixtures("eyes")
    @pytest.mark.parametrize("email, name, message", read_data("./data_files/contact_data.json"))
    def test_contact(self, email, name, message):
        driver = self.driver
        eyes = self.eyes
        eyes.open(driver, "Demoblaze", "Contact test", {"width": 2560, "height": 1440})
        eyes.check("Contact Window test", Target.window())
        basePage = BasePage(driver)
        print("clicking on contact button...")
        basePage.click_on_contact()
        print("filling email...")
        basePage.enter_contact_email(email)
        print("filling name...")
        basePage.enter_contact_name(name)
        print("filling message...")
        basePage.enter_contact_message(message)
        sleep(1)
        print("submitting information...")
        basePage.submit_contact()
        basePage.get_alert()
        eyes.check("Contact submitted", Target.window())
        eyes.close(False)


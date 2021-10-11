from .base_page import BasePage
from .locators import index
from .locators import search
from .locators import register
from .locators import reg_page
import time



class RegPage(BasePage):
    def entrering_reg_data(self):
        self.send_keys(*reg_page.FIRSTNAME)
        self.send_keys(*reg_page.LASTNAME)
        self.send_keys(*reg_page.EMAIL)
        self.send_keys(*reg_page.TELEPHONE)
        self.send_keys(*reg_page.PASSWORD)
        self.send_keys(*reg_page.PASSWORDCONFIRM)
        self.click_element(*reg_page.PRIVATEPOLICE)
        self.click_element(*reg_page.CONTINUE)

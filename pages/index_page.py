from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .locators import index, order_page
from .locators import search
from .locators import register
from .locators import reg_page
import time

class IndexPage(BasePage): 
    def view_index_page(self):
        assert self.is_element_present(*index.HEADER), "The page was not loaded"

    def go_to_index_page(self):
        self.click_element(*reg_page.INDEXPAGE)
    def search_in_index_page(self):
        self.send_keys(*index.SEARCH)
        self.click_element(*index.SEARCHBUTTON)
        assert self.is_element_present(*search.RESULT), "Result is not valid"

    def add_to_cart(self):
        self.click_element(*index.ADDTOCART)
        time.sleep(3)
        assert self.is_element_present(*index.TOTALCART)

    def add_to_wish_list(self):
        self.click_element(*index.ADDTOWISH)
        time.sleep(1)
        assert self.is_element_present(*index.WISHLIST)
    def go_to_registration_page(self):
        time.sleep(1)
        self.click_element(*index.MYPROFILE)
        time.sleep(1)
        self.click_element(*index.REGISTERBUTTON)
        time.sleep(1)
        assert self.is_element_present(*register.HEADER), "Registration page is not found"

    def entrering_reg_data(self):
        self.send_keys_first_name(*reg_page.FIRSTNAME)
        self.send_keys_last_name(*reg_page.LASTNAME)
        self.send_keys_email(*reg_page.EMAIL)
        self.send_keys_telephone(*reg_page.TELEPHONE)
        self.send_keys_Password(*reg_page.PASSWORD)
        self.send_keys_Password(*reg_page.PASSWORDCONFIRM)
        self.click_element(*reg_page.PRIVATEPOLICE)
        time.sleep(3)
        self.click_element(*reg_page.CONTINUE)

        assert self.is_element_present(*reg_page.SUCCESSPAGEREG), "Registration failed"


    def make_order(self):
        self.click_element(*index.CARTBUTTON)
        self.click_element(*index.CHECKOUT)
        #self.click_element(*order_page.NEWADDRESS)
        self.send_keys_first_name(*order_page.FIRSTNAME)
        self.send_keys_last_name(*order_page.LASTNAME)
        self.send_keys_Address1(*order_page.ADDRESS1)
        self.send_keys_City(*order_page.CITY)
        self.send_keys_Postcode(*order_page.POSTCODE)
        self.click_element(*order_page.REGION)
        self.send_keys_Region(*order_page.REGION)
        self.click_element(*order_page.REGION)
        self.click_element(*order_page.CONTINUESTEP2)
        time.sleep(1)
        self.click_element(*order_page.CONTINUESTEP3)
        time.sleep(1)
        self.send_keys(*order_page.COMMENTABOUTORDER)
        time.sleep(1)
        self.click_element(*order_page.CONTINUESTEP4)
        time.sleep(1)
        self.send_keys(*order_page.COMMETNABOUTPAYMENT)
        time.sleep(1)
        self.click_element(*order_page.TERMS)
        time.sleep(1)
        self.click_element(*order_page.CONTINUESTEP5)
        time.sleep(1)
        self.click_element(*order_page.CONFIRMORDER)
        assert self.is_element_present(*order_page.SUCCESSPAGEORDR), "Order failed"
from .base_page import BasePage
from .locators import index
from .locators import search
import time

class IndexPage(BasePage): 
    def view_index_page(self):
        assert self.is_element_present(*index.HEADER), "The page was not loaded"
        
    def search_in_index_page(self):
        self.send_keys(*index.SEARCH)
        self.click_element(*index.SEARCHBUTTON)
        assert self.is_element_present(*search.RESULT), "Result is not valid"

    def add_to_cart(self):
        self.click_element(*index.ADDTOCART)
        time.sleep(3)
        assert self.is_element_present(*index.TOTALCAR)

    def add_to_wish_list(self):
        self.click_element(*index.ADDTOWISH)
        time.sleep(3)
        assert self.is_element_present(*index.WISHLIST)
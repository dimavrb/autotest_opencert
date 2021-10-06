from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

from .login_page import LoginPage
# from .locators import LoginPageLocators

# class MyAccountPage(BasePage):
  #  def should_be_login_page(self):
   #     self.should_be_login_url()
  #      self.should_be_login_form()
 #       self.should_be_register_form()
#
   # def should_be_login_url(self):
  #      assert 'login' in self.browser.current_url, "URL is not login"        
# реализуйте проверку на корректный url адрес
 #       assert True
#
   # def should_be_login_form(self):
    #    assert self.is_element_present(*LoginPageLocators.login_form), "Login link is not presented"           
# реализуйте проверку, что есть форма логина
   #     assert True

  #  def should_be_register_form(self):
 #       assert self.is_element_present(*LoginPageLocators.register_form), "Login link is not presented"   
# реализуйте проверку, что есть форма регистрации на странице
#        assert True
        
        
        

class MyAccountPageLocators:
    LOCATOR_BREAD_CRUMB = (By.CLASS_NAME, "breadcrumb")
    LOCATOR_LIST_GROUP = (By.CLASS_NAME,"list-group")
    LOCATOR_MENU = (By.ID,"menu")
    LOCATOR_SEARCH_BAR = (By.ID,"search")
    LOCATOR_CART_DROPDOWN = (By.ID,"cart-total")
    LOCATOR_TOP = (By.ID,"top")
    LOCATOR_FOOTER = (By.TAG_NAME,"footer")
    


class MyAccountPage(BasePage):
    def ElementsofPage(self):
        self.BreadCrumb()
    
    def BreadCrumb(self):
        assert self.is_element_present(*LoginPageLocators.LOCATOR_BREAD_CRUMB), "BreadCrumb not found"
        assert True

       
       
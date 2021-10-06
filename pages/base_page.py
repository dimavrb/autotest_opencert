from selenium.common.exceptions import NoSuchElementException
class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def find_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def click_element(self, how, what):
        element = self.browser.find_element(how, what).click()
    
    def send_keys(self, how, what):
        element = self.browser.find_element(how, what).send_keys('HP')
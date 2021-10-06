from selenium.webdriver.common.by import By


class index(object):
    HEADER = (By.CSS_SELECTOR, '#top')
    LOGO= (By.CSS_SELECTOR, '#lgo')
    SEARCH= (By.CSS_SELECTOR, '#search > input')
    CART= (By.CSS_SELECTOR, '#cart')
    TOTALCAR = (By.XPATH, "//*[contains(text(),' 1 item(s)')]")
    ADDTOCART = (By.XPATH, "//div[@class='button-group'][1]")
    NAVBAR = (By.CSS_SELECTOR, '#category')
    SLIDESHOW= (By.CSS_SELECTOR, '#slideshow0')
    SLIDER = (By.CSS_SELECTOR, '#carousel0')
    SEARCHBUTTON=(By.CSS_SELECTOR, '#search > span > button')
    ADDTOWISH = (By.XPATH, "//div[@class='button-group']/button[@data-original-title='Add to Wish List'][last()]")
    WISHLIST = (By.XPATH, "//*[contains(text(),'wish list')]")


class search(object):
    RESULT = (By.XPATH, './/a[text() = "HP LP3065"]')
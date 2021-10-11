from selenium.webdriver.common.by import By


class index(object):
    HEADER = (By.CSS_SELECTOR, '#top')
    LOGO= (By.CSS_SELECTOR, '#lgo')
    SEARCH= (By.CSS_SELECTOR, '#search > input')
    CART= (By.CSS_SELECTOR, '#cart')
    TOTALCART = (By.XPATH, "//*[contains(text(),' 1 item(s)')]")
    ADDTOCART = (By.XPATH, "//div[@class='button-group'][1]")
    NAVBAR = (By.CSS_SELECTOR, '#category')
    SLIDESHOW= (By.CSS_SELECTOR, '#slideshow0')
    SLIDER = (By.CSS_SELECTOR, '#carousel0')
    SEARCHBUTTON=(By.CSS_SELECTOR, '#search > span > button')
    ADDTOWISH = (By.XPATH, "//div[@class='button-group']/button[@data-original-title='Add to Wish List'][last()]")
    WISHLIST = (By.XPATH, "//*[contains(text(),'wish list')]")
    MYPROFILE = (By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]")
    REGISTERBUTTON = (By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[1]/a[1]")
class register(object):
    HEADER = (By.XPATH, "//h1[contains(text(),'Register Account')]")

class search(object):
    RESULT = (By.XPATH, './/a[text() = "HP LP3065"]')
class reg_page(object):
    FIRSTNAME = (By.XPATH, "//input[@id='input-firstname']")
    LASTNAME = (By.XPATH, "//input[@id='input-lastname']")
    EMAIL = (By.XPATH,"//input[@id='input-email']")
    TELEPHONE = (By.XPATH, "//input[@id='input-telephone']")
    PASSWORD = (By.XPATH, "//input[@id='input-password']")
    PASSWORDCONFIRM = (By.XPATH, "//input[@id='input-confirm']")
    PRIVATEPOLICE = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    CONTINUE = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]")
    SUCCESSPAGEREG = (By.XPATH, "// a[contains(text(), 'Success')]")
from selenium.webdriver.common.by import By

#Написать нормальные локаторы с XPATH
class index(object):
    HEADER = (By.CSS_SELECTOR, '#top')
    LOGO= (By.CSS_SELECTOR, '#lgo')
    SEARCH= (By.CSS_SELECTOR, '#search > input')
    CART= (By.CSS_SELECTOR, '#cart')
    TOTALCART = (By.XPATH, "//*[contains(text(),' 1 item(s)')]")
    ADDTOCART = (By.XPATH, "//body/div[@id='common-home']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]/span[1]")
    NAVBAR = (By.CSS_SELECTOR, '#category')
    SLIDESHOW= (By.CSS_SELECTOR, '#slideshow0')
    SLIDER = (By.CSS_SELECTOR, '#carousel0')
    SEARCHBUTTON=(By.CSS_SELECTOR, '#search > span > button')
    ADDTOWISH = (By.XPATH, "//div[@class='button-group']/button[@data-original-title='Add to Wish List'][last()]")
    WISHLIST = (By.XPATH, "//*[contains(text(),'wish list')]")
    MYPROFILE = (By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]")
    REGISTERBUTTON = (By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]/ul[1]/li[1]/a[1]")
    CARTBUTTON = (By.XPATH, "//header/div[1]/div[1]/div[3]/div[1]/button[1]")
    CHECKOUT = (By.XPATH, "//body[1]/header[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/div[1]/p[1]/a[2]/strong[1]")

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
    INDEXPAGE = (By.XPATH, "//a[contains(text(),'Your Store')]")

class order_page(object):
    NEWADDRESS = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[3]/label[1]")
    FIRSTNAME = (By.XPATH, "//input[@id='input-payment-firstname']")
    LASTNAME = (By.XPATH, "//input[@id='input-payment-lastname']")
    ADDRESS1 = (By.XPATH, "//input[@id='input-payment-address-1']")
    CITY = (By.XPATH, "//input[@id='input-payment-city']")
    POSTCODE = (By.XPATH, " //input[@id='input-payment-postcode']")
    COUTNRY = (By.XPATH, "//select[@id='input-payment-country']")
    REGION = (By.XPATH, " //select[@id='input-payment-zone']")
    CONTINUESTEP2 = (By.XPATH, " //input[@id='button-payment-address']")
    CONTINUESTEP3 = (By.XPATH, "//input[@id='button-shipping-address']")
    COMMENTABOUTORDER = (By.XPATH, "//body/div[@id='checkout-checkout']/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/p[4]/textarea[1]")
    CONTINUESTEP4 = (By.XPATH, "//input[@id='button-shipping-method']")
    COMMETNABOUTPAYMENT = (By.XPATH, "//body/div[@id='checkout-checkout']/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/p[3]/textarea[1]")
    CONTINUESTEP5 = (By.XPATH, "//input[@id='button-payment-method']")
    TERMS = (By.XPATH, "//body/div[@id='checkout-checkout']/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/input[1]")
    CONFIRMORDER = (By.XPATH, "//input[@id='button-confirm']")
    SUCCESSPAGEORDR = (By.XPATH, "//h1[contains(text(),'Your order has been placed!')]")

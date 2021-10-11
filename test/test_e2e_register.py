from pages.index_page import IndexPage
from pages.reg_page import RegPage



def test_e2e_registration(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.view_index_page()
    page.go_to_registration_page()
    page.entrering_reg_data()

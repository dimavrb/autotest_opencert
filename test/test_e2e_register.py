from pages.index_page import IndexPage



def test_e2e_registration(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.view_index_page()
    page.go_to_registration_page()

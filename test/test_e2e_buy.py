from pages.index_page import IndexPage

def test_buy_notebook(browser):

    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.view_index_page()
    page.go_to_registration_page()
    page.entrering_reg_data()
    page.go_to_index_page()
    page.add_to_cart()
    page.make_order()
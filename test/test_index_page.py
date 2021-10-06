from pages.index_page import IndexPage

    
def test_index_page(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.view_index_page()

def test_search_bar(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.search_in_index_page()

def test_add_to_cart(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.add_to_cart()

def test_add_to_wish_list(browser):
    link = "http://localhost/index.php"
    page = IndexPage(browser, link)
    page.open()
    page.add_to_wish_list()
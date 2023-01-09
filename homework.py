def print_metadata(name_func, *args):
    full_name = name_func.__name__.title().replace("_", " ")
    print(full_name, *args)


def open_browser(browser_name):
    print_metadata(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_metadata(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_metadata(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://vk.com/")
find_registration_button_on_login_page(page_url="https://vk.com/", button_text="login")

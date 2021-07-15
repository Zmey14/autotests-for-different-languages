import pytest
import time


def test_find_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket").is_enabled()
    assert button, "отсутствует button"

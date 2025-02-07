from playwright.sync_api import Page
from pages.main_page import MainPage


def test_specialists_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_specialists_link_exists()


def test_specialists_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_specialists_link_functionality()


def test_leave_request_consultation_button_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_leave_request_consultation_button_exists()


def test_leave_request_consultation_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_leave_request_consultation_button_functionality()

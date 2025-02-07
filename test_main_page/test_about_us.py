from playwright.sync_api import Page
from pages.main_page import MainPage


def test_about_us_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_about_us_link_exists()


def test_about_us_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_about_us_link_functionality()


def test_leave_request_cooperation_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_leave_request_cooperation_link_exists()


def test_leave_request_cooperation_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_leave_request_cooperation_link_functionality()

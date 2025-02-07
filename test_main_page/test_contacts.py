from playwright.sync_api import Page
from pages.main_page import MainPage


def test_contacts_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_contacts_link_exists()


def test_contacts_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_contacts_link_functionality()


def test_phone_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_phone_link_exists()


def test_phone_link_href(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_phone_link_href()


def test_email_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_email_link_exists()


def test_email_link_href(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_email_link_href()


def test_telegram_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_telegram_link_exists()


def test_telegram_link_href(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_telegram_link_href()


def test_success_request_popup_button_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_success_request_popup_button_exists()


def test_success_request_popup_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_success_request_popup_functionality()


def test_error_request_popup_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_error_request_popup_functionality()

from playwright.sync_api import Page
from pages.main_page import MainPage


def test_services_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_services_link_exists()


def test_services_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_services_link_functionality()


def test_more_details_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_more_details_link_exists()


def test_more_details_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_more_details_link_functionality()

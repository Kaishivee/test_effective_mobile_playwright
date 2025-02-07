from playwright.sync_api import Page
from pages.main_page import MainPage


def test_title(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_title()


def test_main_page_top_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_main_top_link_exists()


def test_main_page_top_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_main_top_link_functionality()


def test_main_bottom_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_main_bottom_link_exists()


def test_main_page_bottom_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_main_bottom_link_functionality()

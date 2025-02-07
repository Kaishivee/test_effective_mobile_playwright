from playwright.sync_api import Page
from pages.main_page import MainPage


def test_cases_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_cases_link_exists()


def test_cases_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_cases_link_functionality()


def test_more_info_button_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_more_info_button_exists()


def test_more_info_popup_open(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_more_info_popup_open()


def test_more_info_popup_close(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_more_info_popup_close()


def test_carousel_cases_big_buttons_exist(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_big_buttons_exist()


def test_carousel_cases_next_big_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_next_big_button_functionality()


def test_carousel_cases_prev_big_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_prev_big_button_functionality()


def test_carousel_cases_small_buttons_exist(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_small_buttons_exist()


def test_carousel_cases_slide_1_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_slide_1_small_button_functionality()


def test_carousel_cases_slide_2_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_slide_2_small_button_functionality()


def test_carousel_cases_slide_3_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_cases_slide_3_small_button_functionality()

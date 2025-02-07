from playwright.sync_api import Page
from pages.main_page import MainPage


def test_reviews_link_exists(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_reviews_link_exists()


def test_reviews_link_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_reviews_link_functionality()


def test_carousel_reviews_big_buttons_exist(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_big_buttons_exist()


def test_carousel_reviews_big_next_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_big_next_button_functionality()


def test_carousel_reviews_big_prev_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_big_prev_button_functionality()


def test_carousel_reviews_small_buttons_exist(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_small_buttons_exist()


def test_carousel_reviews_slide_1_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_slide_1_small_button_functionality()


def test_carousel_reviews_slide_2_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_slide_2_small_button_functionality()


def test_carousel_reviews_slide_3_small_button_functionality(page: Page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.check_carousel_reviews_slide_3_small_button_functionality()

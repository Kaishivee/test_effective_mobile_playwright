import re
from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://effective-mobile.ru/")

    def check_title(self):
        expect(self.page).to_have_title(re.compile('Effective Mobile'))

    def check_main_top_link_exists(self):
        # Проверяем, что ссылка "Effective Mobile" есть на странице
        main_link = self.page.locator("#rec573054532").get_by_role("link", name="Effective Mobile")
        expect(main_link).to_be_visible()

    def check_main_top_link_functionality(self):
        # Проверяем, что ссылка "Effective Mobile" работает
        main_link = self.page.locator("#rec573054532").get_by_role("link", name="Effective Mobile")
        expect(main_link).to_have_attribute("href", "#main")
        main_section = self.page.locator("#rec571993583")
        main_link.click()
        expect(main_section).to_be_visible()

    def check_main_bottom_link_exists(self):
        # Проверяем, что ссылка "Effective Mobile" внизу страницы есть на странице
        main_link = self.page.locator("#rec572471347").get_by_role("link", name="Effective Mobile")
        expect(main_link).to_be_visible()

    def check_main_bottom_link_functionality(self):
        # Проверяем, что ссылка "Effective Mobile" внизу страницы работает
        main_link = self.page.locator("#rec572471347").get_by_role("link", name="Effective Mobile")
        expect(main_link).to_have_attribute("href", "#main")
        main_section = self.page.locator("#rec571993583")
        main_link.click()
        expect(main_section).to_be_visible()

    def check_about_us_link_exists(self):
        # Проверяем, что ссылка "О нас" есть на странице
        about_us_link = self.page.get_by_role("link", name="[ О нас ]")
        expect(about_us_link).to_be_visible()

    def check_about_us_link_functionality(self):
        # Проверяем, что ссылка "О нас" работает
        about_us_link = self.page.get_by_role("link", name="[ О нас ]")
        expect(about_us_link).to_have_attribute("href", "#about")
        about_us_section = self.page.locator("#rec572359627")
        about_us_link.click()
        expect(about_us_section).to_be_visible()

    def check_leave_request_cooperation_link_exists(self):
        # Проверяем, что ссылка "Оставить заявку на сотрудничество" есть на странице
        cooperation_button = self.page.locator("#sbs-572374517-1680509731311").get_by_role("link")
        expect(cooperation_button).to_be_visible()

    def check_leave_request_cooperation_link_functionality(self):
        # Проверяем, что кнопка "Оставить заявку на сотрудничество" работает
        cooperation_button = self.page.locator("#sbs-572374517-1680509731311").get_by_role("link")
        contacts_section = self.page.locator("#rec572455122")
        cooperation_button.click()
        expect(contacts_section).to_be_visible()

    def check_cases_link_exists(self):
        # Проверяем, что ссылка "Проекты" есть на странице
        cases_link = self.page.get_by_role("link", name="[ Проекты ]")
        expect(cases_link).to_be_visible()

    def check_cases_link_functionality(self):
        # Проверяем, что ссылка "Проекты" работает
        cases_link = self.page.get_by_role("link", name="[ Проекты ]")
        expect(cases_link).to_have_attribute("href", "#cases")
        cases_section = self.page.locator("#rec572838727")
        cases_link.click()
        expect(cases_section).to_be_visible()

    def check_more_info_button_exists(self):
        # Проверяем, что кнопка "Подробнее" есть на странице
        more_info_button = self.page.get_by_role("button", name="Подробнее")
        expect(more_info_button).to_be_visible()

    def check_more_info_popup_open(self):
        # Проверяем, что попап открывается при нажатии на кнопку "Подробнее"
        more_info_button = self.page.get_by_role("button", name="Подробнее")
        more_info_button.click()
        close_button = self.page.get_by_role("button", name="Закрыть диалоговое окно")
        expect(close_button).to_be_visible()  # Проверяем, что кнопка закрытия видима (попап открыт)

    def check_more_info_popup_close(self):
        # Проверяем, что попап закрывается при нажатии на кнопку "Закрыть диалоговое окно"
        more_info_button = self.page.get_by_role("button", name="Подробнее")
        more_info_button.click()
        close_button = self.page.get_by_role("button", name="Закрыть диалоговое окно")
        close_button.click()
        expect(close_button).not_to_be_visible()  # Проверяем, что кнопка закрытия больше не видима (попап закрыт)

    def check_carousel_cases_big_buttons_exist(self):
        # Проверяем, что кнопки "Следующий слайд" и "Предыдущий слайд" есть на странице
        next_button = self.page.locator("#rec572838727").get_by_role("button", name="Следующий слайд")
        prev_button = self.page.locator("#rec572838727").get_by_role("button", name="Предыдущий слайд")
        expect(next_button).to_be_visible()
        expect(prev_button).to_be_visible()

    def check_carousel_cases_next_big_button_functionality(self):
        # Проверяем, что кнопка "Следующий слайд" работает
        next_button = self.page.locator("#rec572838727").get_by_role("button", name="Следующий слайд")
        next_button.click()

    def check_carousel_cases_prev_big_button_functionality(self):
        # Проверяем, что кнопка "Предыдущий слайд" работает
        prev_button = self.page.locator("#rec572838727").get_by_role("button", name="Предыдущий слайд")
        prev_button.click()

    def check_carousel_cases_small_buttons_exist(self):
        # Проверяем, что кнопки перехода к слайдам 1, 2 и 3 есть на странице
        slide_1_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 1")
        slide_2_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 2")
        slide_3_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 3")
        expect(slide_1_button).to_be_visible()
        expect(slide_2_button).to_be_visible()
        expect(slide_3_button).to_be_visible()

    def check_carousel_cases_slide_1_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 1" работает
        slide_1_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 1")
        slide_1_button.click()

    def check_carousel_cases_slide_2_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 2" работает
        slide_2_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 2")
        slide_2_button.click()

    def check_carousel_cases_slide_3_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 3" работает
        slide_3_button = self.page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 3")
        slide_3_button.click()

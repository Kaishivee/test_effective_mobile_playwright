import re
from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page

        # Локаторы для элементов страницы
        self.main_link_top = page.locator("#rec573054532").get_by_role("link", name="Effective Mobile")
        self.main_link_bottom = page.locator("#rec572471347").get_by_role("link", name="Effective Mobile")

        self.about_us_link = page.get_by_role("link", name="[ О нас ]")
        self.cooperation_button = page.locator("#sbs-572374517-1680509731311").get_by_role("link")

        self.cases_link = page.get_by_role("link", name="[ Проекты ]")
        self.more_info_button = page.get_by_role("button", name="Подробнее")
        self.close_popup_button = page.get_by_role("button", name="Закрыть диалоговое окно")
        self.next_slide_button = page.locator("#rec572838727").get_by_role("button", name="Следующий слайд")
        self.prev_slide_button = page.locator("#rec572838727").get_by_role("button", name="Предыдущий слайд")
        self.slide_1_button = page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 1")
        self.slide_2_button = page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 2")
        self.slide_3_button = page.locator("#rec572838727").get_by_role("button", name="Перейти к слайду 3")

        self.contacts_link = page.get_by_role("link", name="[ Контакты ]")
        self.phone_link = page.locator('a[href="tel:+79639937557"]')
        self.email_link = page.locator('a[href="mailto:dariia.krasnikova@effectivemobile.ru"]')
        self.telegram_link = page.locator('a[href="https://t.me/krasnikova_d"]')
        self.submit_button = page.get_by_role("button", name="Отправить")
        self.success_popup = self.page.locator('#tildaformsuccesspopuptext')
        self.error_popup = self.page.locator('#tilda-popup-for-error')

        self.reviews_link = page.get_by_role("link", name="[ Отзывы ]")
        self.reviews_slider = page.get_by_label("Слайдер")
        self.reviews_next_button = self.reviews_slider.get_by_role("button", name="Следующий слайд")
        self.reviews_prev_button = self.reviews_slider.get_by_role("button", name="Предыдущий слайд")
        self.reviews_slide_1_button = self.reviews_slider.get_by_role("button", name="Перейти к слайду 1")
        self.reviews_slide_2_button = self.reviews_slider.get_by_role("button", name="Перейти к слайду 2")
        self.reviews_slide_3_button = self.reviews_slider.get_by_role("button", name="Перейти к слайду 3")

        self.services_link = page.get_by_role("link", name="[ Услуги ]")
        self.more_details_button = page.get_by_role("link", name='Подробнее')

        self.specialists_button = page.get_by_role("link", name='Выбрать специалиста')
        self.consultation_button = page.locator("#sbs-572441941-1680515472080").get_by_role("button")
        # self.close_button = self.page.get_by_role("button", name="Закрыть диалоговое окно")


        # Локаторы для секций страницы
        self.main_section = page.locator("#rec571993583")
        self.about_us_section = page.locator("#rec572359627")
        self.contacts_section = page.locator("#rec572455122")
        self.cases_section = page.locator("#rec572838727")
        self.contacts_section = page.locator("#rec572455122")
        self.reviews_section = page.locator("#rec699930013")
        self.services_section = page.locator("#rec572392832")


    def goto(self):
        self.page.goto("https://effective-mobile.ru/")

    def check_title(self):
        expect(self.page).to_have_title(re.compile('Effective Mobile'))

    def check_main_top_link_exists(self):
        # Проверяем, что ссылка "Effective Mobile" есть на странице
        expect(self.main_link_top).to_be_visible()

    def check_main_top_link_functionality(self):
        # Проверяем, что ссылка "Effective Mobile" работает
        expect(self.main_link_top).to_have_attribute("href", "#main")
        self.main_link_top.click()
        expect(self.main_section).to_be_visible()

    def check_main_bottom_link_exists(self):
        # Проверяем, что ссылка "Effective Mobile" внизу страницы есть на странице
        expect(self.main_link_bottom).to_be_visible()

    def check_main_bottom_link_functionality(self):
        # Проверяем, что ссылка "Effective Mobile" внизу страницы работает
        expect(self.main_link_bottom).to_have_attribute("href", "#main")
        self.main_link_bottom.click()
        expect(self.main_section).to_be_visible()

    def check_about_us_link_exists(self):
        # Проверяем, что ссылка "О нас" есть на странице
        expect(self.about_us_link).to_be_visible()

    def check_about_us_link_functionality(self):
        # Проверяем, что ссылка "О нас" работает
        expect(self.about_us_link).to_have_attribute("href", "#about")
        self.about_us_link.click()
        expect(self.about_us_section).to_be_visible()

    def check_leave_request_cooperation_link_exists(self):
        # Проверяем, что ссылка "Оставить заявку на сотрудничество" есть на странице
        expect(self.cooperation_button).to_be_visible()

    def check_leave_request_cooperation_link_functionality(self):
        # Проверяем, что кнопка "Оставить заявку на сотрудничество" работает
        self.cooperation_button.click()
        expect(self.contacts_section).to_be_visible()

    def check_cases_link_exists(self):
        # Проверяем, что ссылка "Проекты" есть на странице
        expect(self.cases_link).to_be_visible()

    def check_cases_link_functionality(self):
        # Проверяем, что ссылка "Проекты" работает
        expect(self.cases_link).to_have_attribute("href", "#cases")
        self.cases_link.click()
        expect(self.cases_section).to_be_visible()

    def check_more_info_button_exists(self):
        # Проверяем, что кнопка "Подробнее" есть на странице
        expect(self.more_info_button).to_be_visible()

    def check_more_info_popup_open(self):
        # Проверяем, что попап открывается при нажатии на кнопку "Подробнее"
        self.more_info_button.click()
        expect(self.close_popup_button).to_be_visible()  # Проверяем, что кнопка закрытия видима (попап открыт)

    def check_more_info_popup_close(self):
        # Проверяем, что попап закрывается при нажатии на кнопку "Закрыть диалоговое окно"
        self.more_info_button.click()
        self.close_popup_button.click()
        expect(self.close_popup_button).not_to_be_visible()  # Проверяем, что кнопка закрытия больше не видима (попап закрыт)

    def check_carousel_cases_big_buttons_exist(self):
        # Проверяем, что кнопки "Следующий слайд" и "Предыдущий слайд" есть на странице
        expect(self.next_slide_button).to_be_visible()
        expect(self.prev_slide_button).to_be_visible()

    def check_carousel_cases_next_big_button_functionality(self):
        # Проверяем, что кнопка "Следующий слайд" работает
        self.next_slide_button.click()

    def check_carousel_cases_prev_big_button_functionality(self):
        # Проверяем, что кнопка "Предыдущий слайд" работает
        self.prev_slide_button.click()

    def check_carousel_cases_small_buttons_exist(self):
        # Проверяем, что кнопки перехода к слайдам 1, 2 и 3 есть на странице
        expect(self.slide_1_button).to_be_visible()
        expect(self.slide_2_button).to_be_visible()
        expect(self.slide_3_button).to_be_visible()

    def check_carousel_cases_slide_1_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 1" работает
        self.slide_1_button.click()

    def check_carousel_cases_slide_2_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 2" работает
        self.slide_2_button.click()

    def check_carousel_cases_slide_3_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 3" работает
        self.slide_3_button.click()

    def check_contacts_link_exists(self):
        # Проверяем, что ссылка "Контакты" есть на странице
        expect(self.contacts_link).to_be_visible()

    def check_contacts_link_functionality(self):
        # Проверяем, что ссылка "Контакты" работает
        expect(self.contacts_link).to_have_attribute("href", "#contacts")
        self.contacts_link.click()
        expect(self.contacts_section).to_be_visible()

    def check_phone_link_exists(self):
        # Проверяем, что ссылка с телефонным номером есть на странице
        expect(self.phone_link).to_be_visible()

    def check_phone_link_href(self):
        # Проверяем, что ссылка с телефонным номером имеет правильный атрибут href
        expect(self.phone_link).to_have_attribute("href", "tel:+79639937557")

    def check_email_link_exists(self):
        # Проверяем, что ссылка с email есть на странице
        expect(self.email_link).to_be_visible()

    def check_email_link_href(self):
        # Проверяем, что ссылка с email имеет правильный атрибут href
        expect(self.email_link).to_have_attribute("href", "mailto:dariia.krasnikova@effectivemobile.ru")

    def check_telegram_link_exists(self):
        # Проверяем, что ссылка на Telegram есть на странице
        expect(self.telegram_link).to_be_visible()

    def check_telegram_link_href(self):
        # Проверяем, что ссылка на Telegram имеет правильный атрибут href
        expect(self.telegram_link).to_have_attribute("href", "https://t.me/krasnikova_d")

    def check_success_request_popup_button_exists(self):
        # Проверяем, что кнопка "Отправить" есть на странице
        expect(self.submit_button).to_be_visible()

    def check_success_request_popup_functionality(self):
        # Проверяем функциональность формы успешной отправки
        self.page.locator("#nm-1531306243545").fill("Сергей")
        self.page.locator("#input_1531306540094").fill("(999) 999-99-99")
        self.page.locator("#in-1680516575724").fill("test_telegram")
        self.page.locator("#ta-1680516600617").fill("Расскажите о своем проекте")
        self.submit_button.click()
        expect(self.success_popup).to_be_visible() # может не работать из-за CAPTCHA :)

    def check_error_request_popup_functionality(self):
        # Проверяем функциональность формы с ошибкой
        self.submit_button.click()
        expect(self.error_popup).to_be_visible()

    def check_reviews_link_exists(self):
        # Проверяем, что ссылка "Отзывы" есть на страниц
        expect(self.reviews_link).to_be_visible()

    def check_reviews_link_functionality(self):
        # Проверяем, что ссылка "Отзывы" работает
        expect(self.reviews_link).to_have_attribute("href", "#Reviews")
        self.reviews_link.click()
        expect(self.reviews_section).to_be_visible()

    def check_carousel_reviews_big_buttons_exist(self):
        # Проверяем, что кнопки "Следующий слайд" и "Предыдущий слайд" есть на странице
        expect(self.reviews_next_button).to_be_visible()
        expect(self.reviews_prev_button).to_be_visible()

    def check_carousel_reviews_big_next_button_functionality(self):
        # Проверяем, что кнопка "Следующий слайд" работает
        self.reviews_next_button.click()

    def check_carousel_reviews_big_prev_button_functionality(self):
        # Проверяем, что кнопка "Предыдущий слайд" работает
        self.reviews_prev_button.click()

    def check_carousel_reviews_small_buttons_exist(self):
        # Проверяем, что кнопки перехода к слайдам 1, 2 и 3 есть на странице
        expect(self.reviews_slide_1_button).to_be_visible()
        expect(self.reviews_slide_2_button).to_be_visible()
        expect(self.reviews_slide_3_button).to_be_visible()

    def check_carousel_reviews_slide_1_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 1" работает
        self.reviews_slide_1_button.click()

    def check_carousel_reviews_slide_2_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 2" работает
        self.reviews_slide_2_button.click()

    def check_carousel_reviews_slide_3_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 3" работает
        self.reviews_slide_3_button.click()

    def check_services_link_exists(self):
        # Проверяем, что ссылка "Услуги" есть на странице
        expect(self.services_link).to_be_visible()

    def check_services_link_functionality(self):
        # Проверяем, что ссылка "Услуги" работает
        expect(self.services_link).to_have_attribute("href", "#moreinfo")
        self.services_link.click()
        expect(self.services_section).to_be_visible()

    def check_more_details_link_exists(self):
        # Проверяем, что ссылка "Подробнее" есть на странице
        expect(self.more_details_button).to_be_visible()

    def check_more_details_link_functionality(self):
        expect(self.more_details_button).to_have_attribute("href", "#moreinfo")
        self.more_details_button.click()
        expect(self.services_section).to_be_visible()

    def check_specialists_link_exists(self):
        # Проверяем, что ссылка "Выбрать специалиста" есть на странице
        expect(self.specialists_button).to_be_visible()

    def check_specialists_link_functionality(self):
        # Проверяем, что ссылка "Выбрать специалиста" работает
        expect(self.specialists_button).to_have_attribute("href", "#specialists")
        self.specialists_button.click()
        expect(self.contacts_section).to_be_visible()

    def check_leave_request_consultation_button_exists(self):
        # Проверяем, что кнопка "Оставить заявку на консультацию" есть на странице
        expect(self.consultation_button).to_be_visible()

    def check_leave_request_consultation_button_functionality(self):
        # Проверяем, что кнопка "Оставить заявку на консультацию" работает
        self.consultation_button.click()
        expect(self.close_popup_button).to_be_visible()  # Проверяем, что кнопка закрытия видима (попап открыт)
        self.close_popup_button.click()
        expect(self.close_popup_button).not_to_be_visible()

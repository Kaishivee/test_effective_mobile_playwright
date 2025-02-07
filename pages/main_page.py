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

    def check_contacts_link_exists(self):
        # Проверяем, что ссылка "Контакты" есть на странице
        contacts_link = self.page.get_by_role("link", name="[ Контакты ]")
        expect(contacts_link).to_be_visible()

    def check_contacts_link_functionality(self):
        # Проверяем, что ссылка "Контакты" работает
        contacts_link = self.page.get_by_role("link", name="[ Контакты ]")
        expect(contacts_link).to_have_attribute("href", "#contacts")
        contacts_section = self.page.locator("#rec572455122")
        contacts_link.click()
        expect(contacts_section).to_be_visible()

    def check_phone_link_exists(self):
        # Проверяем, что ссылка с телефонным номером есть на странице
        phone_number = self.page.locator('a[href="tel:+79639937557"]')
        expect(phone_number).to_be_visible()

    def check_phone_link_href(self):
        # Проверяем, что ссылка с телефонным номером имеет правильный атрибут href
        phone_number = self.page.locator('a[href="tel:+79639937557"]')
        expect(phone_number).to_have_attribute("href", "tel:+79639937557")

    def check_email_link_exists(self):
        # Проверяем, что ссылка с email есть на странице
        email_link = self.page.locator('a[href="mailto:dariia.krasnikova@effectivemobile.ru"]')
        expect(email_link).to_be_visible()

    def check_email_link_href(self):
        # Проверяем, что ссылка с email имеет правильный атрибут href
        email_link = self.page.locator('a[href="mailto:dariia.krasnikova@effectivemobile.ru"]')
        expect(email_link).to_have_attribute("href", "mailto:dariia.krasnikova@effectivemobile.ru")

    def check_telegram_link_exists(self):
        # Проверяем, что ссылка на Telegram есть на странице
        telegram_link = self.page.locator('a[href="https://t.me/krasnikova_d"]')
        expect(telegram_link).to_be_visible()

    def check_telegram_link_href(self):
        # Проверяем, что ссылка на Telegram имеет правильный атрибут href
        telegram_link = self.page.locator('a[href="https://t.me/krasnikova_d"]')
        expect(telegram_link).to_have_attribute("href", "https://t.me/krasnikova_d")

    def check_success_request_popup_button_exists(self):
        # Проверяем, что кнопка "Отправить" есть на странице
        submit_button = self.page.get_by_role("button", name="Отправить")
        expect(submit_button).to_be_visible()

    def check_success_request_popup_functionality(self):
        # Проверяем функциональность формы успешной отправки
        self.page.locator("#nm-1531306243545").fill("Сергей")
        self.page.locator("#input_1531306540094").fill("(999) 999-99-99")
        self.page.locator("#in-1680516575724").fill("test_telegram")
        self.page.locator("#ta-1680516600617").fill("Расскажите о своем проекте")
        self.page.get_by_role("button", name="Отправить").click()
        success_popup = self.page.locator('#tildaformsuccesspopuptext')
        expect(success_popup).to_be_visible()

    def check_error_request_popup_functionality(self):
        # Проверяем функциональность формы с ошибкой
        self.page.get_by_role("button", name="Отправить").click()
        error_popup = self.page.locator('#tilda-popup-for-error')
        expect(error_popup).to_be_visible()

    def check_reviews_link_exists(self):
        # Проверяем, что ссылка "Отзывы" есть на страниц
        reviews_link = self.page.get_by_role("link", name="[ Отзывы ]")
        expect(reviews_link).to_be_visible()

    def check_reviews_link_functionality(self):
        # Проверяем, что ссылка "Отзывы" работает
        reviews_link = self.page.get_by_role("link", name="[ Отзывы ]")
        expect(reviews_link).to_have_attribute("href", "#Reviews")
        reviews_section = self.page.locator("#rec699930013")
        reviews_link.click()
        expect(reviews_section).to_be_visible()

    def check_carousel_reviews_big_buttons_exist(self):
        # Проверяем, что кнопки "Следующий слайд" и "Предыдущий слайд" есть на странице
        next_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Следующий слайд")
        prev_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Предыдущий слайд")
        expect(next_button).to_be_visible()
        expect(prev_button).to_be_visible()

    def check_carousel_reviews_big_next_button_functionality(self):
        # Проверяем, что кнопка "Следующий слайд" работает
        next_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Следующий слайд")
        next_button.click()

    def check_carousel_reviews_big_prev_button_functionality(self):
        # Проверяем, что кнопка "Предыдущий слайд" работает
        prev_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Предыдущий слайд")
        prev_button.click()

    def check_carousel_reviews_small_buttons_exist(self):
        # Проверяем, что кнопки перехода к слайдам 1, 2 и 3 есть на странице
        slide_1_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 1")
        slide_2_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 2")
        slide_3_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 3")
        expect(slide_1_button).to_be_visible()
        expect(slide_2_button).to_be_visible()
        expect(slide_3_button).to_be_visible()

    def check_carousel_reviews_slide_1_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 1" работает
        slide_1_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 1")
        slide_1_button.click()

    def check_carousel_reviews_slide_2_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 2" работает
        slide_2_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 2")
        slide_2_button.click()

    def check_carousel_reviews_slide_3_small_button_functionality(self):
        # Проверяем, что кнопка "Перейти к слайду 3" работает
        slide_3_button = self.page.get_by_label("Слайдер").get_by_role("button", name="Перейти к слайду 3")
        slide_3_button.click()

    def check_services_link_exists(self):
        # Проверяем, что ссылка "Услуги" есть на странице
        services_link = self.page.get_by_role("link", name="[ Услуги ]")
        expect(services_link).to_be_visible()

    def check_services_link_functionality(self):
        # Проверяем, что ссылка "Услуги" работает
        services_link = self.page.get_by_role("link", name="[ Услуги ]")
        expect(services_link).to_have_attribute("href", "#moreinfo")
        services_section = self.page.locator("#rec572392832")
        services_link.click()
        expect(services_section).to_be_visible()

    def check_more_details_link_exists(self):
        more_details_button = self.page.get_by_role("link", name='Подробнее')
        expect(more_details_button).to_be_visible()

    def check_more_details_link_functionality(self):
        more_details_button = self.page.get_by_role("link", name='Подробнее')
        expect(more_details_button).to_have_attribute("href", "#moreinfo")
        more_details_section = self.page.locator("#rec572392832")
        more_details_button.click()
        expect(more_details_section).to_be_visible()

    def check_specialists_link_exists(self):
        # Проверяем, что ссылка "Выбрать специалиста" есть на странице
        specialists_button = self.page.get_by_role("link", name='Выбрать специалиста')
        expect(specialists_button).to_be_visible()

    def check_specialists_link_functionality(self):
        # Проверяем, что ссылка "Выбрать специалиста" работает
        specialists_button = self.page.get_by_role("link", name='Выбрать специалиста')
        expect(specialists_button).to_have_attribute("href", "#specialists")
        contacts_section = self.page.locator("#rec660927810")
        specialists_button.click()
        expect(contacts_section).to_be_visible()

    def check_leave_request_consultation_button_exists(self):
        # Проверяем, что кнопка "Оставить заявку на консультацию" есть на странице
        consultation_button = self.page.locator("#sbs-572441941-1680515472080").get_by_role("button")
        expect(consultation_button).to_be_visible()

    def check_leave_request_consultation_button_functionality(self):
        # Проверяем, что кнопка "Оставить заявку на консультацию" работает
        consultation_button = self.page.locator("#sbs-572441941-1680515472080").get_by_role("button")
        consultation_button.click()
        close_button = self.page.get_by_role("button", name="Закрыть диалоговое окно")
        expect(close_button).to_be_visible()  # Проверяем, что кнопка закрытия видима (попап открыт)
        close_button.click()
        expect(close_button).not_to_be_visible()

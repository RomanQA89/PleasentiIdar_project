import time
import pytest
import selenium
from selenium.webdriver import Keys
from pages.locators import HeaderNavigation, MainPage, FooterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestsPositiveUI:
    """ Позитивные тесты сайта https://dima731515.github.io/hakaton/html/# """

    @pytest.mark.header
    def test_header_check(self, web_browser):
        """Проверка наличия и кликабельности кнопок соц. сетей в хедере сайта."""

        page = HeaderNavigation(web_browser)

        time.sleep(3)

        page.btn_youtube.click()

        web_browser.implicitly_wait(10)

        page.btn_twitch.click()

        web_browser.implicitly_wait(10)

        page.btn_tel.click()

        web_browser.implicitly_wait(10)

        page.btn_inst.click()

        web_browser.implicitly_wait(10)

        page.btn_twit.click()

        web_browser.implicitly_wait(10)

        page.btn_vk.click()

        web_browser.implicitly_wait(10)

        assert page.btn_youtube.is_presented() and page.btn_youtube.is_clickable()
        assert page.btn_twitch.is_presented() and page.btn_twitch.is_clickable()
        assert page.btn_tel.is_presented() and page.btn_tel.is_clickable()
        assert page.btn_twit.is_presented() and page.btn_twit.is_clickable()
        assert page.btn_inst.is_presented() and page.btn_inst.is_clickable()
        assert page.btn_vk.is_presented() and page.btn_vk.is_clickable()

    @pytest.mark.main
    def test_main_check(self, web_browser):
        """Проверка наличия и кликабельности кнопок в разделе Main сайта."""

        page = MainPage(web_browser)

        time.sleep(3)

        page.btn_watch_you.click()

        web_browser.implicitly_wait(10)

        assert page.btn_watch_you.is_presented() and page.btn_watch_you.is_clickable()
        assert page.btn_get_pr.is_presented() and page.btn_get_pr.is_clickable()
        assert page.btn_chat_bot.is_presented() and page.btn_chat_bot.is_clickable()

    @pytest.mark.main
    def test_logo_and_info_check(self, web_browser):
        """Проверка наличия логотипа и информации об авторе сайта."""

        page = MainPage(web_browser)

        time.sleep(3)

        assert page.logo.is_presented()
        assert page.info1.is_presented() and page.info2.is_presented()

    @pytest.mark.main
    def test_merch_check(self, web_browser):
        """Проверка наличия и кликабельности кнопок в разделе "Мерч" сайта."""

        page = MainPage(web_browser)

        time.sleep(10)

        assert page.thing1.is_presented() and page.thing1.is_clickable()
        assert page.thing2.is_presented() and page.thing2.is_clickable()
        assert page.thing3.is_presented() and page.thing3.is_clickable()
        assert page.thing4.is_presented() and page.thing4.is_clickable()
        assert page.thing5.is_presented() and page.thing5.is_clickable()
        assert page.btn_all_coll.is_presented() and page.btn_all_coll.is_clickable()

    @pytest.mark.footer
    def test_footer_check(self, web_browser):
        """Проверка наличия и кликабельности кнопок в разделе Footer сайта."""

        page = FooterPage(web_browser)

        time.sleep(3)

        assert page.btn_youtube.is_presented() and page.btn_youtube.is_clickable()
        assert page.btn_tel.is_presented() and page.btn_tel.is_clickable()
        assert page.btn_inst.is_presented() and page.btn_inst.is_clickable()
        assert page.btn_vk.is_presented() and page.btn_vk.is_clickable()


# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exe tests\test_ui_positive.py
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exe tests\test_ui_positive.py -v -m "header"
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exe tests\test_ui_positive.py -v -m "main"
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exe tests\test_ui_positive.py -v -m "footer"
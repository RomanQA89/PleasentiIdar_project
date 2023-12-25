from pages.base import WebPage
from pages.elements import WebElement


class HeaderNavigation(WebPage):
    """Локаторы для элементов Header сайта."""

    def __init__(self, web_driver, url=''):
        url = 'https://dima731515.github.io/hakaton/html/#'
        super().__init__(web_driver, url)

    # Кнопка Youtube
    btn_youtube = WebElement(xpath='//*[@src="../images/icons-header/v.2/Youtube.svg"]')

    # Кнопка Twitch
    btn_twitch = WebElement(xpath='//*[@src="../images/icons-header/v.2/Twitch.svg"]')

    # Кнопка Telegram
    btn_tel = WebElement(xpath='//*[@src="../images/icons-header/v.2/Telegram.svg"]')

    # Кнопка Instagram
    btn_inst = WebElement(xpath='//*[@src="../images/icons-header/v.2/Instagram.svg"]')

    # Кнопка Twitter
    btn_twit = WebElement(xpath='//*[@src="../images/icons-header/v.2/Twitter.svg"]')

    # Кнопка Vkontakte
    btn_vk = WebElement(xpath='//*[@src="../images/icons-header/v.2/VK.svg"]')


class MainPage(WebPage):
    """Локаторы для элементов раздела Main сайта."""

    def __init__(self, web_driver, url=''):
        url = 'https://dima731515.github.io/hakaton/html/#'
        super().__init__(web_driver, url)

    # Кнопка "СМОТРЕТЬ НА YOUTUBE"
    btn_watch_you = WebElement(xpath='/html/body/main/section[1]/a/div/p')

    # Кнопка "ПОЛУЧИТЬ ПРЕДСКАЗАНИЕ"
    btn_get_pr = WebElement(xpath='/html/body/main/section[5]/div[2]/div[1]/a/div/p')

    # Кнопка "ПОЗНАКОМИТЬСЯ С ЧАТ-БОТОМ"
    btn_chat_bot = WebElement(xpath='/html/body/main/section[6]/a/div/p')

    # Логотип
    logo = WebElement(xpath='/html/body/main/section[1]/div[2]/div/img')

    # Информация об авторе
    info1 = WebElement(xpath='/html/body/main/section[1]/div[2]/p')
    info2 = WebElement(xpath='//*[@class="about__text_first"]')

    # Кнопки "Купить" у товаров
    thing1 = WebElement(xpath='/html/body/main/section[7]/diav/div/div[1]/a/p')
    thing2 = WebElement(xpath='/html/body/main/section[7]/diav/div/div[2]/a/p')
    thing3 = WebElement(xpath='/html/body/main/section[7]/diav/div/div[3]/a/p')
    thing4 = WebElement(xpath='/html/body/main/section[7]/diav/div/div[4]/a/p')
    thing5 = WebElement(xpath='/html/body/main/section[7]/diav/div/div[5]/a/p')

    # Кнопка "ПОСМОТРЕТЬ ВСЮ КОЛЛЕКЦИЮ"
    btn_all_coll = WebElement(xpath='//*[contains(text(), "ПОСМОТРЕТЬ ВСЮ КОЛЛЕКЦИЮ")]')


class FooterPage(WebPage):
    """Локаторы для элементов раздела Footer сайта."""

    def __init__(self, web_driver, url=''):
        url = 'https://dima731515.github.io/hakaton/html/#'
        super().__init__(web_driver, url)

    # Кнопка Youtube
    btn_youtube = WebElement(xpath='/html/body/footer/div[2]/a[1]/p')

    # Кнопка Telegram
    btn_tel = WebElement(xpath='/html/body/footer/div[2]/a[2]/p')

    # Кнопка Instagram
    btn_inst = WebElement(xpath='/html/body/footer/div[2]/a[3]/p')

    # Кнопка Vkontakte
    btn_vk = WebElement(xpath='/html/body/footer/div[2]/a[4]/p')

    # Кнопка "СОТРУДНИЧЕСТВО"
    btn_collab = WebElement(xpath='//*[contains(text(), "СОТРУДНИЧЕСТВО")]')

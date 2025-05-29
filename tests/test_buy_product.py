import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.cart_popup_component import CartPopupComponent
from components.header_component import HeaderComponent
from pages.cart_page import CartPage
from pages.catalog_category_subwoofer import CatalogCategorySubwoofer
from pages.login_page import LoginPage
from pages.order_page import OrderPage


def test_buy_random_subwoofer():
    options = webdriver.ChromeOptions()  # возможность добавлять дополнительные настройки для браузера
    options.add_experimental_option('detach', True)  # опция, которая не позволит нашему браузеру закрыться
    options.add_argument("--guest")  # опция, которая отключает оповещения от Браузера, с просьбой смены пароля
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:/Users/LISTER/PycharmProjects/FavoritProject/utilities/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    print("Start Test")

    login = LoginPage(driver)
    login.authorization() #Авторизация на сайте

    header = HeaderComponent(driver)
    header.transition_subwoofer_category() #Переход ко списку товаров из категории Сабуферы

    catalog_subwoofer = CatalogCategorySubwoofer(driver)
    catalog_subwoofer.add_to_cart_random_item() #Добавляем в корзину товар

    cart_popup = CartPopupComponent(driver)
    cart_popup.close_cart_popup() #Закрываем поп-ап который появляется при добавлении товара в корзину

    first_product_title = catalog_subwoofer.get_first_product_title().text
    first_product_price = catalog_subwoofer.get_first_product_price().text

    header.open_cart() #Открываем корзину

    cart_page = CartPage(driver)
    cart_page.ordering() #Оформляем заказ на странице корзины

    order_page = OrderPage(driver)
    product_title = order_page.get_product_title()
    product_price = order_page.get_product_price()

    order_page.assert_word(product_title, first_product_title) #Проверяем соответствие названия товара
    order_page.assert_word(product_price, first_product_price) #Проверяем соответствие стоимости товара
    order_page.create_order() #Заполняем данные и создаем заказ


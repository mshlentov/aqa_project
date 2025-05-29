import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random  # Импортируем модуль для работы со случайными числами

from base.base_class import Base

class CatalogCategorySubwoofer(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    subcategory = "//div[@class='subcollections-grid__item']"
    filter_availability = "//label[@for='filter-item-only_available']"
    filter_material_ferrit = "//label[@for='filter-item-60407734']"
    items = "//form[@action='/cart_items']"
    add_to_cart_button = "//div[@class='product-card__add']"
    first_product_title = "//a[@class='product-card__title'][1]"
    first_product_price = "//span[@class='product-card__price'][1]"


    #Getters

    def get_all_subcategory(self):
        # 1. Ожидаем появления хотя бы одного элемента
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.subcategory)))

        # 2. Находим ВСЕ элементы по локатору
        return self.driver.find_elements(By.XPATH, self.subcategory)

    def get_first_subcategory(self):
        return self.get_all_subcategory()[0]

    def get_filter_availability(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_availability)))

    def get_filter_material_ferrit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_material_ferrit)))

    def get_all_items(self):
        """Возвращает список всех элементов товаров"""
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.items)))
        return self.driver.find_elements(By.XPATH, self.items)

    def get_first_item(self):
        """Возвращает первый товар из списка"""
        return self.get_all_items()[0]

    def get_add_to_cart_button(self, item):
        """Возвращает кнопку 'В корзину' для конкретного товара"""
        # Ищем кнопку внутри элемента товара
        return self.get_first_item().find_element(By.XPATH, self.add_to_cart_button)

    def get_first_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product_title)))

    def get_first_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product_price)))


    #Actions

    def click_first_subcategory(self):
        self.get_first_subcategory().click()
        print("Click Subwoofer First Subcategory")

    def click_filter_availability(self):
        # Получаем элемент фильтра
        element = self.get_filter_availability()

        # Скроллим к элементу с центрированием
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element
        )

        # Кликаем по элементу
        element.click()

    def click_filter_material_ferrit(self):
        self.get_filter_material_ferrit().click()
        print("Click Filter Material Ferrit")

    def click_add_to_cart_first_item(self):
        first_item = self.get_first_item()
        ActionChains(self.driver).move_to_element(first_item).perform()
        print("Hovered over first item")

        # Ожидаем появления кнопки
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.add_to_cart_button)))

        # Находим кнопку внутри товара
        add_button = self.get_add_to_cart_button(first_item)

        # Кликаем
        add_button.click()
        print("Click Add To Cart First item")



    #Methods
    def add_to_cart_random_item(self):
        self.click_first_subcategory()
        self.click_filter_material_ferrit()
        self.click_filter_availability()
        self.click_add_to_cart_first_item()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class HeaderComponent(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    main_word = "//h1[@class='section__title']"
    cart_button = "//a[@aria-label='Корзина']"
    catalog_button = "//div[@class='hamburger']"
    catalog_category_subwoofer = "//li[@data-nav-item='10458912']"
    catalog_category_acoustics = "//li[@data-nav-item='10458698']"
    catalog_category_amplifiers = "//li[@data-nav-item='10458943']"

    # Getters

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_category_subwoofer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_category_subwoofer)))

    def get_category_acoustics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_category_acoustics)))

    def get_category_amplifiers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_category_amplifiers)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def hover_catalog_button(self):
        ActionChains(self.driver).move_to_element(self.get_catalog_button()).perform()
        print("Hover Catalog Button")

    def click_category_subwoofer(self):
        self.get_category_subwoofer().click()
        print("Click Category Subwoofer")

    def click_category_acoustics(self):
        self.get_category_acoustics().click()

    def click_category_amplifiers(self):
        self.get_category_amplifiers().click()

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Open Cart")


    # Methods

    def transition_subwoofer_category(self):
        self.hover_catalog_button()
        self.click_category_subwoofer()
        self.assert_word(self.get_main_word(), "Сабвуферы")

    def open_cart(self):
        self.click_cart_button()
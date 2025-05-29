from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    order_button = "//input[@value='Оформить заказ']"


    #Getters

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))


    #Actions

    def click_order_button(self):
        self.get_order_button().click()
        print("Click Order Button")


    #Methods

    def ordering(self):
        self.click_order_button()
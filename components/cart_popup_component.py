from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CartPopupComponent(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    close_button = "//button[@class='fancybox-close-small']"


    # Getters

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_button)))


    # Actions

    def click_close_button(self):
        self.get_close_button().click()
        print("Click Close Button Cart Popup")

    # Methods

    def close_cart_popup(self):
        self.click_close_button()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class LoginPage(Base):

    url = 'https://favoritcaraudio.ru/client_account/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    user_name = "//input[@id='email']"
    password = "//input[@id='password']"
    login_button = "//button[@name='commit']"
    main_word = "//div[@class='client-account__title']"


    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input Login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("+7(927)104-85-86")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "история заказов")

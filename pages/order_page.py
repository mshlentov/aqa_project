import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    create_order_button = "//button[@id='create_order']"
    order_comment = "//textarea[@id='order_comment']"
    payment_method_store = "//label[@for='order_payment_gateway_id_1415753']"
    delivery_radiobutton = "//label[@for='order_delivery_variant_id_3002307']"
    address = "//textarea[@id='shipping_address_address']"
    product_title = "//div[@class='co-basket_item-description']"
    product_price = "//div[@class='co-basket_total-price co-price--current']"
    title_word = "//div[@class='co-title co-title--h2'][1]"



    #Getters

    def get_create_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_order_button)))

    def get_order_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_comment)))

    def get_payment_method_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_store)))

    def get_delivery_radiobutton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_radiobutton)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_title_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))


    #Actions

    def click_create_order_button(self):
        self.get_create_order_button().click()
        print("Click Create Order Button")

    def input_order_comment(self):
        self.get_order_comment().send_keys(f"Тестовый заказ: {datetime.date.today()}")
        print("Input Order Comment")

    def click_payment_method_store(self):
        self.get_payment_method_store().click()
        print("Click Payment Method Store")

    def click_delivery_radiobutton(self):
        self.get_delivery_radiobutton().click()
        print("Click Delivery Radiobutton")

    def input_address(self):
        self.get_address().send_keys("г.Марс, улица Тестовая, д.164, кв.77")
        print("Input Address")


    #Methods

    def create_order(self):
        self.click_delivery_radiobutton()
        self.input_address()
        self.input_order_comment()
        self.click_create_order_button()
        self.assert_word(self.get_title_word(), "Информация о заказе")
        self.get_screenshot()

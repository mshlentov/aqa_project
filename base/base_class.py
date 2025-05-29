import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    # Get Method Current URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    # Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good value word: {value_word} = {result}")

    # Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    # Method Screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f'screenshot-{now_date}.png'
        self.driver.save_screenshot(f'./screen/{name_screenshot}')
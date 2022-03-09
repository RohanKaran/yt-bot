import youtube.constants as const
import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


class YouTube(webdriver.Chrome):
    def __init__(self, drivar_path=webdriver.Chrome(executable_path="chromedriver.exe",
                                                    chrome_options=chrome_options), teardown=False):
        self.driver_path = drivar_path
        self.teardown = teardown
        super(YouTube, self).__init__()
        self.implicitly_wait(25)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


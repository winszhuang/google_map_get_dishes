import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.dish import Dish
import delivers.delivers as delivers


class DishesSpider:

    _thread_local = threading.local()

    @classmethod
    def get_driver(cls, chrome_driver_path):
        if not hasattr(cls._thread_local, "driver"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches",
                                                   ["enable-automation"])
            # chrome_options.add_experimental_option('useAutomationExtension', False)
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument('Referer=https://www.google.com.tw/')
            chrome_options.add_argument(
                'Sec-Ch-Ua="Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"'
            )
            chrome_options.add_argument(
                'Accept-Language=zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7')
            chrome_options.add_argument('Accept-Encoding=gzip, deflate, br')
            chrome_options.add_argument('Sec-Ch-Ua-Platform="Windows"')
            chrome_options.add_argument(
                'Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
            )
            chrome_options.add_argument('Cache-Control=max-age=0')
            chrome_options.add_argument(
                'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
            )

            driver = webdriver.Chrome(chrome_driver_path,
                                      options=chrome_options)
            cls._thread_local.driver = driver
        return cls._thread_local.driver

    def __init__(self, chrome_driver_path):
        self.driver = self.get_driver(chrome_driver_path)

    def find_deliver_link(self):
        foodpandaUrl = self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="foodpanda.com.tw"]')
        if foodpandaUrl is not None:
            return foodpandaUrl.get_attribute("href")

        ubereatsUrl = self.driver.find_element(By.CSS_SELECTOR,
                                               '[aria-label="ubereats.com"]')
        if ubereatsUrl is not None:
            return ubereatsUrl.get_attribute("href")
        return ""

    def scrape_dishes(self, url) -> tuple[list[Dish], Exception]:
        self.driver.get(url)
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[aria-label="預訂"]')), "沒有合作店家")
        except Exception as e:
            return None, e

        if el is None:
            return None, Exception("找不到預訂按鈕")

        # 只有一個合作店家的情況
        url = el.get_attribute("href")
        if url is not None:
            return delivers.get_dishes(url)

        # 超過一個以上的店家的情況
        el.click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[aria-label="選擇服務供應商"]')))
        except Exception as e:
            return None, e

        url = self.find_deliver_link()
        if url == "":
            return None, Exception("找不到該合作店家")

        return delivers.get_dishes(url)

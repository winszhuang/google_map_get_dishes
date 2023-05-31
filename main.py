from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import delivers.delivers as delivers

__path__ = "D:/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(__path__)

# restaurant_url = "https://www.google.com.tw/maps/place/%E5%88%81%E6%B0%91-%E9%85%B8%E8%8F%9C%E9%AD%9A+%E5%B4%87%E5%BE%B7%E5%BA%97/@24.1691613,120.6796219,16.25z/data=!4m5!3m4!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!8m2!3d24.1670957!4d120.6848373?entry=ttu"
restaurant_url = "https://www.google.com.tw/maps/place/%E7%89%A7%E7%A6%BE%E5%A0%82%E5%8F%B0%E4%B8%AD%E5%8C%97%E5%B9%B3%E5%BA%97/@24.1713982,120.6659293,14.75z/data=!4m14!1m7!3m6!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!2z5YiB5rCRLemFuOiPnOmtmiDltIflvrflupc!8m2!3d24.1670963!4d120.6848373!16s%2Fg%2F11qm37nh6j!3m5!1s0x346917901f6b4a5b:0xf507d5c683b79253!8m2!3d24.1713975!4d120.6756103!16s%2Fg%2F11rr2kb7kx?entry=ttu"


def init_chrome_options():
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


def check_deliver(url):
    if url.find("ubereats.com") != -1: return "ubereats"
    if url.find("foodpanda.com") != -1: return "foodpanda"
    return ""


def find_deliver_link():
    foodpandaUrl = driver.find_element(By.CSS_SELECTOR,
                                       '[aria-label="foodpanda.com.tw"]')
    if foodpandaUrl is not None:
        url = foodpandaUrl.get_attribute("href")
        return "foodpanda", url
    ubereatsUrl = driver.find_element(By.CSS_SELECTOR,
                                      '[aria-label="ubereats.com"]')
    if ubereatsUrl is not None:
        url = ubereatsUrl.get_attribute("href")
        return "ubereats", url
    return "", ""


def run(url):
    driver.get(url)
    el = driver.find_element(By.CSS_SELECTOR, '[aria-label="預訂"]')
    if el is None:
        print("找不到該元素哦")
        exit()
    print(el)

    # 只有一個合作店家的情況
    url = el.get_attribute("href")
    if url is not None:
        deliver_name = check_deliver(url)
        dishes_data = delivers.get_dishes(deliver_name, url)
        for dish in dishes_data:
            print("-------")
            dish.print()
        return

    # 超過一個以上的店家的情況
    el.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[aria-label="選擇服務供應商"]')))
    deliver_name, url = find_deliver_link()
    if deliver_name == "":
        print("找不到該合作店家")
        return

    dishes_data = delivers.get_dishes(deliver_name, url)
    for dish in dishes_data:
        print("-------")
        dish.print()
    return


init_chrome_options()
run(restaurant_url)

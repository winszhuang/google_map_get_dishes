from concurrent.futures import ThreadPoolExecutor
import json
from spider.spider import DishesSpider
import tools.wirte_file as wf
import time

driver_path = "D:/chromedriver_win32/chromedriver.exe"

url_list = [
    "https://www.google.com.tw/maps/place/%E5%88%81%E6%B0%91-%E9%85%B8%E8%8F%9C%E9%AD%9A+%E5%B4%87%E5%BE%B7%E5%BA%97/@24.1691613,120.6796219,16.25z/data=!4m5!3m4!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!8m2!3d24.1670957!4d120.6848373?entry=ttu",
    "https://www.google.com.tw/maps/place/%E7%89%A7%E7%A6%BE%E5%A0%82%E5%8F%B0%E4%B8%AD%E5%8C%97%E5%B9%B3%E5%BA%97/@24.1713982,120.6659293,14.75z/data=!4m14!1m7!3m6!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!2z5YiB5rCRLemFuOiPnOmtmiDltIflvrflupc!8m2!3d24.1670963!4d120.6848373!16s%2Fg%2F11qm37nh6j!3m5!1s0x346917901f6b4a5b:0xf507d5c683b79253!8m2!3d24.1713975!4d120.6756103!16s%2Fg%2F11rr2kb7kx?entry=ttu",
    "https://www.google.com.tw/maps/place/%E6%98%8E%E6%B2%BB%E9%AB%98%E7%BA%96%E7%8F%BE%E7%82%92%E9%A4%A8/@24.1714915,120.6741878,19.29z/data=!4m14!1m7!3m6!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!2z5YiB5rCRLemFuOiPnOmtmiDltIflvrflupc!8m2!3d24.1670963!4d120.6848373!16s%2Fg%2F11qm37nh6j!3m5!1s0x346917d0e386d0cd:0x32fdc46ef905da37!8m2!3d24.1715747!4d120.6749243!16s%2Fg%2F1vn_wqgl?entry=ttu",
    "https://www.google.com.tw/maps/place/%E6%9D%8E%E8%A8%98%E8%92%B8%E9%A4%83%E4%B8%96%E5%AE%B6/@24.1715135,120.6740671,19z/data=!4m14!1m7!3m6!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!2z5YiB5rCRLemFuOiPnOmtmiDltIflvrflupc!8m2!3d24.1670963!4d120.6848373!16s%2Fg%2F11qm37nh6j!3m5!1s0x346917d0e1d256fd:0x8eca656e251d86a!8m2!3d24.1714288!4d120.6746994!16s%2Fg%2F1v7tj2w1?entry=ttu",
    "https://www.google.com.tw/maps/place/%E6%A8%82%E5%A5%BD%E5%91%B3%E6%B6%BC%E9%BA%B5%E5%B0%8F%E9%A4%A8/@24.1716617,120.6736783,21z/data=!3m1!5s0x346917d119f27e39:0x68b3d48e054b56b5!4m14!1m7!3m6!1s0x3469175c40b583a5:0x2fafe51d9c6a35de!2z5YiB5rCRLemFuOiPnOmtmiDltIflvrflupc!8m2!3d24.1670963!4d120.6848373!16s%2Fg%2F11qm37nh6j!3m5!1s0x3469171d74f24649:0x1c165ff5b2f63a6c!8m2!3d24.1716743!4d120.6739409!16s%2Fg%2F11sqh57nfk?entry=ttu"
]

spider = DishesSpider(driver_path)


def scrape_dishes(url):
    dishes, err = spider.scrape_dishes(url)
    time.sleep(1)
    if err:
        print(err)
    else:
        print("--------" + url)
        for dish in dishes:
            print("--")
            print(dish.__dict__)
        wf.write(f"dishes_{url_list.index(url)}.json",
                 json.dumps(dishes.__dict__))


if __name__ == "__main__":
    start = time.time()

    max_workers = 5
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(scrape_dishes, url_list)

    end = time.time()
    print("執行時間：%f 秒" % (end - start))

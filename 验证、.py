import base64
import logging
import time
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

locale = "de_de"
chromedriver_path = "C:\\Users\\BOBO\\Downloads\\chromedriver.exe"

time_format = "%Y-%m-%d %H:%M:%S"
log_format = "%(asctime)s\t%(levelname)s\t\t%(message).50s"

logger = logging.getLogger()
logger.setLevel("INFO")
formatter = logging.Formatter(log_format, time_format)
chlr = logging.StreamHandler()  # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel("INFO")
fhlr = logging.FileHandler("hermes_cookie.log")  # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)


class VerifyCaptcha:
    def __init__(self):
        #self.url = (
        #    "https://bck.hermes.cn/products?locale="
        #    + locale
        #    + "&searchterm=lindy&sort=relevance"
        #)
        self.url = "https://www.hermes.com/de/de/search/?s=lindy"
        self.result = ""

    def start(self):
        self.open()
        try:
            self.result = self.get_cookie()
        except Exception as e:
            logging.error(e)
        finally:
            self.close()
        return self.result

    def open(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument('content-type="application/json"')
        self.chrome = webdriver.Chrome(
            executable_path=chromedriver_path, options=options,
        )

    def close(self):
        self.chrome.close()
        self.chrome.quit()

    def get_gap_test(self, picture0, picture1, picture2):
        position = picture0.getbbox()
        img = cv2.cvtColor(
            np.abs(np.array(picture2) - np.array(picture1)), cv2.COLOR_RGB2GRAY
        )

        _, img_both = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
        _, img_false = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

        pic_img_both = cv2.cvtColor(img_both, cv2.COLOR_GRAY2RGB)
        pic_img_false = cv2.cvtColor(img_false, cv2.COLOR_GRAY2RGB)

        img = cv2.cvtColor(
            np.abs(np.array(pic_img_both) - np.array(pic_img_false)), cv2.COLOR_RGB2GRAY
        )

        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, None)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, None)

        count = 0
        start = 0
        for i in range(img.shape[1]):
            if (
                img[position[1] + 10, i] == 255
                or img[position[3] - 10, i] == 255
                or img[(position[1] + position[3]) // 2, i] == 255
            ):
                count += 1
                if count == 30:
                    start = i - 30
                    break
            else:
                count = 0
        return start - 3

    def SimulateDragX(self, driver, source, targetOffsetX):
        def ease_out_quad(x):
            return 1 - (1 - x) * (1 - x)

        def ease_out_quart(x):
            return 1 - pow(1 - x, 4)

        def ease_out_expo(x):
            if x == 1:
                return 1
            else:
                return 1 - pow(2, -10 * x)

        def get_tracks(distance, seconds, ease_func):
            tracks = [0]
            offsets = [0]
            for t in np.arange(0.0, seconds, 0.1):
                offset = round(ease_func(t / seconds) * distance)
                tracks.append(offset - offsets[-1])
                offsets.append(offset)
            return offsets, tracks

        offsets, tracks = get_tracks(targetOffsetX, 0.5, ease_out_expo)
        ActionChains(driver).click_and_hold(source).perform()
        for x in tracks:
            ActionChains(driver).move_by_offset(x, 0).perform()
        ActionChains(driver).pause(0.5).release().perform()

    def get_picture(self, classname):
        img_info = self.chrome.execute_script(
            'return document.getElementsByClassName("'
            + classname
            + '")[0].toDataURL("image/png");'
        )
        img_base64 = img_info.split(",")[1]
        img_bytes = base64.b64decode(img_base64)
        picture = Image.open(BytesIO(img_bytes))
        return picture

    def get_cookie(self):
        chrome = self.chrome
        chrome.get(self.url)
        time.sleep(2)
        while "hermes.com" in chrome.title:
            logging.info("开始处理验证码")
            chrome.switch_to.frame(0)

            try:
                # 触发验证码
                WebDriverWait(chrome, 10).until(
                    lambda the_driver: the_driver.find_element_by_xpath(
                        '//div[@class="geetest_holder geetest_wind geetest_ready"]'
                    ).is_displayed(),
                    message="请勿将鼠标置于浏览器界面中！尝试解决...",
                )
                captcha = chrome.find_element_by_xpath(
                    '//div[@class="geetest_holder geetest_wind geetest_ready"]'
                )
                ActionChains(chrome).move_to_element_with_offset(
                    to_element=captcha, xoffset=0, yoffset=1
                ).perform()
                ActionChains(chrome).move_to_element_with_offset(
                    to_element=captcha, xoffset=0, yoffset=2
                ).perform()
            except Exception as e:
                logging.error(e)

                # 触发验证码
                WebDriverWait(chrome, 10).until(
                    lambda the_driver: the_driver.find_element_by_xpath(
                        '//div[@class="geetest_holder geetest_wind geetest_detect"]'
                    ).is_displayed(),
                    message="验证码触发失败",
                )
                captcha = chrome.find_element_by_xpath(
                    '//div[@class="geetest_holder geetest_wind geetest_detect"]'
                )
                ActionChains(chrome).move_to_element_with_offset(
                    to_element=captcha, xoffset=0, yoffset=1
                ).perform()
                ActionChains(chrome).move_to_element_with_offset(
                    to_element=captcha, xoffset=0, yoffset=2
                ).perform()

            # 加载验证码
            WebDriverWait(chrome, 10).until(
                lambda the_driver: the_driver.find_element_by_xpath(
                    "//div[@class='geetest_holder geetest_wind geetest_wait_compute']"
                ).is_displayed()
            )
            chrome.find_element_by_xpath(
                '//div[@class="geetest_holder geetest_wind geetest_wait_compute"]'
            ).click()

            # 显示验证码
            WebDriverWait(chrome, 10).until(
                lambda the_driver: the_driver.find_element_by_xpath(
                    "//div[@class='geetest_slider_button']"
                ).is_displayed()
            )
            slider = chrome.find_element_by_xpath(
                '//div[@class="geetest_slider_button"]'
            )

            # 滑块
            picture0 = self.get_picture("geetest_canvas_slice geetest_absolute")
            # 完整图
            picture1 = self.get_picture(
                "geetest_canvas_fullbg geetest_fade geetest_absolute"
            )
            # 缺口图
            picture2 = self.get_picture("geetest_canvas_bg geetest_absolute")

            gap = self.get_gap_test(picture0, picture1, picture2)
            self.SimulateDragX(chrome, slider, gap)

            time.sleep(10)
            if "hermes.com" in chrome.title:
                chrome.refresh()

        result = chrome.get_cookie("datadome")["value"]
        return result


if __name__ == "__main__":
    while True:
        try:
            cookie = VerifyCaptcha().start()
        except Exception as e:
            logging.error(e)
            continue
        if not cookie:
            continue
        with open("cookie.txt", "w", encoding="UTF-8") as f:
            f.write(cookie + "\n")
        time.sleep(120)

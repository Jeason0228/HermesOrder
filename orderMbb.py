from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import settings

class OrderProject:

    def __init__(self):
        self.__creatBrowser()
        self.index = 1

    def __creatBrowser(self):
        # 创建driver
        try:
            options = webdriver.ChromeOptions()
            if not settings.LOAD_IMAGES:
                prefs = {"profile.managed_default_content_settings.images": "2"}
                options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("debuggerAddress", "127.0.0.1:6001")
            driver = webdriver.Chrome(chrome_options=options)
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 600)
        except Exception as e:
            return

    def slow_type(self, element, text: str, delay: float = 0.1):
        """Send a text to an element one character at a time with a delay."""
        for character in text:
            element.send_keys(character)
            time.sleep(delay)

    def home_page(self):
        try:
            url = "https://www.hermes.com/pl/en"
            self.driver.get(url)
        except Exception as e:
            return

    def login(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.home_page()
        while "Please enable JS and disable any ad blocker" in self.driver.page_source:
            time.sleep(10)
        time.sleep(2)
        try:
            if "de/de" in self.driver.current_url:
                login_btn = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='header-navigation']/ul/li/button/span[contains(text(), 'Konto')]")))
            else:
                login_btn = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='header-navigation']/ul/li/button/span[contains(text(), 'Account')]")))
            login_btn.click()
            time.sleep(2)
        except Exception as e:
            pass

        try:
            if "cn/en" in self.driver.current_url:
                usernameInput = self.wait.until(EC.presence_of_element_located((By.ID, 'edit-loginphone--5')))
            else:
                usernameInput = self.wait.until(EC.presence_of_element_located((By.ID, 'login-email')))
            self.slow_type(usernameInput, username)

            password = self.wait.until(EC.presence_of_element_located((By.ID, 'login-password')))
            self.slow_type(password, passwd)

            login_submit = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#hermes-account-login-form div.submit-text')))
            login_submit.click()
        except Exception as e:
            pass

        totalTime = 0
        while not self.driver.find_elements_by_css_selector("p.notification-message-title"):
            time.sleep(5)
            totalTime += 10
            if totalTime > 100:
                self.login(username, passwd)
                break

        self.driver.get("https://www.hermes.com/pl/en/category/women/scarves-and-silk-accessories/#||Category")
        time.sleep(5)

        
    def make_order(self, url):
        if self.index == 1:
            self.index += 1
            self.driver.get(url)


            try:
                # if "de/de" in url:
                #     backStr = "Zurück"
                # else:
                #     backStr = "Back"
                back = self.driver.find_elements_by_css_selector("button.back-button")
                num = 0
                while not back:
                    back = self.driver.find_elements_by_css_selector("button.back-button")
                    time.sleep(0.5)
                    num += 0.5
                    if num >=2:
                        break

                js = 'document.getElementById("add-to-cart-button-in-stock").click();'
                self.driver.execute_script(js)
                # add_btn.click()
            except Exception as e:
                return
            time.sleep(30)
            self.index = 1
        #
        # while self.driver.find_elements_by_id('add-to-cart-button-in-stock'):
        #     try:
        #         add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-button-in-stock')))
        #         add_btn.click()
        #         time.sleep(1)
        #     except:
        #         break



    def restartBrowser(self):
        self.driver.get("https://www.hermes.com/pl/en/")
        account_btn = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='header-navigation']/ul/li/button/span[contains(text(), 'Account')]")))
        account_btn.click()
        time.sleep(1)

        sign_out_btn = self.wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.signed-in > a.logout-user")))

        sign_out_btn.click()

        time.sleep(15)
        self.login(self.username, self.passwd)



# if __name__ == '__main__':
#     app = OrderProject()
#     USERNAME = "libo985989982@hotmail.com"
#     PASSWD = "libo19930728"
#     # app.home_page()
#     app.login(USERNAME, PASSWD)
#     url = "https://www.hermes.com/pl/en/product/saut-hermes-25-bag-H079081CCAG/"
#     app.make_order(url)

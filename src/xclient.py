import os
import pickle as pkl
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

COOKIE_FILE = "cookies.pkl"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"

X_LOGIN_URL = "https://x.com/i/flow/login"
X_POST_URL = "https://twitter.com/intent/tweet?text={text}"
X_HOME_URL = "https://x.com/home"
USERNAME_XPATH = '//input[@name="text"]'
PASSWORD_XPATH = '//input[@name="password"]'
POST_XPATH = '//button[@data-testid="tweetButton"]'

IMPLICIT_WAIT = 20


class XClient:
    def __init__(self):
        pass

    def start(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument(f"user-agent={USER_AGENT}")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub", options=options
        )
        # self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(IMPLICIT_WAIT)

    def quit(self):
        self.driver.quit()

    def login(self, username: str, password: str, cookie_file: str = COOKIE_FILE):
        # クッキーが保存されている場合は読み込む
        if os.path.exists(cookie_file):
            print("cookie file exists")
            self.driver.get(X_HOME_URL)
            cookies = pkl.load(open(COOKIE_FILE, "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(X_HOME_URL)
        # クッキーが保存されていない場合はログインする
        else:
            print("cookie file does not exist")
            self.driver.get(X_LOGIN_URL)
            elem = self.driver.find_element(By.XPATH, USERNAME_XPATH)
            elem.send_keys(username)
            elem.send_keys(Keys.RETURN)

            elem = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)

        # ログイン後の画面が表示されるまで待つ
        WebDriverWait(self.driver, 10).until(EC.url_contains(X_HOME_URL))

        # クッキーを保存
        cookies = self.driver.get_cookies()
        pkl.dump(cookies, open(cookie_file, "wb"))

        time.sleep(2)

    def post(self, text: str):
        # ポスト画面に遷移
        url = X_POST_URL.format(text=text)
        self.driver.get(url)

        # ポストボタンを押下
        elem = self.driver.find_element(By.XPATH, POST_XPATH)
        elem.click()

        time.sleep(2)

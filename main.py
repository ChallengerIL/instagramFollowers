from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "nasa"
USERNAME = "bzayzemdowhhkzoccw@kvhrw.com"
PASSWORD = r"{(tt@?wq46\b}+D>"
PATH = "C:\Development\chromedriver.exe"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))

    def login(self):
        self.driver.get("https://www.instagram.com/")

        time.sleep(3)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(1)

        followers_count = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        followers_count.click()

        time.sleep(2)

        active = 0

        while active < 10:
            followers_list = self.driver.find_element(By.CSS_SELECTOR, '.isgrP')
            followers = followers_list.find_elements(By.TAG_NAME, "li")[-1]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", followers)
            active += 1
            time.sleep(1)

    def follow(self):
        followers_list = self.driver.find_element(By.CSS_SELECTOR, '.isgrP')
        followers_buttons = followers_list.find_elements(By.TAG_NAME, "button")

        for b in followers_buttons:
            b.click()
            time.sleep(1)


bot = InstaFollower(PATH)

bot.login()
time.sleep(2)
bot.find_followers()
bot.follow()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class job:
    def __init__(self,username,password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.naukri.com/'
        self.job = driver
        # self.login()

    def login(self):
            self.job.get(self.base_url)

            self.job.find_element_by_xpath(
                '//*[@id="login_Layer"]/div').click()
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input').send_keys(
                "amahendra1188@gmail.com")
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[3]/input').send_keys(
                "143&amahendra")
            time.sleep(5)

            self.job.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div/form/div[6]/button').click()
            time.sleep(3)

            self.job.find_element_by_xpath(
               '//*[@id="root"]/div/div/span/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div').click()
            time.sleep(3)

            self.job.find_element_by_xpath(
                '//*[@id="root"]/div/div/span/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/em').click()
            time.sleep(3)

            self.job.find_element_by_xpath(
                '//*[@id="saveBasicDetailsBtn"]').click()
            time.sleep(3)

j=job('****************','***********')
j.login()


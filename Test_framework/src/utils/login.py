# 登录模块
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
# from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader


class LoGin:
    URL = Config().get('URL')
    excel = DATA_PATH + '\TestLogin.xlsx'
    locator_button = (By.XPATH, Config().get('loginxpath'))
    phone = (By.XPATH, Config().get('phone'))
    Username = (By.ID, Config().get('Username'))
    password = (By.XPATH, Config().get('password'))
    # login_button = (By.XPATH, Config().get('login_button'))
    login_button = (By.XPATH, Config().get('login_button'))  # 登录页，登录按钮
    quit = (By.XPATH, Config().get('quit'))
    digital = Config().get('digital')
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    # driver.maximize_window()
    # driver.get(URL)

    # def __init__(self, driver):
    #     self.driver = driver

    def test_sup(DRIVER):
        self.driver = LoGin('driver')
        P = self.driver.driver
        driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        driver.maximize_window()
        driver.get(LoGin.URL)

    def test_search(self):
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.get(LoGin.URL)
        datas = ExcelReader(self.excel).data
        self.driver.find_element(*self.locator_button).click()
        time.sleep(3)
        self.driver.find_element(*self.phone).clear()
        self.driver.find_element(*self.phone).send_keys(datas[LoGin.digital]['username'])
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(datas[LoGin.digital]['password'])
        self.driver.find_element(*self.login_button).click()
        print(2)
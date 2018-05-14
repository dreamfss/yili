# coding = utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
# from Test_framework.src.utils.login import LoGin
from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait


class Test_Login(unittest.TestCase):
    # 页面元素定位（获取Config中配置）
    URL = Config().get('URL')  # 获取URL
    excel = DATA_PATH + '\TestLogin.xlsx'  # 所用表格
    phone = (By.XPATH, Config().get('phone'))  # 用户名输入框
    Username = (By.ID, Config().get('Username'))  # 登录后，用户名
    password = (By.XPATH, Config().get('password'))  # 密码输入框
    login_button = (By.XPATH, Config().get('login_button'))  # 登录页，登录按钮
    quit_button = (By.XPATH, Config().get('quit'))  # 首页，退出按钮
    login_account = (By.XPATH, Config().get('login_account'))  #未输入账号，提示信息
    login_password = (By.XPATH, Config().get('login_password'))  #未输入密码，提示信息
    Information = (By.XPATH, Config().get('Information'))  #登录失败，页面提示信息
    digital = Config().get('digital')

    @classmethod
    def sub_setUp(cls):
        # 调用登录模块中driver
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Test_Login.URL)
        print(1)
        # self.driver = p
        # LoGin.sub_setup(self.driver)

    def sub_tearDown(self):
        # 关闭游览器、命令框
        print(2)
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()  # 调用sub_setUp方法
            # self.driver.maximize_window()
            # self.driver.get(Test_Login.URL)
            datas = ExcelReader(self.excel).data  # 获取excell表格中字符串
            # 循环导入username、password
            # for index, d in enumerate(datas):
            #     time.sleep(3)
            self.driver.find_element(*self.phone).clear()  # 清空用户名输入框
            self.driver.find_element(*self.password).clear()  # 清空密码输入框
            self.driver.find_element(*self.phone).send_keys(
                datas[Test_Login.digital]['username'])  # 输入用户名（读取表格）
            self.driver.find_element(*self.password).send_keys(
                datas[Test_Login.digital]['password'])  # 输入密码（读取表格）
            self.driver.find_element(*self.login_button).click()  # 登录页，点击登录按钮
            print(2)
            time.sleep(2)
            handles = self.driver.current_url
            print(handles)
            # WebDriverWait(self.driver, 10).until(lambda driver:
            #                                      self.driver.find_element(*self.Username))
            # links = self.driver.find_element(*self.Username).text  # 通过ID，获得用户名
            # if links == Config().get('links'):  # 验证获得的用户名与配置文件中是否一致
            #     self.driver.find_element(*self.quit_button).click()  # 首页（已登录），退出按钮
            #     logger.info('登录成功')  # 登录成功日志
            self.sub_tearDown()  # 调用退出方法
        except Exception as msg:
            # 代码执行错误时，打印图片
            nowTime = time.strftime("%Y.%m.%d.%H.%M.%S") + ".test_001_login"  # 图片名称格式
            self.driver.get_screenshot_as_file(
                "D:\\TestCase\\Hypweb.Frame\\Test_framework\\log\\%s.png" % nowTime)  # 截屏图片
            logger.info("test_001_login.%s" % msg)
            self.sub_tearDown()  # 调用退出方法


if __name__ == '__main__':
    unittest.main()

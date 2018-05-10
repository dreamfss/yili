import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
from Test_framework.src.utils.login import LoGin
from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader


# from Test_framework.src.utils.login import login
# from Test_framework.src.utils.file_reader import ExcelReader
# from Test_framework.src.utils.HTMLTestRunner import HTMLTestRunner


class Test_Order(unittest.TestCase):
    # 页面元素定位（获取Config中配置）
    search_goods = Config().get('search_goods')  # 搜索商品
    search = (By.XPATH, Config().get('search'))  # 搜索栏

    @classmethod
    def sub_setUp(cls):
        # 调用登录模块中driver
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(LoGin.URL)

    def sub_tearDown(self):
        # 关闭游览器、命令框
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()  # 调用sub_setUp方法
            p = LoGin(self.driver)
            p.test_search()
            time.sleep(2)
            self.driver.find_element(*self.search).clear()  # 清空搜索栏
            self.driver.find_element(*self.search).send_keys(Test_Order.search_goods)
            time.sleep(3)
            logger.info('登录成功')  # 登录成功日志
            self.sub_tearDown()  # 调用退出方法
        except Exception:
            # 代码执行错误时，打印图片
            nowTime = time.strftime("%Y.%m.%d.%H.%M.%S") + ".test_003_login"  # 图片名称格式
            self.driver.get_screenshot_as_file(
                "D:\\TestCase\\Hypweb.Frame\\Test_framework\\log\\log%s.png" % nowTime)  # 截屏图片
            logger.warnning('登录失败')  # 登录失败日志
            logger.error('页面元素未找到')#登录失败日志
            self.sub_tearDown()  # 调用退出方法


if __name__ == '__main__':
    unittest.main()

import time
import unittest
from Test_framework.src.utils.login import LoGin
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config
from Test_framework.src.utils.log import logger


class Test_Member(unittest.TestCase):
    member_centre = (By.XPATH, Config().get('member_centre'))
    prompt = (By.XPATH, Config().get('prompt'))

    def sub_setUp(self):
        # 调用登录模块中driver
        self.driver = LoGin().driver

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()
            LoGin().test_search()
            self.driver.find_element(*self.member_centre).click()
            test = self.driver.find_element(*self.prompt).text
            links = test[3:7]
            print(links)
            if links == Config().get('links'):
                self.sub_tearDown()
                logger.info('会员中心登录成功')
        except Exception:
            # 代码执行错误时，打印图片
            nowtime = time.strftime("%Y.%m.%d.%H.%M.%S")+".test_002_member"
            self.driver.get_screenshot_as_file("D:\\TestCase\\Hypweb.Frame\\Test_framework\\log\\log%s.png" % nowtime)
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

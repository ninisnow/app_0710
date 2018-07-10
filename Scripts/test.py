import allure
import sys,os,time
sys.path.append(os.getcwd())
from Base.init_driver import get_driver

class Test_aa:
    def setup_class(self):
        self.driver = get_driver()
        time.sleep(3)

    def teardown_class(self):
        self.driver.quit()

    def get_screen(self):
        image_name = "./Screen/%d.png" % int(time.time())
        self.driver.get_screenshot_as_file(image_name)
        with open(image_name,"rb") as f:
            allure.attach("截图名字",f.read(),allure.attach_type.PNG)

    def test_abc(self):
        allure.attach("描述","内容")
        assert 1,self.get_screen()

    def test_efg(self):
        self.driver.find_element_by_xpath("//*[contains(@text,""分类)]").click()
        time.sleep(2)
        assert False,self.get_screen()

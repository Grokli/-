from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from chaojiying import Chaojiying_Client
from PIL import Image
from io import BytesIO
import time

# 初始化
CHAOJIYING_USERNAME = ''
CHAOJIYING_PASSWORD = ''
CHAOJIYING_SOFT_ID = 898072
CHAOJIYING_KIND = 9004


class CrackYY:
    def __init__(self):
        self.url = 'https://aq.yy.com/p/reg/account.do?appid=&url=&fromadv=udbclsd_r%27'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.browser.get(self.url)
        self.browser.switch_to.frame(self.browser.find_element_by_xpath('//iframe[@frameborder="no" and @scrolling="no"]'))
        self.chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD,CHAOJIYING_SOFT_ID)

    def get_yanzheng_element(self):
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'pw_main')))
        return element

    def get_position(self):
        element = self.get_yanzheng_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'],location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        print(type(screenshot))
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_yanzheng_image(self, name='dianchu.png'):
        top,bottom,left,right = self.get_position()
        print('验证码位置',top,bottom,left,right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        print(type(captcha))
        captcha.save(name)
        return captcha

    def get_poins(self, captcha_result):
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_yanzheng_element(),location[0], location[1]).click().perform()
            time.sleep(1)

    def touch_click_verify(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pw_submit')))
        button.click()

    def crack(self):
        image = self.get_yanzheng_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        result = self.chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        locations = self.get_poins(result)
        self.touch_click_words(locations)
        self.touch_click_verify()
        try:
            success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,'done_text'),'验证成功'))
            print(success)
        except TimeoutException:
            report = self.chaojiying.ReportError(result['pic_id'])
            print(report)
        finally:
            self.crack()


if __name__ == '__main__':
    crack = CrackYY()
    crack.crack()


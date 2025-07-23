from setting_floor import sele_setting;
import time;
from selenium.webdriver.common.by import By

webdriver=sele_setting.get_browser("edge");

time.sleep(5)

webdriver.get("https://www.baidu.com/");

time.sleep(5)
#send.keys() 的核心功能就是模拟键盘输入
webdriver.find_element(by=By.ID,value="kw").send_keys("国际新闻");

time.sleep(5)

webdriver.find_element(by=By.PARTIAL_LINK_TEXT,value="国际新闻 - 百度百科").click();
time.sleep(500)
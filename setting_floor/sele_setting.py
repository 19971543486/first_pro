from selenium import webdriver;
import time;
from selenium.webdriver.common.by import By

def get_browser(web_name):
    if web_name=="chrome":
        return webdriver.Chrome();
    elif web_name=="firefox":
        return webdriver.Firefox();
    elif web_name=="edge":
        return webdriver.Edge();
    else:
        print("请输入正确的浏览器");


def login(llq):
    llq=get_browser("edge")
    llq.get("http://127.0.0.1:8008/");
    time.sleep(3);

    llq.find_element(by=By.NAME, value="username").clear()
    time.sleep(3)

    llq.find_element(by=By.NAME, value="username").send_keys("admin")
    time.sleep(3)

    llq.find_element(by=By.NAME, value="password").clear()
    time.sleep(3)

    llq.find_element(by=By.NAME, value="password").send_keys("admin123")
    time.sleep(3)

    llq.find_element(by=By.ID, value="btnSubmit").click()
    time.sleep(3)
    return llq;
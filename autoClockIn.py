# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 填ChromeDriver地址
driveUrl = ".../chromedriver"
browser = webdriver.Chrome()

url = "https://cup.edu.cn"
browser.get(url)

browser.find_element(By.XPATH,'/html/body/article[1]/div[4]/div/div/div[2]/div[1]/ul/li[7]/a[1]').click()
sleep(1)
browser.switch_to.frame("loginIframe")

# 输入学号
stuID = ""
browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[6]/input[1]').send_keys(stuID)

# 输入密码
stuPassword = ""
browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[6]/input[2]').send_keys(stuPassword)

# 点击登录
browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[6]/div[3]').click()

browser.switch_to.default_content()

sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div[6]/section/div/a[3]/p').click()

# sleep时间可调，根据你的网速决定
sleep(1)
browser.find_element(By.XPATH,'//*[@id="launch"]/div[1]/div/div/div[4]').click()
sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[2]/a/div[1]/div[2]/div[1]/span').click()
sleep(10)

# 是否在校
holiday = True

if not holiday:
    # 是否在校，默认在校
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
    sleep(1)

    # 在校状态填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[4]/td[4]/div/div[1]/div/div/div/input').click()
    sleep(1)


    # 在校状态选择，1:4分别对应未离校、通勤京内工作站、实习以及其他临时出校。在xpath末尾处“li[]“中修改。默认未离校
    browser.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[1]/span').click()
    sleep(1)


    # 体温填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[12]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    

    # 1:2对应37.3度以下和以上。默认37.3度以下
    browser.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[1]/span').click()
    sleep(1)


    # 地理位置填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div/span').click()
    sleep(1)
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/div/ul[2]/li[4]').click()

    # 详细地理位置填写，默认润杰公寓
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/div/div[3]/textarea').send_keys("润杰公寓")
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/span/button[2]').click()
    sleep(1)

else :
    # 是否在校，默认不在校
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
    sleep(1)

    # 地理位置填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[5]/td[2]/div/div[1]/div/span').click()
    sleep(1)
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[5]/td[2]/div/div[1]/div[2]/div/ul[2]/li[4]').click()

    # 详细地理位置填写，填写家庭住址
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[5]/td[2]/div/div[1]/div[2]/div/div[3]/textarea').send_keys("")
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[5]/td[2]/div/div[1]/div[2]/span/button[2]').click()

    # 输入不在校状态
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[6]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[4]/span').click()

    # 5.是否存在以下状况：
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[7]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[1]/span').click()

    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[9]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[1]/span').click()

    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[10]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[1]/ul/li[1]/span').click()

    # 地理位置填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div/span').click()
    sleep(1)
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/div/ul[2]/li[4]').click()

    # 详细地理位置填写，填写家庭住址
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/div/div[3]/textarea').send_keys("")
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[11]/td[4]/div/div[1]/div[2]/span/button[2]').click()
    sleep(1)

    # 体温填报
    browser.find_element(By.XPATH,'//*[@id="pageBox"]/div[2]/div/table/tbody/tr[12]/td[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    

    # 1:2对应37.3度以下和以上。默认37.3度以下
    browser.find_element(By.XPATH,'/html/body/div[10]/div[1]/div[1]/ul/li[1]').click()
    sleep(1)

# 勾选承诺
browser.find_element(By.XPATH,'//*[@id="dradioviewRadio_197"]/label/span').click()
sleep(2)
if not holiday:
    browser.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div[2]/a').click()
else :
    browser.find_element(By.XPATH,'/html/body/div[11]/div/div[2]/div/div[2]/a').click()


# 提交
browser.execute_script("arguments[0].click();", browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button'))


sleep(3)
browser.quit()

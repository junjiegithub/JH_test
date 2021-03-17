#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
#coding=utf-8
import time
import random
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.support import expected_conditions as EC
#pip install Configparser
driver = webdriver.Chrome()  # 定义变量存webdriver

#初始化浏览器
def driver_init():
    #driver = webdriver.Chrome()#定义变量存webdriver
    driver.get("https://grayads-sc.jhongnet.com/")   #get网址
    driver.maximize_window()
    time.sleep(3)

#获取element信息
def get_element(name_xpath):
    element =driver.find_element_by_xpath(name_xpath)
    return element

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)  # 截取整个网页并保存到D盘
    code_element =driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/form/div[3]/div/div/div[2]/img")  # 定义变量获取验证码的定位元素
    # print(code_element.location)#{'x': 795, 'y': 359}       #打印验证码在网页上的坐标
    left = code_element.location['x']  # 定义验证码左边的定位数值
    top = code_element.location['y']  # 定义验证码上边的坐标
    right = code_element.size['width'] + left  # 定义验证码图片的宽度和坐标
    height = code_element.size['height'] + top  # 定义验证码图片的宽度和坐标
    im = Image.open(file_name)  # 定义打开保存的网页截图
    img = im.crop((left, top, right, height))  # 定义整个验证码的4个坐标
    img.save(file_name)  # 保存截取的验证码图片到D盘

#解析图片获取验证码
def code_online(file_name):
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)  # 识别图片
    print(text)
    return text

#运行主程序
def run_main():
    # user_name_info =get_range_user()
    login_name ="liu.xy@jiahongnet.com"
    password="123456"
    file_name ="D:/b.png"
    driver_init()
    get_element("//*[@id='app']/div/div[2]/div[2]/form/div[1]/div/div[1]/input").send_keys(login_name)
    get_element("//*[@id='app']/div/div[2]/div[2]/form/div[2]/div/div[1]/input").send_keys(password)
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("//*[@id='app']/div/div[2]/div[2]/form/div[3]/div/div[1]/div[1]/input").click()
    time.sleep(3)
    get_element("//*[@id='app']/div/div[2]/div[2]/form/div[3]/div/div[1]/div[1]/input").send_keys(text)

    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[2]").click()



run_main()
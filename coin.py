import os
import sys
import time
import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
Email = ""
Password = ""
def cash():

    option = webdriver.ChromeOptions()
    bot = webdriver.Chrome(executable_path=CM().install(), options=option)
    bot.set_window_size(500, 950)
    link = 'https://www.coinpayu.com/dashboard'
    bot.get(link)
    time.sleep(5)
    bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[2]/a').click()

    bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[2]/div/div[3]/a/p/span').click()



    bot.find_elements_by_class_name("videoList-msg-title").click()
    time.sleep(62)
    pyautogui.keyDown('ctrl')
    pyautogui.keyUp('w')

cash()

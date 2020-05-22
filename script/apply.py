"""=====================================================

                        import

====================================================="""
import pandas as pd
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime
import traceback
from slacker import Slacker
from google.cloud import storage
import os
import re
import requests
import random
"""=====================================================

                        read_info

====================================================="""
with open("private_info.txt","r") as f:
    info=f.read().split("\n")

email=info[0].replace("email:","")
password=info[1].replace("password:","")
apply_num=int(info[2].replace("apply_num:",""))
"""=====================================================

                        main

====================================================="""

if __name__ == '__main__':
    try:
        # HEADLESSブラウザに接続
        driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        #dmainに遷移
        driver.get("https://www.wantedly.com")
        sleep(5)

        #ログイン画面に遷移
        driver.find_element_by_class_name("ui-show-modal").click()

        driver.find_element_by_id('login_user_email').send_keys(email)#メアド入力
        driver.find_element_by_id('login_user_password').send_keys(password)#パスワード入力
        #ホームに遷移
        driver.find_element_by_name("commit").click()

        #パラメータ設定
        trial_num=100000
        start_id,limit_id=1,140000000
        count=0
        apply_id=[]

        for _ in range(trial_num):
            random_num=random.randint(start_id,limit_id)#ランダムなIDに遷移
            driver.get("https://www.wantedly.com/users/{}".format(str(random_num)))
            try:
                request_button=driver.find_element_by_css_selector('a[class="wt-ui-button connection-request-button"]').click()
                count+=1
                apply_id.append(random_num)
                sleep(2)
                if count>=apply_num:
                    break
            except:
                pass

        driver.close
                
        

    finally:
        # 終了
        driver.close()
        driver.quit()

        for num in apply_id:
            print(num)


# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 10:52:36 2019

@author: arindam halder
"""

import time
import os
from selenium import webdriver

cwd = os.getcwd()
filePath = os.path.join(cwd, "test.jpg")

# browser = webdriver.Chrome(executable_path = './chrome/78/chromedriver.exe')
browser = webdriver.Firefox()
browser.get('https://www.atg.party') 

''' Use Navigation Timing  API to calculate the timings that matter the most '''   
 
navigationStart = browser.execute_script("return window.performance.timing.navigationStart")
responseStart = browser.execute_script("return window.performance.timing.responseStart")
domComplete = browser.execute_script("return window.performance.timing.domComplete")
 
''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
 
print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

time.sleep(3)


# browser.find_element_by_xpath('//*[@title="Search"]').click()
login_buttton = browser.find_element_by_css_selector('a.additional_signin')
login_buttton.click()
time.sleep(3)
inputEmail = browser.find_element_by_id("email")
inputEmail.send_keys("wiz_saurabh@rediffmail.com")
time.sleep(3)
inputPassword = browser.find_element_by_id("password")
inputPassword.send_keys("Pass@123")
time.sleep(3)
signinButton = browser.find_element_by_id("reset_button")
time.sleep(15)
browser.get('https://www.atg.party/article')
time.sleep(9)
inputTitle = browser.find_element_by_name("title")
inputTitle.send_keys("Arindam's Party")
time.sleep(9)
partyDescInput = browser.find_element_by_css_selector('div.fr-element.fr-view')
partyDescInput.send_keys("It is gonna be wonderful bachelor's party!!")
time.sleep(9)
browser.find_element_by_id("article_pic").send_keys(filePath)
time.sleep(9)
# browser.find_element_by_id("featurebutton").click()
browser.find_element_by_css_selector('button.btn.btn-post').click()
time.sleep(9)
url = browser.current_url
print(url)
time.sleep(7)
browser.quit()

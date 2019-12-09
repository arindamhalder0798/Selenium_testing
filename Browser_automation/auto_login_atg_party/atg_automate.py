# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:52:36 2019

@author: arindam halder
"""

import time
import os
from selenium import webdriver
from datetime import datetime

cwd = os.getcwd()
filePath = os.path.join(cwd, "test.jpg")
print("\n\n\n Testing has results are as follows:\n")
# browser = webdriver.Firefox()
browser = webdriver.Chrome(executable_path = './chrome/78/chromedriver.exe')
#string fbrowserile to save in log
log_file = ""
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
log_file = log_file + "Date and time = " + str(dt_string) + "\n\n"
browser_name = browser.capabilities['browserName']
version = browser.capabilities['browserVersion']
# print(browser.capabilities)
log_file = log_file + "Browser version: " + str(browser_name) + " " + str(version) + "\n"

log_file = log_file + "Tester Name : Arindam Halder" + "\n"

print(log_file)
browser.get('https://www.atg.party') 
time.sleep(2)
browser.maximize_window()

''' Use Navigation Timing  API to calculate the timings '''   
 
navigationStart = browser.execute_script("return window.performance.timing.navigationStart")
responseStart = browser.execute_script("return window.performance.timing.responseStart")
domComplete = browser.execute_script("return window.performance.timing.domComplete")
 
''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

log_file = log_file + "Back End loading time: " + str(backendPerformance_calc)+ "\n"
log_file = log_file + "Front End loading time: " + str(frontendPerformance_calc)+ "\n"

print("Back End loading time: %s" % backendPerformance_calc)
print("Front End loading time: %s" % frontendPerformance_calc)

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
signinButton.click()
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
log_file = log_file + "Url after posting the event: " + str(url)+ "\n\n ===========================================================\n\n\n"
print("Url after posting the event:",url)
time.sleep(7)
browser.quit()
with open("test_log.txt", "a") as myfile:
    myfile.write(log_file)
print("Log file has been saved. Exiting ..")

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_to_do_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todo/")
    ermsg = driver.find_element_by_xpath("//div[@class ='alert alert-warning']").text
    pageHeader = driver.find_element_by_xpath("//div/h2").text
    tdItems = ""
    try :
        element= driver.find_element_by_xpath("//div[@class='list-group']")
        if element.is_displayed():
            tdItems == "there"
            return(tdItems)
        else:
            tdItems == "not there"
            return(tdItems)
    except:
        tdItems == "not there"
        return(tdItems)
    assert 'not there' == tdItems and ermsg == "You're not logged in!" and pageHeader == 'Todos | Team Green Tea'
    driver.close()

def test_get_to_do_page_url_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://127.0.0.1:8000/todo/")

    chkheader = driver.find_element_by_xpath("//div/h2").text
    TDCountRows = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    
    assert  'Todos | Team Green Tea' == chkheader and TDCountRows >= 0
    driver.close()


import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_delete_to_do_item_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todo/")

    ermsg = driver.find_element_by_xpath("//div[@class ='alert alert-warning']").text
    pageHeader = driver.find_element_by_xpath("//div/h2").text
    DeleteTDBtn = ""
    try :
        element= driver.find_element_by_xpath("//input[@type='submit' and @value='Delete']")
        if element.is_displayed():
            DeleteTDBtn == "there"
            return(DeleteTDBtn)
        else:
            DeleteTDBtn == "not there"
            return(DeleteTDBtn)
    except:
        DeleteTDBtn == "not there"
        return(DeleteTDBtn)
    
    assert 'not there' == DeleteTDBtn and ermsg == "You're not logged in!" and pageHeader == 'Todos | Team Green Tea'
    driver.close()

def test_delete_to_do_item_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)

    driver.get("http://127.0.0.1:8000/todo/")
    rowcountbefore = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))    
    driver.find_element_by_xpath("//input[@type='submit' and @value='Delete']").click()    
    rowcountafterdelete = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))

    assert rowcountbefore -1  == rowcountafterdelete
    driver.close()

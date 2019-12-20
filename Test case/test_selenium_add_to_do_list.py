import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_add_to_do_item_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/add") #incomplete
    assert  'Login Page' == driver.title
    driver.close()

def test_add_to_do_item_logged_in_blank_to_do_items_field():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/add") #incomplete
    ##blahblah something add
    assert  'Add To Do Item' == driver.title && errormsg == "" ##errormsg shown
    driver.close()

def test_add_to_do_item_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/add") #incomplete
    ##blahblah do some adding
    ##blahblah search for "JiaweiTest" in one of the rows or smth
    assert  'To Do List' == driver.title && smth == "JiaweiTest" ##assert same page and the To Do Item got added
    driver.close()

def test_add_to_do_item_logged_in_timestamp():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/add") #incomplete
    ##blahblah do some adding
    ##blahblah search for "JiaweiTest" in one of the rows or smth
    ##blahblah look for date time
    assert  'To Do List' == driver.title && smth == "timeStampTestJiawei" && datetimesmth == datetime.now
    ##assert same page and the To Do Item got added and the date time of the item created same as now
    driver.close()

    

    

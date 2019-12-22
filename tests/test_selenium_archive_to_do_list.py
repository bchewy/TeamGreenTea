import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_archive_to_do_item_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/") #delete fields? dk how they going delete
    assert  'Login Page' == driver.title
    driver.close()

def test_archive_to_do_item_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/add") #incomplete
    ##blahblah select something then delete
    assert  'To Do Item' == driver.title #check make sure the number of H2 reduced
    driver.close()

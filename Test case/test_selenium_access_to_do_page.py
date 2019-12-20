import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_to_do_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    assert  'Login Page' == driver.title
    driver.close()

def test_get_to_do_page_url_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    assert  'To Do List' == driver.title
    driver.close()


import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_to_do_history_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    assert  'Login Page' == driver.title
    driver.close()

def test_get_to_do_history_page_url_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    assert  'To Do History' == driver.title
    driver.close()

def test_view_list_of_to_do_history_items_contains_added_item():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    lastaddeditem = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text #Switch to search for JiaweiTest
    assert  'To Do History' == driver.title and lastaddeditem == 'JiaweiTest'
    driver.close()

def test_view_list_of_to_do_history_items_contains_deleted_item():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    lastaddeditem = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text #Switch to search for JiaweiTest
    assert  'To Do History' == driver.title and lastaddeditem == 'JiaweiTest'
    driver.close()

'''
def test_view_list_of_to_do_history_items():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todolist/")
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr")) #counting rows
    assert  'To Do History' == driver.title and row_count >= 1
    driver.close()
'''

import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
#Sprint 1
def test_get_to_do_history_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todo_history/")

    ermsg = driver.find_element_by_xpath("//div[@class ='alert alert-warning']").text
    pageHeader = driver.find_element_by_xpath("//div/h1").text
    tdHistoryItems = ""
    try :
        element= driver.find_element_by_xpath("//div[@class='list-group']")
        if element.is_displayed():
            tdHistoryItems == "there"
            return(tdHistoryItems)
        else:
            tdHistoryItems == "not there"
            return(tdHistoryItems)
    except:
        tdHistoryItems == "not there"
        return(tdHistoryItems)
    assert 'not there' == tdItems and ermsg == "You're not logged in!" and pageHeader == 'Todo History Page!'
    driver.close()

def test_get_to_do_history_page_url_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)
    
    driver.get("http://127.0.0.1:8000/todo_history/")
    chkheader = driver.find_element_by_xpath("//div/h1").text
    assert  'Todo History Page!' == chkheader
    driver.close()

def test_view_list_of_todo_history_items():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)
    
    driver.get("http://127.0.0.1:8000/todo_history/")
    row_count = len(driver.find_elements_by_xpath("//table[@class='table table-striped']/tbody/tr"))
    lastaddeditemaddtype = driver.find_element_by_xpath("//table/tbody/tr/td[contains(text(), 'Added')]").text
    assert row_count >= 1 and lastaddeditemaddtype == 'Added'
    driver.close()


def test_view_list_of_to_do_history_items_contains_just_added_item():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)
    #adding test data
    driver.get("http://127.0.0.1:8000/todo/")
    driver.find_element_by_xpath("//input[@placeholder='What do you need to do?']").send_keys("TestAddingForHistory")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Add']").click()
    
    driver.get("http://127.0.0.1:8000/todo_history/")
    lastaddeditemname = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[contains(text(), 'TestAddingForHistory')]").text
    lastaddeditemaddtype = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[contains(text(), 'Added')]").text
    assert lastaddeditemname == 'TestAddingForHistory' and lastaddeditemaddtype == 'Added'
    driver.close()

#Sprint 2
def test_view_list_of_to_do_history_items_contains_deleted_item(): 
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)   
    #Deleteing Test Data
    driver.get("http://127.0.0.1:8000/todo/")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Delete']").click()   
       
    driver.get("http://127.0.0.1:8000/todo_history/")
    lastaddeditemAddType = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[contains(text(), 'Deleted')]").text
    assert lastaddeditemAddType == 'Deleted'
    driver.close()


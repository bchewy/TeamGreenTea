import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
#Sprint 1
def test_get_to_do_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todo/")

    ermsg = driver.find_element_by_xpath("//div[@class ='alert alert-warning']").text
    pageHeader = driver.find_element_by_xpath("//div/h2").text
    TDCheckAddBtn = ""

    try :
        element= driver.find_element_by_xpath("//input[@type='submit' and @value='Add']")
        if element.is_displayed():
            TDCheckAddBtn == "there"
            return(TDCheckAddBtn)
        else:
            tdItems == "not there"
            return(TDCheckAddBtn)
    except:
        TDCheckAddBtn == "not there"
        return(TDCheckAddBtn)
    
    assert 'not there' == TDCheckAddBtn and ermsg == "You're not logged in!" and pageHeader == 'Todos | Team Green Tea'
    driver.close()

def test_add_to_do_item_logged_in_blank_to_do_items_field():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)

    driver.get("http://127.0.0.1:8000/todo/")
    rowcountbeforeadd = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    driver.find_element_by_xpath("//input[@placeholder='What do you need to do?']").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Add']").click()
    
    rowcountafteradd = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))

    assert rowcountbeforeadd == rowcountafteradd
    driver.close()


def test_add_to_do_item_logged_in():
    chkAddedData =""
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)

    driver.get("http://127.0.0.1:8000/todo/")
    rowcountbeforeadd = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    driver.find_element_by_xpath("//input[@placeholder='What do you need to do?']").send_keys("JiaweiTest")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Add']").click()
    
    rowcountafteradd = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    try :
        element= driver.find_element_by_xpath("//*[contains(text(), 'JiaweiTest')]")
        if element.is_displayed():
            chkAddedData == "there"
            return(chkAddedData)
        else:
            chkAddedData == "not there"
            return(chkAddedData)
    except:
        chkAddedData == "not there"
        return(chkAddedData)

    assert rowcountbeforeadd +1 == rowcountafteradd and chkAddedData == 'there'
    driver.close()

#Sprint 2
def test_add_to_do_item_logged_in_timestamp():
    chkAddedData =""
    chkTimeField =""
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)

    driver.get("http://127.0.0.1:8000/todo/")
    driver.find_element_by_xpath("//input[@placeholder='What do you need to do?']").send_keys("TestDateTime")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Add']").click()

    try :
        element= driver.find_element_by_xpath("//*[contains(text(), 'JiaweiTest')]")
        if element.is_displayed():
            chkAddedData == "there"
            return(chkAddedData)
        else:
            chkAddedData == "not there"
            return(chkAddedData)
    except:
        chkTimeField == "not there"
        return(chkAddedData)

    try :
        element= driver.find_element_by_xpath("//div[@class='d-flex w-100 justify-content-between']/small]")
        if element.is_displayed():
            chkTimeField == "there"
            return(chkTimeField)
        else:
            chkTimeField == "not there"
            return(chkTimeField)
    except:
        chkTimeField == "not there"
        return(chkTimeField)

    assert chkAddedData == 'there' and chkTimeField == 'there'

    

    

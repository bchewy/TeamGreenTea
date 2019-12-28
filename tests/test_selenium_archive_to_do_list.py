import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_to_do_history_page_url_not_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/todo/")

    ermsg = driver.find_element_by_xpath("//div[@class ='alert alert-warning']").text
    pageHeader = driver.find_element_by_xpath("//div/h2").text
    TDArchiveBtn = ""
    try :
        element= driver.find_element_by_xpath("//div[@class='list-group']")
        if element.is_displayed():
            TDArchiveBtn == "there"
            return(TDArchiveBtn)
        else:
            TDArchiveBtn == "not there"
            return(TDArchiveBtn)
    except:
        TDArchiveBtn == "not there"
        return(TDArchiveBtn)
    
    assert 'not there' == TDArchiveBtn and ermsg == "You're not logged in!" and pageHeader == 'Todos | Team Green Tea'
    driver.close()

def test_archive_to_do_item_logged_in():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/accounts/login/")
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    elemPassword.send_keys(Keys.RETURN)
    #Count rows at Archive Page
    driver.get("http://127.0.0.1:8000/todoArchived/")
    ArchivePageRowCountBeforeArchive = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    #Count rows at TD Page
    driver.get("http://127.0.0.1:8000/todo/")
    TDPageRowCountBeforeArchive = len(driver.find_elements_by_xpath("//div[@class='list-group']/a")) 
    driver.find_element_by_xpath("//input[@type='submit' and @value='Archive']").click()
    TDPageRowCountAfterArchive = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))
    #Count rows at Archive Page
    driver.get("http://127.0.0.1:8000/todoArchived/")
    ArchivePageRowCountAfterArchive = len(driver.find_elements_by_xpath("//div[@class='list-group']/a"))

    assert TDPageRowCountBeforeArchive -1 == TDPageRowCountAfterArchive and ArchivePageRowCountBeforeArchive +1 == ArchivePageRowCountAfterArchive
    driver.close()

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_item_existence_on_diffAccount():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Login").click()
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")
    
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)

    driver.find_element_by_link_text("Logout").click()
    driver.find_element_by_link_text("Login").click()

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("admin")
    
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")

    elemPassword.send_keys(Keys.RETURN)

#def test_filter_to_do_list():
    
#def test_viewable_selectable_to_do_list():

#def test_viewable_unselectable_to_do_list():

#def test_viewable_to_do_list():

#def test_unviewable_to_do_list():

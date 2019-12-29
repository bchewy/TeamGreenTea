import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_sign_up_page():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    
def test_sign_up_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    #assert driver.find_element_by_class_name("errornote")
    assert driver.find_element_by_css_selector("input:invalid")

def test_sign_up_UsernameConfirm_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()
    
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    #assert driver.find_element_by_class_name("errornote")
    assert driver.find_element_by_css_selector("input:invalid")

def test_sign_up_PasswordConfirm_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("JunYoung")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    #assert driver.find_element_by_class_name("errornote")
    assert driver.find_element_by_css_selector("input:invalid")

def test_sign_up_UsernamePassword_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("admin1234@")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    #assert driver.find_element_by_class_name("errornote")
    assert driver.find_element_by_css_selector("input:invalid")

def test_sign_up_with_CPassword_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("JunYoung")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    #assert driver.find_element_by_class_name("errornote")
    assert driver.find_element_by_css_selector("input:invalid")

def test_sign_up_with_CPassword_wrong():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("SarahLee")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("TestingEverything123")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("123Password")

    elemSUpCPassword.send_keys(Keys.RETURN)
    #assert driver.find_element_by_class_name("errornote")

def test_sign_up_with_CPassword_correct():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Register").click()

    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("DarrenYap")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("admin1234@")

    elemSUpCPassword.send_keys(Keys.RETURN)


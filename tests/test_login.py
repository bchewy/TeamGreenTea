import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_fail_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_blank_username_wrong_password():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Password123")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_blank_username_correct_password():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_blank_password_wrong_username():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JohnDoe69")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_blank_password_correct_username():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JohnDoe69")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Password123")

    elemPassword.send_keys(Keys.RETURN)
    #assert driver.find_element_by_css_selector("input:invalid")
    assert driver.find_element_by_class_name("errornote")

def test_login_wrong_username():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JohnDoe69")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    #assert driver.find_element_by_css_selector("input:invalid")

def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Password123")

    elemPassword.send_keys(Keys.RETURN)
    #assert driver.find_element_by_css_selector("input:invalid")
    assert driver.find_element_by_class_name("errornote")

def test_login_pass():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    assert "Site administration" in driver.title

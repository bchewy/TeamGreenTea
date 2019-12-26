import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_sign_up_page():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    #driver.find_element_by_link_text("Add user").click()
    #driver.find_element_by_xpath('//a[@href="'+admin/auth/user/+'"]').click()
    driver.find_element_by_class_name("addlink").click()

    #assert "Add user" in driver.find_element_by_tag_name('h1')
    assert driver.find_element_by_class_name("colM")

def test_sign_up_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_UsernameConfirm_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_PasswordConfirm_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("JunYoung")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_UsernamePassword_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("admin1234@")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_with_CPassword_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("JunYoung")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_with_CPassword_wrong():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("JunYoung")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("123Password")

    elemSUpCPassword.send_keys(Keys.RETURN)
    
    assert driver.find_element_by_class_name("errornote")

def test_sign_up_with_CPassword_correct():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("dishonored")

    elemPassword.send_keys(Keys.RETURN)
    driver.get("http://localhost:8000/admin/")
    
    driver.find_element_by_link_text("Users").click()
    
    driver.find_element_by_class_name("addlink").click()
    elemSUpName = driver.find_element_by_name("username")
    elemSUpName.send_keys("DarrenYap")

    elemSUpPassword = driver.find_element_by_name("password1")
    elemSUpPassword.send_keys("admin1234@")

    elemSUpCPassword = driver.find_element_by_name("password2")
    elemSUpCPassword.send_keys("admin1234@")

    elemSUpCPassword.send_keys(Keys.RETURN)

    assert driver.find_element_by_class_name("success")

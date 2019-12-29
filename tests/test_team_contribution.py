import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_access_team_contri():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Contributions").click()

    assert driver.find_element_by_class_name("container")

#def test_add_new_task():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_activity_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_task_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_roles_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_team_member_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_assign_task_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_unassign_task_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_assign_roles_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

#def test_unassign_roles_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todo/")
#    driver.find_element_by_link_text("Contributions").click()

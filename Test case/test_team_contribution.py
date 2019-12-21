import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_add_new_task():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/todo/")
    driver.find_element_by_link_text("Contributions").click()

    assert driver.find_element_by_class_name("container")

#def test_activity_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_task_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_roles_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_team_member_select():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_assign_task_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_unassign_task_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_assign_roles_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

#def test_unassign_roles_to_member():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8000/todolist/contributions/")

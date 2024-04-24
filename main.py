import json
from variables import Credentials, Locations
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

DRIVER = webdriver.Chrome()

with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def wait_till_close():
    sleep(30)
    DRIVER.quit()


def get_website(website):
    DRIVER.get(website)
    sleep(3)


def enter_data(element_field, data):
    selected = DRIVER.find_element(By.XPATH, element_field)
    selected.send_keys(data)
    sleep(1)


def click_button(button):
    DRIVER.find_element(By.XPATH, button).click()
    sleep(3)


def automate_home_page():
    """Enters email and pass for home page"""
    get_website(Credentials.url)
    enter_data(Locations.field_email, Credentials.email)
    click_button(Locations.home_page_btn)
    enter_data(Locations.field_pass, Credentials.password)
    click_button(Locations.home_page_btn)
    print("Waiting for PWSL Page")
    sleep(15)


def wait_for_pwsl():
    wait = WebDriverWait(DRIVER, 10)
    wait.until(EC.title_is("Pre-Work Safety Log NEW (Page 1 of 3)"))
    print("start")


def harzard_buttons():
    click_button(Locations.driving_btn)
    click_button(Locations.ladder_btn)
    click_button(Locations.tool_btn)
    click_button(Locations.slip_btn)
    click_button(Locations.trip_btn)


def automate_pwsl():
    wait_for_pwsl()
    click_button(Locations.home_btn)
    sleep(1)
    enter_data(Locations.field_user_id, Credentials.employee_id)
    enter_data(Locations.field_location, Credentials.location)
    click_button(Locations.no_btn)
    sleep(1)
    enter_data(Locations.field_equipment, Credentials.equipment)
    enter_data(Locations.field_task, Credentials.task)
    harzard_buttons()
    enter_data(Locations.field_describe, Credentials.hazard)
    enter_data(Locations.field_tools, Credentials.tools)
    enter_data(Locations.field_easier, Credentials.na)
    enter_data(Locations.field_unique, Credentials.na)
    click_button(Locations.ppe_btn)
    click_button(Locations.safety_btn)
    click_button(Locations.next_btn)
    click_button(Locations.none_btn)
    click_button(Locations.normal_btn)
    click_button(Locations.submit_btn)


automate_home_page()
automate_pwsl()
wait_till_close()

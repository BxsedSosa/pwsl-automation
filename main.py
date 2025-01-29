import json, sys, os
from variables import Credentials, Locations
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

DRIVER = webdriver.Chrome()


def translate_path(file):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        file_path = os.path.join(sys._MEIPASS, file)
    else:
        file_path = os.path.abspath(file)

    return file_path


text_file = translate_path("./text.json")


with open(text_file, "r", encoding="utf-8") as file:
    MSG = json.load(file)


def wait_till_close():
    sleep(10)
    DRIVER.quit()


def get_website(website):
    DRIVER.get(website)
    sleep(3)


def enter_data(element_field, data):
    selected = DRIVER.find_element(By.XPATH, element_field)
    selected.send_keys(data)
    sleep(0.5)


def click_button(button):
    DRIVER.find_element(By.XPATH, button).click()
    sleep(0.1)


def automate_home_page():
    """Enters email and pass for home page"""
    get_website(Credentials.url)
    sleep(7)
    enter_data(Locations.field_email, Credentials.email)
    click_button(Locations.home_page_btn)
    sleep(7)
    print("Waiting for PWSL Page")
    sleep(30)


def harzard_buttons():
    click_button(Locations.driving_btn)
    click_button(Locations.ladder_btn)
    click_button(Locations.tool_btn)
    click_button(Locations.slip_btn)
    click_button(Locations.trip_btn)


def automate_pwsl():
    click_button(Locations.home_btn)
    sleep(1)
    enter_data(Locations.field_user_id, Credentials.employee_id)
    enter_data(Locations.field_location, Credentials.location)
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

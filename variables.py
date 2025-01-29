import json

with open("./text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


class Credentials:

    url = MSG["home"]["url"]
    email = MSG["credentials"]["user"]
    password = MSG["credentials"]["pass"]
    employee_id = MSG["credentials"]["employee-id"]
    location = MSG["credentials"]["location"]
    equipment = MSG["credentials"]["equipment"]
    task = MSG["credentials"]["task"]
    hazard = MSG["credentials"]["hazard"]
    tools = MSG["credentials"]["tools"]
    na = MSG["credentials"]["na"]


class Locations:

    home_page_btn = MSG["element"]["submit-btn"]
    field_email = MSG["element"]["email"]
    field_pass = MSG["element"]["pass"]

    home_btn = MSG["pwsl"]["element"]["home-btn"]
    field_user_id = MSG["pwsl"]["element"]["employee-id"]
    field_location = MSG["pwsl"]["element"]["location"]
    field_equipment = MSG["pwsl"]["element"]["equipment"]
    field_task = MSG["pwsl"]["element"]["task"]
    driving_btn = MSG["pwsl"]["element"]["hazard"]["driving"]
    ladder_btn = MSG["pwsl"]["element"]["hazard"]["ladder"]
    tool_btn = MSG["pwsl"]["element"]["hazard"]["hand-tool"]
    slip_btn = MSG["pwsl"]["element"]["hazard"]["slip"]
    trip_btn = MSG["pwsl"]["element"]["hazard"]["trip"]
    field_describe = MSG["pwsl"]["element"]["describe"]
    field_tools = MSG["pwsl"]["element"]["tools"]
    field_easier = MSG["pwsl"]["element"]["easier"]
    field_unique = MSG["pwsl"]["element"]["unique"]
    safety_btn = MSG["pwsl"]["element"]["safety-btn"]
    ppe_btn = MSG["pwsl"]["element"]["ppe-btn"]
    next_btn = MSG["pwsl"]["element"]["next-btn"]
    none_btn = MSG["pwsl"]["element"]["none-btn"]
    normal_btn = MSG["pwsl"]["element"]["normal-btn"]
    submit_btn = MSG["pwsl"]["element"]["submit-btn"]

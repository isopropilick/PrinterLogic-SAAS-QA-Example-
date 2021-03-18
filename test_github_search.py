from selenium import webdriver
import time
import allure
import csv
import pytest
test_data=[]
driver = webdriver.Firefox(executable_path="webdriver/gecko/windows_64/geckodriver.exe")
with open("test-data/users.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        test_data.append(row)
    test_data.pop(0)

@allure.feature('Log-in window')
@pytest.mark.parametrize('data',test_data)
def test_login(data):
    user=data[0]
    password=data[1]
    global driver
    driver.get('https://ericp.printercloud.com/admin/')
    print("user: "+user+"//"+"password: "+password)
    user_input=driver.find_element_by_xpath("//input[@id='relogin_user']")
    pswd_input = driver.find_element_by_xpath("//input[@id='relogin_password']")
    login_btn=driver.find_element_by_xpath("//button[@id='admin-login-btn']")
    login_text=driver.find_element_by_xpath("//div[@id='logintext']")
    user_menu=driver.find_element_by_xpath("//body[@id='thebody']/div[@id='header']/ul[@id='utility']/li[1]").get_attribute("innerHTML")
    if data[2] == 'pass':
        user_input.send_keys(user)
        pswd_input.send_keys(password)
        login_btn.click()
        time.sleep(50)
        usr=user_menu
        print(usr)
        assert usr == user
    else:
        user_input.send_keys(user)
        pswd_input.send_keys(password)
        login_btn.click()
        assert login_text.text == "Invalid username or password."
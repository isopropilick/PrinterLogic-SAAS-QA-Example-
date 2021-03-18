from selenium import webdriver
import time
import allure
import csv
import pytest

#Test data array creation
user_data=[]
with open("test-data/users.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        user_data.append(row)
    user_data.pop(0)

printer_data=[]
with open("test-data/printers.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        printer_data.append(row)
    printer_data.pop(0)
#Driver initialization
driver = webdriver.Firefox(executable_path="webdriver/gecko/windows_64/geckodriver.exe")
driver.get('https://ericp.printercloud.com/admin/')
#Selectors




#Validate login edge cases
@allure.feature('Log-in window')
@pytest.mark.parametrize('data', user_data)
def test_login(data):
    user=data[0]
    password=data[1]
    global driver
    assert "PrinterLogic" in driver.title
    login_text = driver.find_element_by_xpath("//div[@id='logintext']")
    user_input = driver.find_element_by_xpath("//input[@id='relogin_user']")
    pswd_input = driver.find_element_by_xpath("//input[@id='relogin_password']")
    login_btn = driver.find_element_by_xpath("//button[@id='admin-login-btn']")
    if data[2] == 'pass':
        user_input.send_keys(user)
        pswd_input.send_keys(password)
        login_btn.click()
        time.sleep(5)
        user_menu=driver.find_element_by_xpath("//body[@id='thebody']/div[@id='header']/ul[@id='utility']/li[1]")
        assert user in user_menu.get_attribute("innerHTML")
        user_menu.click()
        time.sleep(1)
        driver.find_element_by_xpath("// a[contains(text(), 'Log Out')]").click()
    else:
        user_input.send_keys(user)
        pswd_input.send_keys(password)
        login_btn.click()
        time.sleep(5)
        assert login_text.text == "Invalid username or password."
        user_input.clear()
        pswd_input.clear()

@allure.feature('Printer creation')
@pytest.mark.parametrize('printers', printer_data)
def test_printer(printers):
    global driver
    printer=printers[0]
    location=printers[1]
    ip=printers[2]
    comment=printers[3]
    user = user_data[0][0]
    password = user_data[0][1]
    driver.find_element_by_xpath("//input[@id='relogin_user']").send_keys(user)
    driver.find_element_by_xpath("//input[@id='relogin_password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='admin-login-btn']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@id='newfolder']").click()
    driver.find_element_by_xpath("//a[@id='addip_link']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='PrinterName']").send_keys(printer)
    driver.find_element_by_xpath("//input[@id='PrinterLocation_popup']").send_keys(location)
    driver.find_element_by_xpath("//input[@id='IPAddress']").send_keys(ip)
    driver.find_element_by_xpath("//input[@id='PrinterComment_popup']").send_keys(comment)
    driver.find_element_by_xpath("//button[@id='add_ip_close']").click()
    print(printer)
    print(user)

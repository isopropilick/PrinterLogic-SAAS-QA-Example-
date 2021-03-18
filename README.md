# Sample QA scrip for PrinterLogic

This PyTest/Selenium script covers the following cases:

* Validate edge cases on yhe login screen (Cap sensitive password, cap insensitive user, wrong user, wrong password)
* Validate the correct storage of the information given in the printer creation form
* Validate the correct date in the printer sumary list
* Validate the functionality of the delete function

## TO-DOs

* Remove implicit waits and replace them with explicit waits
* Create the proper user/password constrains validation test cases
* Create the proper fixtures for Pytest (fixtures to initialize the WebDriver and to manage it)

## Usage

Run `pytest --alluredir=allure-results/` to execute the test cases recovering the execution data in the `allure-results` folder.

Run `allure serve allure-results/` from the project directory in order to build and present the HTML report.

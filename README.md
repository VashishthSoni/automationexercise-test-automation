# Selenium Automation Testing Framework

Automated UI test suite for Automation Exercise using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Reporting

## Test Coverage
### Allure Report:
![Report](https://github.com/VashishthSoni/automationexercise-test-automation/blob/main/utilities/Allure%20Report.png)

✔ User Registration  
✔ Login / Logout  
✔ Product Search  
✔ Cart Operations  
✔ Checkout Flow  
✔ Invoice Download  
✔ Subscription Validation  
✔ Contact Form Validation  

**Total Tests:** 25  
**Status:** 25 Passed

## Run Tests
1. Run Pytest Test
```bash
pytest -v 
```

2. Run Pytest and Generate Allure Report
```bash
pytest --reruns 2 --alluredir=allure-results
allure serve allure-results
```

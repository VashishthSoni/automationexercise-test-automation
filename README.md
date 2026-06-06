# Selenium Automation Testing Framework

Automated UI test suite for Automation Exercise using:

- Python
- Selenium WebDriver
- Pytest
- XPath and CSS Selectors
- Page Object Model (POM)
- Allure Reporting

## Test Coverage
### Allure Report:
![Report](https://github.com/VashishthSoni/automationexercise-test-automation/blob/main/utilities/Allure%20Report.png)

### Test Cases
1. Register User
2. Login User with correct email and password
3. Login User with incorrect email and password
4. Logout User
5. Register User with existing email
6. Contact Us Form
7. Verify Test Cases Page
8. Verify All Products and Product Detail Page
9. Search Product
10. Verify Subscription in Home Page
11. Verify Subscription in Cart Page
12. Add Products in Cart
13. Verify Product Quantity in Cart
14. Place Order: Register While Checkout
15. Place Order: Register Before Checkout
16. Place Order: Login Before Checkout
17. Remove Products From Cart
18. View Category Products
19. View & Cart Brand Products
20. Search Products and Verify Cart After Login
21. Add Review on Product
22. Add to Cart from Recommended Items
23. Verify Address Details in Checkout Page
24. Download Invoice After Purchase Order
25. Verify Scroll Up Using 'Arrow' Button and Scroll Down Functionality
26. Verify Scroll Up Without 'Arrow' Button and Scroll Down Functionality

**Total Tests:** 26  
**Status:** 26 Passed


## Setup
Install project dependencies
```bash
pip install -r requirements.txt
```

## Run Tests
1. Run All Pytest Tests
```bash
pytest -v 
```

2. Run Pytest and Generate Allure Report
```bash
pytest --reruns 2 --alluredir=allure-results
allure serve allure-results
```

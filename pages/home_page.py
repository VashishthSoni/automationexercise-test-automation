from selenium.webdriver.common.by import By

class HomePage:
    signup_login_btn = (By.LINK_TEXT, "Signup / Login")
    contact_us_btn = (By.XPATH,"//a[contains(.,'Contact us')]")
    test_case_btn = (By.XPATH,"//a[contains(.,'Test Cases')]")
    products_page_btn = (By.XPATH,"//a[@href='/products']")
    cart_page_btn = (By.XPATH,"//a[@href='/view_cart']")
    delete_btn = (By.XPATH, "//a[@href='/delete_account']")
    
    def __init__(self, driver):
        self.driver = driver

    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_btn).click()
    
    def click_contact_us(self):
        self.driver.find_element(*self.contact_us_btn).click()
    
    def click_test_cases_page(self):
        self.driver.find_element(*self.test_case_btn).click()
        
    def click_products(self):
        self.driver.find_element(*self.products_page_btn).click()
    
    def click_cart(self):
        self.driver.find_element(*self.cart_page_btn).click()
    
    def click_delete_account(self):
        self.driver.find_element(*self.delete_btn).click()
    
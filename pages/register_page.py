from selenium.webdriver.common.by import By


class RegisterPage:
    name = (By.NAME,"name")
    email = (By.XPATH,"//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH,"//button[@data-qa='signup-button']")
    
    password = (By.ID, "password")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")
    
    create_account_btn = (By.XPATH,"//button[@data-qa='create-account']")
    continue_btn = (By.XPATH,"//a[@data-qa='continue-button']")
    delete_account_btn = (By.LINK_TEXT, "Delete Account")
    
    def __init__(self, driver):
        self.driver = driver

    def enter_signup_details(self, name, email):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
    

    def click_signup(self):
        self.driver.find_element(*self.signup_btn).click()
        
    def fill_account_info(self):
        self.driver.find_element(*self.password).send_keys("Test@123")
        self.driver.find_element(*self.first_name).send_keys("Test")
        self.driver.find_element(*self.last_name).send_keys("User")
        self.driver.find_element(*self.address).send_keys("Street 1")
        self.driver.find_element(*self.state).send_keys("Gujarat")
        self.driver.find_element(*self.city).send_keys("Ahmedabad")
        self.driver.find_element(*self.zipcode).send_keys("380001")
        self.driver.find_element(*self.mobile).send_keys("9999999999")
    
    def create_account(self):
        self.driver.find_element(*self.create_account_btn).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def delete_account(self):
        self.driver.find_element(*self.delete_account_btn).click()
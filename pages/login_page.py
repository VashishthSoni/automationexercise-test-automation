from selenium.webdriver.common.by import By
class LoginPage:
    email = (By.XPATH,"//input[@data-qa='login-email']") 
    password = (By.XPATH,"//input[@data-qa='login-password']") 
    
    login_btn = (By.XPATH,"//button[@data-qa='login-button']") 
    delete_account_btn = (By.LINK_TEXT, "Delete Account")

    def __init__(self, driver):
        self.driver = driver
        
    def fill_details(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
        
    def delete_account(self):
        self.driver.find_element(*self.delete_account_btn).click()
import os
from selenium.webdriver.common.by import By

class ContactUs:
    name = (By.NAME,'name')
    email = (By.NAME,'email')
    subject = (By.NAME,'subject')
    message = (By.ID,'message')
    file = (By.NAME,'upload_file')
    
    submit_btn = (By.NAME, 'submit')
    home_btn = (By.XPATH,"//span[contains(.,'Home')]")
    def __init__(self, driver):
        self.driver = driver
        
    def fill_form(self):
        self.driver.find_element(*self.name).send_keys("Test User")
        self.driver.find_element(*self.email).send_keys("testuser123@gmail.com")
        self.driver.find_element(*self.subject).send_keys("Inquiry About Product Features")
        self.driver.find_element(*self.message).send_keys("Hello, I am testing the contact us form submission functionality for automation purposes. Please ignore this message. Thank you.")
        self.driver.find_element(*self.file).send_keys(os.path.abspath("utilities/demo.txt"))
    
    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()
    
    def click_ok(self):
        self.driver.switch_to.alert.accept()
        
    def click_home(self):
        self.driver.find_element(*self.home_btn).click()
 
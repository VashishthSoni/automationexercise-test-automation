from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    proceed_checkout = (By.XPATH,"//a[@class='btn btn-default check_out']")
    register_login_popup = (By.XPATH,"//u[text()='Register / Login']/parent::a")
    comment_text_area = (By.XPATH,"//textarea[@name='message']")
    place_order_btn = (By.XPATH,"//a[@href='/payment']")
    remove_product_btn = (By.XPATH, "(//a[@class='cart_quantity_delete'])[1]")
    click_pay_btn = (By.ID,"submit")
    name = (By.NAME,"name_on_card")
    card_number = (By.NAME,"card_number")
    cvc = (By.NAME,"cvc")
    expiration_month = (By.NAME,"expiry_month")
    expiration_year= (By.NAME,"expiry_year")
    invoice_btn = (By.LINK_TEXT,"Download Invoice")
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_checkout(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.proceed_checkout)
        )
        button.click()
        
        
    def click_register_login_in_popup(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.register_login_popup)
        )
        button.click()
    
    def write_comment(self):
        self.driver.find_element(*self.comment_text_area).send_keys("Avoid Ringing Bell, Leave parcel to guard")
        
    def click_place_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.place_order_btn)
        ).click()
    
    def fill_cc_details(self):
        self.driver.find_element(*self.name).send_keys("Test User")
        self.driver.find_element(*self.card_number).send_keys("1234 5678 9123 4566")
        self.driver.find_element(*self.cvc).send_keys("111")
        self.driver.find_element(*self.expiration_month).send_keys("10")
        self.driver.find_element(*self.expiration_year).send_keys("31")
    
    def click_pay(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_pay_btn)
        ).click()
        
    def remove_product_from_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_product_btn)
        ).click()
    
    def download_invoice(self):
        self.driver.find_element(*self.invoice_btn).click()


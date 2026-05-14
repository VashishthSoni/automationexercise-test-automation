from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    
    search_input = (By.ID,'search_product')
    search_btn = (By.ID,'submit_search')
    continue_shopping_btn = (By.XPATH,"//button[@class='btn btn-success close-modal btn-block']")
    view_cart_btn = (By.XPATH,"//a[@href='/view_cart']")
    
    review_name = (By.ID,"name")
    review_email = (By.ID,"email")
    review_review = (By.ID,"review")
    submit_review_btn = (By.ID,"button-review")
    
    def __init__(self,driver):
        self.driver = driver
        
    def select_product(self,index):
        if index > 0:
            self.driver.find_element(By.XPATH,f"//a[@href='/product_details/{index}']").click()

    def search(self,query):
        self.driver.find_element(*self.search_input).send_keys(query)
        self.driver.find_element(*self.search_btn).click()
        
    def hover_and_click_product(self, index):
        element = self.driver.find_element(By.XPATH,f"//a[@href='/product_details/{index}']")
        ActionChains(self.driver).move_to_element(element).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@data-product-id='{index}']"))
        ).click()
        
    def click_continue_shopping(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_shopping_btn)
        )
        button.click()
        
    def click_view_cart_dismissal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_cart_btn)
        ).click()
    
    def click_category(self, category):
        locator = (By.XPATH, f"//div[@id='accordian']//a[contains(text(),'{category}')]")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def click_category_product(self, category, subcategory):
        locator = (By.XPATH, f"//div[@id='{category}']//a[contains(text(),'{subcategory}')]")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def view_product(self,index):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,f"//a[@href='/product_details/{index}']"))
        ).click()
        
    def write_review(self):
        self.driver.find_element(*self.review_name).send_keys("Test User 1")
        self.driver.find_element(*self.review_email).send_keys("Testuser@testuser.com")
        self.driver.find_element(*self.review_review).send_keys("Good Product, A color was bit off and different. Otherwise comfortable and great design.")
    
    def submit_review(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_review_btn)
        )
        button.click()
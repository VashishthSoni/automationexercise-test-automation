import time
from pages.home_page import HomePage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from pages.products_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remove_product_from_cart(driver):
    homepage = HomePage(driver)
    assert "https://automationexercise.com/" in driver.current_url    
    
    homepage.click_products()
    time.sleep(4)
    productPage = ProductPage(driver)
    productPage.hover_and_click_product(1)
    productPage.click_continue_shopping()

    driver.find_element(By.XPATH,"//a[@href='/view_cart']").click()
    
    cartPage = CartPage(driver)
    cartPage.remove_product_from_cart()

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//b[contains(.,'Cart is empty!')]")
        )
    )
    assert "Cart is empty!".upper() in driver.find_element(By.XPATH,"//b[contains(.,'Cart is empty!')]").text.upper()
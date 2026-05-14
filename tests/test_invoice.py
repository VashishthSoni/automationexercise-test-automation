import time
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from pages.products_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_download_invoice(driver):
    homepage = HomePage(driver)
    homepage.click_signup_login()
    
    signup = RegisterPage(driver)
    signup.enter_signup_details(name="TestUser1",email=f"TestUser{int(time.time())}@test.com")
    
    signup.click_signup()
    
    
    assert "Enter Account Information".upper() in driver.find_element(By.XPATH,"//b[contains(text(),'Enter Account Information')]").text.upper()
    time.sleep(3)
    signup.fill_account_info()
    signup.create_account()
    
    
    acc = driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
    assert "ACCOUNT CREATED!" in acc.upper()
    
    signup.click_continue()
    
    
    check_Login = driver.find_element(By.XPATH,"//a[contains(.,'Logged in as')]").text
    assert "Logged in as" in check_Login
    
    homepage.click_products()
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='All Products']")
        )
    )
    time.sleep(4)
    
    productPage = ProductPage(driver)
    productPage.hover_and_click_product(1)
    productPage.click_continue_shopping()

    driver.find_element(By.XPATH,"//a[@href='/view_cart']").click()
    
    
    cartPage = CartPage(driver)
    cartPage.click_checkout()
    time.sleep(2)    
    
    assert 'Your delivery address'.upper() in driver.find_element(By.XPATH,"//h3[contains(.,'Your delivery address')]").text.upper()
    cartPage.write_comment()
    cartPage.click_place_order()
    
    cartPage.fill_cc_details()
    time.sleep(2)
    cartPage.click_pay()
    wait.until(EC.url_contains("payment_done"))
    
    confirmation = driver.find_element(By.XPATH,"//b[contains(.,'Order Placed!')]").text
    assert "Order Placed!".upper() in confirmation.upper()

    cartPage.download_invoice()
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
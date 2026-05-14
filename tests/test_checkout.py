import time
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.products_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def signup_helper(driver):
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
    
    return signup
    
def complete_payment_helper(cartPage, wait):
    cartPage.write_comment()
    cartPage.click_place_order()
    cartPage.fill_cc_details()
    time.sleep(2)
    cartPage.click_pay()
    wait.until(EC.url_contains("payment_done"))

def test_register_while_checkout(driver):
    homepage = HomePage(driver)
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
    cartPage.click_register_login_in_popup()
    
    signup = signup_helper(driver)
    
    homepage.click_cart()
    cartPage.click_checkout()
    assert 'Your delivery address'.upper() in driver.find_element(By.XPATH,"//h3[contains(.,'Your delivery address')]").text.upper()

    complete_payment_helper(cartPage,wait)
    
    confirmation = driver.find_element(By.XPATH,"//b[contains(.,'Order Placed!')]").text
    assert "Order Placed!".upper() in confirmation.upper()

    signup.delete_account()
    deleted = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[contains(text(),'Account Deleted!')]")
        )
    ).text
    assert "ACCOUNT DELETED!" in deleted.upper()
    
def test_register_before_checkout(driver):
    homepage = HomePage(driver)
    homepage.click_signup_login()
    
    signup = signup_helper(driver)
        
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
    complete_payment_helper(cartPage,wait)

    confirmation = driver.find_element(By.XPATH,"//b[contains(.,'Order Placed!')]").text
    assert "Order Placed!".upper() in confirmation.upper()

    signup.delete_account()
    deleted = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[contains(text(),'Account Deleted!')]")
        )
    ).text
    assert "ACCOUNT DELETED!" in deleted.upper()
    
def test_login_before_checkout(driver):
    homepage = HomePage(driver)
    homepage.click_signup_login()
    assert_login = driver.find_element(By.XPATH,"//h2[text()='Login to your account']").text
    assert "Login to your account" in assert_login
    
    login = LoginPage(driver) 
    login.fill_details(email='TestUser112@testuser.com',password='Test@123')    
    login.click_login()
    
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
    
    complete_payment_helper(cartPage,wait)
    
    confirmation = driver.find_element(By.XPATH,"//b[contains(.,'Order Placed!')]").text
    assert "Order Placed!".upper() in confirmation.upper()
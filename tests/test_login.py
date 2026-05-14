from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_user(driver):
    home = HomePage(driver)
    home.click_signup_login()
    assert_login = driver.find_element(By.XPATH,"//h2[text()='Login to your account']").text
    assert "Login to your account" in assert_login
    
    login = LoginPage(driver) 
    login.fill_details(email='TestUser112@testuser.com',password='Test@123')    

    login.click_login()
    
    check_Login = driver.find_element(By.XPATH,"//a[contains(.,'Logged in as')]").text
    assert "Logged in as" in check_Login
    

def test_login_fail(driver):
    home = HomePage(driver)
    home.click_signup_login()
    assert_login = driver.find_element(By.XPATH,"//h2[text()='Login to your account']").text
    assert "Login to your account" in assert_login
    
    login = LoginPage(driver) 
    login.fill_details(email='wrong@test.com',password='wrong@123456')    
    login.click_login()
    
    check_login = driver.find_element(By.XPATH,"//p[text()='Your email or password is incorrect!']").text
    assert 'Your email or password is incorrect!' in check_login
    
def test_logout(driver):
    home = HomePage(driver)
    home.click_signup_login()
    assert_login = driver.find_element(By.XPATH,"//h2[text()='Login to your account']").text
    assert "Login to your account" in assert_login
    
    login = LoginPage(driver) 
    login.fill_details(email='TestUser112@testuser.com',password='Test@123')    
    login.click_login()
    
    check_Login = driver.find_element(By.XPATH,"//a[contains(.,'Logged in as')]").text
    assert "Logged in as" in check_Login
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    ).click()
    
    assert "login" in driver.current_url
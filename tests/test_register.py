import time
from pages.register_page import RegisterPage    
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_register_user(driver):
    assert "Automation Exercise" in driver.title
    
    home = HomePage(driver)
    home.click_signup_login()
    
    signup = RegisterPage(driver)
    signup.enter_signup_details(name="TestUser1",email=f"TestUser{int(time.time())}@test.com")
    
    signup.click_signup()
        
    assert "Enter Account Information" in driver.page_source
    signup.fill_account_info()
    signup.create_account()
    
    acc = driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
    assert "ACCOUNT CREATED!" in acc
    
    signup.click_continue()

    check_Login = driver.find_element(By.XPATH,"//a[contains(.,'Logged in as')]").text
    assert "Logged in as" in check_Login
        
    signup.delete_account() 
    check_delete = driver.find_element(By.XPATH,"//b[text()='Account Deleted!']").text
    assert "ACCOUNT DELETED!" in check_delete

def test_register_existing_user(driver):
    homepage = HomePage(driver)
    homepage.click_signup_login()
    assert 'New User Signup' in driver.find_element(By.XPATH,"//h2[text()='New User Signup!']").text        
    
    signup = RegisterPage(driver)
    signup.enter_signup_details(name='Test', email='TestUser112@testuser.com')
    signup.click_signup()
    
    assert 'Email Address already exist!' in driver.find_element(By.XPATH,"//p[text()='Email Address already exist!']").text

def test_scroll_up_using_arrow(driver):
    homepage = HomePage(driver)
    assert "Automation Exercise" in driver.title

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    subscription = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Subscription')]")
        )
    )

    assert "SUBSCRIPTION" in subscription.text.upper()

    arrow = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "scrollUp")
        )
    )
    arrow.click()

    top_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Full-Fledged practice website for Automation Engineers')]")
        )
    )

    assert "FULL-FLEDGED PRACTICE WEBSITE FOR AUTOMATION ENGINEERS" in top_text.text.upper()
    
def test_scroll_up_without_arrow(driver):
    homepage = HomePage(driver)
    assert "Automation Exercise" in driver.title

    wait = WebDriverWait(driver, 10)
    
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    subscription = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Subscription')]")
        )
    )

    assert "SUBSCRIPTION" in subscription.text.upper()

    time.sleep(3)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)

    top_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Full-Fledged practice website for Automation Engineers')]")
        )
    )

    assert "FULL-FLEDGED PRACTICE WEBSITE FOR AUTOMATION ENGINEERS" in top_text.text.upper()
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_subscription_homepage(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    
    subscription_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='Subscription']")
        )
    )
    assert 'SUBSCRIPTION' in subscription_text.text.upper()
    
    driver.find_element(By.ID,'susbscribe_email').send_keys('testuser1@testauto.com')
    driver.find_element(By.ID, "subscribe").click()

    success_msg = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'You have been successfully subscribed!')]")
        )
    )

    assert "You have been successfully subscribed!" in success_msg.text

def test_subscription_cartpage(driver):
    wait = WebDriverWait(driver, 10)
    
    homepage = HomePage(driver)
    homepage.click_cart()
    
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    subscription_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='Subscription']")
        )
    )
    assert 'SUBSCRIPTION' in subscription_text.text.upper()
    
    driver.find_element(By.ID,'susbscribe_email').send_keys('testuser1@testauto.com')
    driver.find_element(By.ID, "subscribe").click()

    success_msg = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'You have been successfully subscribed!')]")
        )
    )
    assert "You have been successfully subscribed!" in success_msg.text
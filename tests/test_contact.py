import time
from pages.home_page import HomePage
from pages.ContactUs import ContactUs
from selenium.webdriver.common.by import By

def test_contact_us(driver):
    homepage = HomePage(driver)
    homepage.click_contact_us()
    assert 'GET IN TOUCH' in driver.find_element(By.XPATH,"//h2[text()='Get In Touch']").text.upper()
    time.sleep(5)
    contact_us = ContactUs(driver)
    contact_us.fill_form()
    
    contact_us.click_submit()
    time.sleep(3)
    
    contact_us.click_ok()
    assert "Success! Your details have been submitted successfully" in driver.find_element(By.XPATH,"//div[@class='status alert alert-success']").text
    
    
    contact_us.click_home()
    assert 'https://automationexercise.com/' in driver.current_url


def test_testcase_page(driver):
    homepage = HomePage(driver)
    
    homepage.click_test_cases_page()
    
    assert 'TEST CASES' in driver.find_element(By.XPATH,"//b[text()='Test Cases']").text.upper()
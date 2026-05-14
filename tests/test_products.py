from pages.home_page import HomePage
import time
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from pages.products_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

def test_verify_products_and_details(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    wait = WebDriverWait(driver, 10)

    all_products = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='All Products']")
        )
    )

    assert all_products.text == "ALL PRODUCTS"

    productPage = ProductPage(driver)
    time.sleep(5)
    productPage.select_product(1)
    
    wait.until(EC.url_contains("product_details"))
    assert "product_details" in driver.current_url
    assert "Rs." in wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Rs.')]")
        )
    ).text

    assert "Category" in driver.find_element(By.XPATH, "//p[contains(.,'Category')]").text
    assert "Availability" in driver.find_element(By.XPATH, "//b[contains(.,'Availability')]").text
    assert "Condition" in driver.find_element(By.XPATH, "//b[contains(.,'Condition')]").text
    assert "Brand" in driver.find_element(By.XPATH, "//b[contains(.,'Brand')]").text

def test_search_products(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    wait = WebDriverWait(driver, 10)

    all_products = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='All Products']")
        )
    )

    assert all_products.text == "ALL PRODUCTS"
    
    productpage = ProductPage(driver)
    productpage.search("Top")
    
    search_products =  wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,"//h2[text()='Searched Products']")
        )
    ).text
    
    assert 'SEARCHED PRODUCTS' in search_products

def test_add_product_to_cart(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    time.sleep(4)
    productpage = ProductPage(driver)
    productpage.hover_and_click_product(1)
    
    productpage.click_continue_shopping()
    
    productpage.hover_and_click_product(2)
    
    productpage.click_view_cart_dismissal()
        
    products = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")
    assert len(products) == 2
    
    price1 = driver.find_element(By.XPATH,"(//td[@class='cart_price']/p)[1]").text
    price2 = driver.find_element(By.XPATH,"(//td[@class='cart_price']/p)[2]").text

    assert "Rs." in price1
    assert "Rs." in price2

    # Verify quantity
    qty1 = driver.find_element(By.XPATH,"(//button[@class='disabled'])[1]").text
    qty2 = driver.find_element(By.XPATH,"(//button[@class='disabled'])[2]").text

    assert qty1 == "1"
    assert qty2 == "1"

    # Verify total
    total1 = driver.find_element(By.XPATH,"(//td[@class='cart_total']/p)[1]").text
    total2 = driver.find_element(By.XPATH,"(//td[@class='cart_total']/p)[2]").text

    assert "Rs." in total1
    assert "Rs." in total2
    
def test_product_quantity(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    wait = WebDriverWait(driver, 10)
    time.sleep(4)
    productpage = ProductPage(driver)
    for i in range(4):
        productpage.hover_and_click_product(1)
        if i == 3:
            productpage.click_view_cart_dismissal()
            break
        
        productpage.click_continue_shopping()
    
    
    quantity = driver.find_element(By.XPATH,"(//button[@class='disabled'])[1]").text
    
    assert quantity == "4"

def test_view_category_products(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    wait = WebDriverWait(driver, 10)
    time.sleep(4)
    
    # Verify categories sidebar visible
    assert "BRANDS" in driver.find_element(By.XPATH,"//h2[text()='Brands']").text.upper()
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//a[@href='/brand_products/Polo']")
        )
    ).click()
    time.sleep(3)
    assert "brand_products/Polo" in driver.current_url
    assert "Brand - Polo Products".upper() in driver.find_element(By.XPATH,"//h2[contains(.,'Brand - Polo Products')]").text.upper()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//a[@href='/brand_products/H&M']")
        )
    ).click()
    time.sleep(3)
    assert "brand_products/H&M" in driver.current_url
    assert "Brand - H&M Products".upper() in driver.find_element(By.XPATH,"//h2[contains(.,'Brand - H&M Products')]").text.upper()
    
def test_search_product_and_cart(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    wait = WebDriverWait(driver, 10)
    time.sleep(4)
    
    product_page = ProductPage(driver)
    assert "BRANDS" in driver.find_element(By.XPATH,"//h2[text()='Brands']").text.upper()
    time.sleep(4)
    product_page.search("Dress")
    search_products =  wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,"//h2[text()='Searched Products']")
        )
    ).text
    assert 'SEARCHED PRODUCTS' in search_products
    
    products = driver.find_elements(By.CLASS_NAME,"product-image-wrapper")
    time.sleep(3)
    for i in range(0,len(products)):
        products[i].find_element(By.XPATH,".//a[@class='btn btn-default add-to-cart']").click()
        product_page.click_continue_shopping()
        time.sleep(1)
    
    homepage.click_cart()
    time.sleep(1)
    assert len(products) == len(driver.find_elements(By.XPATH,"//tr[contains(@id,'product')]"))
    
    driver.find_element(By.XPATH,"//a[@href='/login']").click()
    loginpage = LoginPage(driver)
    loginpage.fill_details(email='TestUser112@testuser.com',password='Test@123')
    loginpage.click_login()
    check_Login = driver.find_element(By.XPATH,"//a[contains(.,'Logged in as')]").text
    assert "Logged in as" in check_Login
    
    homepage.click_cart()
    time.sleep(1)
    assert len(products) == len(driver.find_elements(By.XPATH,"//tr[contains(@id,'product')]"))

def test_write_review(driver):
    homepage = HomePage(driver)
    homepage.click_products()

    time.sleep(4)
    
    product_page = ProductPage(driver)
    assert "BRANDS" in driver.find_element(By.XPATH,"//h2[text()='Brands']").text.upper()
    time.sleep(4)
    product_page.view_product(1)
    
    assert "Write Your Review".upper() in driver.find_element(By.XPATH,"//a[text()='Write Your Review']").text.upper()
    
    product_page.write_review()
    product_page.submit_review()
    
    assert "Thank you for your review.".upper() in driver.find_element(By.XPATH,"//div[@class='alert-success alert']/span").text.upper()
    
def test_recommended_products(driver):
    homepage = HomePage(driver)
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    recommended_header = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(.,'recommended items')]")
        )
    )

    assert "RECOMMENDED ITEMS" in recommended_header.text.upper()

    recommended_items = driver.find_element(
        By.XPATH,
        "//div[@class='recommended_items']"
    )

    recommended_items.find_element(
        By.XPATH,
        ".//a[@data-product-id='1']"
    ).click()
    
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success close-modal btn-block']"))
    ).click()
    homepage.click_cart()
    
    time.sleep(2)
    
    product_rows = driver.find_elements(
        By.XPATH,
        "//tr[contains(@id,'product')]"
    )
    assert len(product_rows) > 0

def test_verify_address_checkout(driver):
    
    assert "Automation Exercise" in driver.title

    homepage = HomePage(driver)
    homepage.click_signup_login()
    
    signup_helper(driver)
    homepage.click_products()
    time.sleep(5)
    productPage = ProductPage(driver)
    productPage.hover_and_click_product(1)
    productPage.click_view_cart_dismissal()
    
    cartpage = CartPage(driver)
    cartpage.click_checkout()
    time.sleep(1)
    
    delivery = driver.find_element(
        By.XPATH,
        "//h3[contains(.,'Your delivery address')]"
    ).text

    assert "Your delivery address".upper() in delivery.upper()

    billing = driver.find_element(
        By.XPATH,
        "//h3[contains(.,'Your billing address')]"
    ).text

    assert "Your billing address".upper() in billing.upper()
    
    homepage.click_delete_account()
    
    check_delete = driver.find_element(By.XPATH,"//b[text()='Account Deleted!']").text
    assert "ACCOUNT DELETED!" in check_delete
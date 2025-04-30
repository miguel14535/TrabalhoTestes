import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os
import random

class DemoBlazeTest(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test method."""
        self.start_time = datetime.now()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        
    def test_004_purchase_flow(self):
        """TC-004: Test the complete purchase flow of a product."""
        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card"))
        )
        
        # Select a random product from the list
        products = self.driver.find_elements(By.CLASS_NAME, "card")
        random_product = random.choice(products)
        product_name = random_product.find_element(By.CLASS_NAME, "card-title").text
        print(f"Selected product: {product_name}")
        random_product.click()
        
        # Wait for product page to load and click Add to Cart
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add to cart')]"))
        ).click()
        
        # Handle alert - wait for it and accept
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted")
        except TimeoutException:
            print("No alert appeared")
        
        # Go to Cart
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cartur"))
        ).click()
        
        # Wait for cart page to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "success"))
        )
        
        # Verify product is in cart
        cart_items = self.driver.find_elements(By.XPATH, "//tr[@class='success']")
        self.assertGreater(len(cart_items), 0, "No items in cart")
        
        # Click Place Order
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
        ).click()
        
        # Wait for the order form to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        )
        
        # Fill out the form
        self.driver.find_element(By.ID, "name").send_keys("Test User")
        self.driver.find_element(By.ID, "country").send_keys("Test Country")
        self.driver.find_element(By.ID, "city").send_keys("Test City")
        self.driver.find_element(By.ID, "card").send_keys("4111111111111111")
        self.driver.find_element(By.ID, "month").send_keys("12")
        self.driver.find_element(By.ID, "year").send_keys("2025")
        
        # Submit the form
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Purchase')]"))
        ).click()
        
        # Wait for confirmation and get the confirmation details
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you')]"))
        )
        
        confirmation_text = self.driver.find_element(By.CLASS_NAME, "sweet-alert").text
        
        # Extract order ID and amount
        import re
        order_id_match = re.search(r"Id: (\d+)", confirmation_text)
        amount_match = re.search(r"Amount: (\d+) USD", confirmation_text)
        
        order_id = order_id_match.group(1) if order_id_match else "Not found"
        amount = amount_match.group(1) if amount_match else "Not found"
        
        print(f"Order ID: {order_id}")
        print(f"Amount: {amount} USD")
        
        # Take screenshot
        os.makedirs('../relatorios/screenshots', exist_ok=True)
        self.driver.save_screenshot("../relatorios/screenshots/tc_004_confirmation.png")
        
        # Save results for the report
        with open("../relatorios/tc_004_results.txt", "w") as f:
            f.write(f"Product purchased: {product_name}\n")
            f.write(f"Order ID: {order_id}\n")
            f.write(f"Amount: {amount} USD\n")
            f.write(f"Full confirmation message:\n{confirmation_text}\n")
            f.write("Test result: Passed\n")
        
        # Assert that confirmation contains "Thank you"
        self.assertIn("Thank you", confirmation_text)
    
    def tearDown(self):
        """Clean up after each test method."""
        self.end_time = datetime.now()
        self.execution_time = self.end_time - self.start_time
        print(f"Test execution time: {self.execution_time}")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
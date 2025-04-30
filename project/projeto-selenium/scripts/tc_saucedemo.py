import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os

class SauceDemoTest(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test method."""
        self.start_time = datetime.now()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def test_001_login_successful(self):
        """TC-001: Test successful login with standard user."""
        # Locate username and password fields
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        # Input credentials
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        
        # Click login button
        login_button.click()
        
        # Verify successful login by checking URL and inventory container
        current_url = self.driver.current_url
        inventory_container = self.driver.find_element(By.ID, "inventory_container")
        
        # Assert test conditions
        self.assertTrue("inventory.html" in current_url)
        self.assertTrue(inventory_container.is_displayed())
        
        # Save screenshot for report
        os.makedirs('../relatorios/screenshots', exist_ok=True)
        self.driver.save_screenshot("../relatorios/screenshots/tc_001_success.png")
        
    def test_002_login_unsuccessful(self):
        """TC-002: Test unsuccessful login with invalid credentials."""
        # Locate username and password fields
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        # Input invalid credentials
        username_field.send_keys("invalid_user")
        password_field.send_keys("wrong_password")
        
        # Click login button
        login_button.click()
        
        # Check for error message
        error_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        error_message = error_container.text
        
        # Assert test conditions
        self.assertTrue(error_container.is_displayed())
        self.assertTrue("Epic sadface" in error_message)
        
        # Save screenshot for report
        os.makedirs('../relatorios/screenshots', exist_ok=True)
        self.driver.save_screenshot("../relatorios/screenshots/tc_002_failure.png")
    
    def tearDown(self):
        """Clean up after each test method."""
        self.end_time = datetime.now()
        self.execution_time = self.end_time - self.start_time
        print(f"Test execution time: {self.execution_time}")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
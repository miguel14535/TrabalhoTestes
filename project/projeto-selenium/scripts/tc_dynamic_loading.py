import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os

class DynamicLoadingTest(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test method."""
        self.start_time = datetime.now()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading")
        
    def test_003_wait_for_element(self):
        """TC-003: Test waiting for an element to appear after clicking a button."""
        # Click on the Example 1 link
        example_link = self.driver.find_element(By.XPATH, "//a[contains(@href, 'elements/1')]")
        example_link.click()
        
        # Locate and click the start button
        start_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
        start_button.click()
        
        wait_start_time = time.time()
        
        try:
            # Wait for the text to appear with a timeout of 30 seconds
            wait = WebDriverWait(self.driver, 30)
            hello_text = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
            )
            
            wait_end_time = time.time()
            wait_duration = wait_end_time - wait_start_time
            
            # Assert test conditions
            self.assertTrue(hello_text.is_displayed())
            self.assertEqual(hello_text.text, "Hello World!")
            
            # Log the wait time
            print(f"Wait duration: {wait_duration} seconds")
            
            # Save screenshot for report
            os.makedirs('../relatorios/screenshots', exist_ok=True)
            self.driver.save_screenshot("../relatorios/screenshots/tc_003_success.png")
            
            # Save the results to use in the report
            with open("../relatorios/tc_003_results.txt", "w") as f:
                f.write(f"Wait duration: {wait_duration:.2f} seconds\n")
                f.write(f"Text displayed: {hello_text.text}\n")
                f.write("Test result: Passed\n")
                
        except Exception as e:
            wait_end_time = time.time()
            wait_duration = wait_end_time - wait_start_time
            
            # Log the error
            print(f"Error: {str(e)}")
            print(f"Wait duration before error: {wait_duration} seconds")
            
            # Save screenshot for report
            os.makedirs('../relatorios/screenshots', exist_ok=True)
            self.driver.save_screenshot("../relatorios/screenshots/tc_003_failure.png")
            
            # Save the results to use in the report
            with open("../relatorios/tc_003_results.txt", "w") as f:
                f.write(f"Wait duration: {wait_duration:.2f} seconds\n")
                f.write(f"Error: {str(e)}\n")
                f.write("Test result: Failed\n")
                
            # Re-raise the exception to fail the test
            raise
    
    def tearDown(self):
        """Clean up after each test method."""
        self.end_time = datetime.now()
        self.execution_time = self.end_time - self.start_time
        print(f"Test execution time: {self.execution_time}")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os

class FormyTest(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test method."""
        self.start_time = datetime.now()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/form")
        
    def test_005_form_submission(self):
        """TC-005: Test form filling and submission."""
        # Dictionary to store all form field values for reporting
        form_values = {}
        
        # Fill personal information
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        form_values["First Name"] = "John"
        
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Doe")
        form_values["Last Name"] = "Doe"
        
        job_title = self.driver.find_element(By.ID, "job-title")
        job_title.send_keys("QA Engineer")
        form_values["Job Title"] = "QA Engineer"
        
        # Select education level (radio button)
        college_radio = self.driver.find_element(By.ID, "radio-button-2")
        college_radio.click()
        form_values["Education"] = "College"
        
        # Select gender (checkbox)
        male_checkbox = self.driver.find_element(By.ID, "checkbox-1")
        male_checkbox.click()
        form_values["Gender"] = "Male"
        
        # Select experience using select dropdown
        experience_select = Select(self.driver.find_element(By.ID, "select-menu"))
        experience_select.select_by_visible_text("2-4")
        form_values["Years of Experience"] = "2-4"
        
        # Fill date
        date_field = self.driver.find_element(By.ID, "datepicker")
        date_field.send_keys("12/25/2023")
        form_values["Date"] = "12/25/2023"
        
        # Take screenshot before submission
        os.makedirs('../relatorios/screenshots', exist_ok=True)
        self.driver.save_screenshot("../relatorios/screenshots/tc_005_before_submit.png")
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
        submit_button.click()
        
        # Wait for the success message
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert"))
        )
        
        # Get the success message
        alert = self.driver.find_element(By.CLASS_NAME, "alert")
        alert_text = alert.text
        
        # Take screenshot after submission
        self.driver.save_screenshot("../relatorios/screenshots/tc_005_after_submit.png")
        
        # Assert the success message
        self.assertEqual(alert_text, "The form was successfully submitted!")
        
        # Save results for the report
        with open("../relatorios/tc_005_results.txt", "w") as f:
            f.write("Form Field Values:\n")
            for key, value in form_values.items():
                f.write(f"{key}: {value}\n")
            f.write(f"\nSuccess Message: {alert_text}\n")
            f.write("Test result: Passed\n")
    
    def tearDown(self):
        """Clean up after each test method."""
        self.end_time = datetime.now()
        self.execution_time = self.end_time - self.start_time
        print(f"Test execution time: {self.execution_time}")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
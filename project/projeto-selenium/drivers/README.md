# WebDrivers Directory

This directory is intended for storing WebDriver executables required for Selenium to interact with different browsers.

## Supported Drivers

- ChromeDriver: For Google Chrome browser
- GeckoDriver: For Mozilla Firefox browser

## Automatic WebDriver Management

In our test scripts, we're using the `webdriver_manager` package to automatically download and manage the correct WebDriver versions. This means you don't need to manually download and place the WebDriver executables in this directory.

The `webdriver_manager` will:

1. Check the version of your installed browser
2. Download the compatible WebDriver if it's not already installed
3. Set up the WebDriver service with the correct path

## Manual WebDriver Installation (Optional)

If you prefer to manage WebDrivers manually or if you're working in an environment where automatic downloads are restricted, you can download the WebDrivers yourself and place them in this directory:

- ChromeDriver: https://chromedriver.chromium.org/downloads
- GeckoDriver: https://github.com/mozilla/geckodriver/releases

After downloading, ensure the WebDriver executables are in your system PATH or update the test scripts to use the specific path to your WebDriver executables.

## Configuration

If you need to use a specific WebDriver version or location, you can modify the setup code in each test script:

```python
# Using webdriver_manager (automatic)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Using manual WebDriver path
driver = webdriver.Chrome(service=Service("./drivers/chromedriver"))
```

## Troubleshooting

If you encounter WebDriver issues:

1. Ensure your browser is up to date
2. Try removing the cached WebDrivers to force a fresh download
3. Check for any browser-specific security settings blocking WebDriver execution
4. Verify that the WebDriver version matches your browser version
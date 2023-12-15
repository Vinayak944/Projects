from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open a website (for example, Google)
driver.get("https://www.google.com")

# Wait for a bit (optional)
# You can use this to see if the browser opens and navigates correctly
import time
time.sleep(5)  # Waits for 5 seconds

# Close the browser window
driver.quit()

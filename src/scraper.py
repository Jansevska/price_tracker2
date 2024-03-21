# scraper.py: Contains the web scraping logic that retrieves the current price of the iPad from Amazon.
# The scraper.py will use Selenium to navigate to the Amazon page and scrape the current iPad price.
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()

# Set the desired User-Agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
options.add_argument(f'user-agent={USER_AGENT}')

# Additional arguments as needed
options.add_argument('--headless')  # Run Chrome in headless mode (optional)
options.add_argument('--disable-gpu')  # Disable GPU (optional)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


# Set up the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #

# Open the webpage
driver.get("https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=sr_1_1_sspa?crid=3C0GSCZB3YQT0&dib=eyJ2IjoiMSJ9.x37hw5scXMlLBGdXY-8OgxwwuwjAPTL4jNHENCjqcExH989sluaQy0tIFSlqwVR48sM9_2aseELA75AW6epEe9lk7KNkLsp_WddTB4S0X1SCyAB28YkWcf50Kpxl5TOPtxRWIyLU8MhrWHrx8EqrbN3xq5cKZKYsO_-JZUKhWVlBB_vSS5JjEk-SvQYlPrmexuQatq4HIqq57x-g-HmKET1HcXj2Ars3iWobdk6Vvik.DR5e_rBg32Ca46z06n32XjWcNOMfT6nNFqCy84GfbW8&dib_tag=se&keywords=ipad&qid=1710548798&sprefix=ipad%2Caps%2C220&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# Use WebDriverWait to wait for the price element to be present on the page
try:
    # Define the maximum wait time (for example, 5 seconds)
    wait = WebDriverWait(driver, 10)
    
    # Wait until the element identified by class name 'aok-offscreen' is present
    price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-offscreen")))
    
    # Print the text attribute of the price 
    print(price_element.text)
except Exception as e:
    print(f"An error occurred: {e}")


# Close the browser
driver.quit()



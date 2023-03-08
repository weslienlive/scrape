from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument('headless')
#options.add_argument('--no-sandbox')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager.install()), options=options)
url = "https://www.forexfactory.com/calendar"
driver.get(url)



try:
    # Wait for the tbody tag to appear on the webpage
    tbody_locator = (By.TAG_NAME, 'tbody')
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(tbody_locator))

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html5lib')

    # Find the tbody tag and print it
    tbody = soup.find('tbody')
    print(tbody)
except Exception as e:
    print(f"Error: {e}")
    print("Could not find the tbody tag on the webpage.")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
driver_manager = ChromeDriverManager()
driver = webdriver.Chrome(service=Service(executable_path=driver_manager.install()), options=options)
url = "https://www.forexfactory.com/calendar"
driver.get(url)



try:
    # Wait for the tbody tag to appear on the webpage
    tbody_locator = (By.TAG_NAME, 'tbody')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(tbody_locator))

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table with class "calendar__table"
    calendar_table = soup.find('table', {'class': 'calendar__table'})

    # Find all the tr tags in the table
    tr_tags = table.find_all('tr')

    # Loop through the tr tags and only print the ones that meet the criteria
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        for td in td_tags:
            if td.text.strip() == 'US' and 'calendar__cell calendar__impact impact calendar__impact calendar__impact--low' in td['class']:
                print(tr)
                break
    

    #print(tbody)
except Exception as e:
    print(f"Error: {e}")
    print("Could not find the tbody tag on the webpage.")

driver.quit()
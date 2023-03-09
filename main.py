from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tqdm import tqdm

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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(tbody_locator))

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table with class "calendar__table"
    calendar_table = soup.find('table', {'class': 'calendar__table'})

    # Find all entries
    entries = calendar_table.find_all('tr', {'class' : 'calendar__row calendar_row calendar__row--grey calendar__row--new-day newday'})

    # Loop over entries and print their index number and contents
    events_schedule = {}
    for i, entry in enumerate(entries):
        entries = { "currency" : None, "date" : None, "time" : None, "name" : None, "impact" : None}

        currencies = entry.find_all("td", {'class' : 'calendar__cell calendar__currency currency'})
        entries["currency"] = currencies

        events_schedule[f"entry_{i+1}"] = entries
        
    print(events_schedule)

except Exception as e:
    print(f"Error: {e}")
    print("Could not find the tbody tag on the webpage.")

driver.quit()


'''
# Loop through the tr tags and only print the ones that meet the criteria
for tr in tqdm(tr_tags, desc="Processing events"):
    td_tags = tr.find_all('td', {'class': 'calendar__cell calendar__currency currency'})
    for td in td_tags:
        print(td)

# Get text from <span> inside <td> with class="calendar__cell"
event_date = tr.find("td", {"class": "calendar__cell"}).find("span").text

# Get text from <td> with class="calendar__cell calendar__time time"
event_time = tr.find("td", {"class": "calendar__cell calendar__time time"}).text

# Get text from <span> with class="calendar__event-title"
event_name = tr.find("span", {"class": "calendar__event-title"}).text

# Print the variables
print("Event Date:", event_date)
print("Event Time:", event_time)
print("Event Name:", event_name)

    

        # get event date
        event_date = tr.find('td', {'class': 'calendar__cell calendar__date date'}).find('span', {'class': 'date'})

        # get event time
        event_time = tr.find('td', {'class': 'calendar__cell calendar__time time'})

        # get event currency
        event_currency = tr.find('td', {'class': 'calendar__cell calendar__currency currency'})

        # get event impact
        event_impact = tr.find('td', {'class': 'calendar__cell calendar__impact impact calendar__impact calendar__impact--high'}).span['title']

        # get event title
        event_title = tr.find('span', {'class': 'calendar__event-title'})

        # print results
        print(event_date, event_time, event_currency, event_impact, event_title)



    # Wait for the tbody tag to appear on the webpage
    tbody_locator = (By.TAG_NAME, 'tbody')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(tbody_locator))

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table with class "calendar__table"
    calendar_table = soup.find('table', {'class': 'calendar__table'})


    # Find all currencies
    currencies = calendar_table.find_all("td", {'class' : 'calendar__cell calendar__currency currency'})

    # Find all times
    event_time = calendar_table.find_all("td", {'class' : 'calendar__cell calendar__time time'})

    # Loop over all td tags with the specified class
    for i, td in enumerate(event_time):
        schedule = td.find('div')
        symbols[f"event_time_{i+1}"] = schedule.text.strip()


    # Loop over all td tags with the specified class
    for i, td in enumerate(currencies):
        if td.text.strip() == "USD":
            symbols[f"symbol_{i+1}"] = td.text.strip()

    # Print the symbols dictionary
    print(symbols)


working v2
# Loop over all td tags with the specified class
for i, td in enumerate(event_time):
    schedule = td.find('div')
    symbols[f"event_time_{i+1}"] = schedule.text.strip()

    # Check if the currency is USD
    currency_td = td.find_next_sibling("td", {'class': 'calendar__currency currency'})
    if currency_td.text.strip() == "USD":
        symbols[f"symbol_{i+1}"] = currency_td.text.strip()


good idea
    # Find all table rows
    table_rows = calendar_table.find_all('tr')

    # Loop over all table rows
    symbols = {}
    for i, tr in enumerate(table_rows):
        entry = {}
        
        # Insert loop here
        # Find the currency and event time for this row
        currency = tr.find("td", {'class' : 'calendar__cell calendar__currency currency'})
        event_time = tr.find_all("td", {'class' : 'calendar__cell calendar__time time'})



        # Store the dictionary under the entry number in the symbols dictionary
        symbols[f"entry_number_{i+1}"] = entry

    # Print the symbols dictionary
    print(symbols)
'''
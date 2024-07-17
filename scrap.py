from selenium import webdriver
import time
import csv

# Function to scrape profile information using Selenium
def scrape_profile_info(url):
    # Specify path to chromedriver
    chrome_driver_path = '/path/to/chromedriver'  # Update this path with your chromedriver path
    service = webdriver.chrome.service.Service(chrome_driver_path)
    service.start()
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        
        # Wait for page to load (adjust sleep time as needed)
        time.sleep(5)
        
        # Scrape profile information
        name = driver.find_element_by_css_selector('h2').text.strip()
        address = driver.find_element_by_css_selector('p.address').text.strip()
        map_link = driver.find_element_by_css_selector('a[href]').get_attribute('href')
        
        return [{'Name': name, 'Address': address, 'Map Link': map_link}]
    
    finally:
        driver.quit()
        service.stop()

# URL to scrape
url = 'https://shop.rangs.com.bd/profile'

try:
    data = scrape_profile_info(url)
    
    # Write to CSV
    filename = 'profile_info.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Address', 'Map Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow(data[0])
        
    print(f'Successfully scraped profile data from {url} and saved to {filename}')
    
except Exception as e:
    print(f'Error scraping {url}: {e}')

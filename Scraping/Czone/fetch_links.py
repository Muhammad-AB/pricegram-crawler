# Script: Product URL Scraper
# Author: Syed Ahsan Ullah Tanweer
# Date: 16/12/2023

# Script to extract product URLs for a given category and store them in a txt file
# Uses Selenium and ChromeDriverManager for web scraping

# Import necessary libraries from Selenium and webdriver manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch(driver, category_name, category_url):
    """
    Fetch product links from a given category URL and save them to a text file.

    Parameters:
        driver (webdriver): Selenium webdriver instance.
        category_name (str): Name of the product category.
        category_url (str): URL of the product category.

    Returns:
        None
    """
    # Navigations
    print(f"Trying {category_url} at {time.ctime()}") 
    driver.get(category_url)

    # Click on dropdown to show more results per page
    driver.find_element(By.CSS_SELECTOR, "#ddlResults").click()
    driver.find_element(By.CSS_SELECTOR, "#ddlResults > option:nth-child(6)").click()

    # Extract product links from the page
    products = driver.find_elements(By.CSS_SELECTOR, "div > h4 > a")
    links = []

    for product in products:
        link = product.get_attribute("href")

        # Filter links ending with ".aspx" (irrelevant links)
        if link[-5:] == ".aspx":
            links.append(link)

    # Saving the Data
    with open(f"cz_{category_name}_links.txt", 'a') as txt:
        for link in links:
            txt.write(f"\n{link}")

    print(f"Collected {len(links)} products in Category: {category_name}")

# Define categories and their corresponding URLs
CATEGORIES = {
    "Laptop": "https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx",
    "Used Laptop": "https://www.czone.com.pk/laptops-used-pakistan-ppt.715.aspx",
    "Headsets": "https://www.czone.com.pk/headsets-headphones-mic-pakistan-ppt.175.aspx",
    "Speakers": "https://www.czone.com.pk/speakers-pakistan-ppt.97.aspx",
    "Cameras": "https://www.czone.com.pk/cameras-drones-pakistan-ppt.136.aspx",
    "Mouse": "https://www.czone.com.pk/mouse-pakistan-ppt.95.aspx",
    "Keyboard": "https://www.czone.com.pk/keyboard-pakistan-ppt.162.aspx",
    "Watch": "https://www.czone.com.pk/smart-watches-pakistan-ppt.403.aspx",
    "Mobile": "https://www.czone.com.pk/tablet-pc-pakistan-ppt.278.aspx",
    "Monitor": "https://www.czone.com.pk/lcd-led-monitors-pakistan-ppt.108.aspx"
}

# Create an instance of Chrome webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

# Iterate through each category and fetch product links
for category_name, category_url in CATEGORIES.items():
    fetch(driver, category_name, category_url)

# Close the webdriver
driver.quit()

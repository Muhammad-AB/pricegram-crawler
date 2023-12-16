from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch(driver, category_name, category_url):

    # Navigations
    print(f"Trying {category_url} at {time.ctime()}") 
    driver.get(category_url)
    driver.find_element(By.CSS_SELECTOR, "#ddlResults").click()
    driver.find_element(By.CSS_SELECTOR, "#ddlResults > option:nth-child(6)").click()
    products = driver.find_elements(By.CLASS_NAME, "product")

    links = []
    for product in products:
        link = product.find_element(By.CLASS_NAME, "image").find_elements(By.TAG_NAME, 'a')
        links.append(link[-1].get_attribute("href"))
        
    # Saving the Data
    with open(f"tg_{category_name}_links.txt",'a') as txt:
        for link in links:
            txt.write(f"\n{link}")

    print(f"Collected {len(links)} products in Category: {category_name}")

CATEGORIES = {
    "laptops": "https://www.techglobe.pk/laptops",
    "headsets": "https://www.techglobe.pk/headphones-earphones",
    "speakers": "https://www.techglobe.pk/speakers",
    "cameras": "https://www.techglobe.pk/cameras",
    "mouse": "https://www.techglobe.pk/mouse",
    "keyboard": "https://www.techglobe.pk/keyboard"
}

# Create an instance of Chrome webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

for category_name, category_url in CATEGORIES.items():
    fetch(driver, category_name, category_url)
# driver.quit()
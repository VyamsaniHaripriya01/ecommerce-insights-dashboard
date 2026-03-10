"""
Flipkart Product Scraper

Scrapes product title, price, rating, and link from Flipkart search results
using Selenium and undetected_chromedriver.
"""

# script that scrapes the first N pages of search results for a product keyword

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)
driver.get("https://www.flipkart.com")

# Close login popup
try:
    close_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_btn.click()
except:
    print("Popup not shown")

# Search for laptops
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search.send_keys("laptop")
search.submit()

# Let page load and scroll
time.sleep(4)

# Scroll multiple times to trigger full product load
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Save the full HTML page to inspect what Selenium sees
with open("flipkart_laptops_rendered.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Page saved. Open flipkart_laptops_rendered.html and inspect the structure.")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, '_13oc-S')]"))
)

#Find the product data(scrape)
product_cards = driver.find_elements(By.XPATH, "//div[contains(@class, '_13oc-S')]")
print("Product cards found:", len(product_cards))

products = []

for card in product_cards:
    try:
         title_elem = card.find_elements(By.XPATH, ".//div[contains(@class,'_4rR01T') or contains(@class,'s1Q9rs') or contains(@class,'IRpwTa')]")
         if not title_elem:
            continue
         title = title_elem[0].text.strip()

    except:
        try:
            title = card.find_element(By.XPATH, ".//a[contains(@class,'s1Q9rs')]").text
        except:
            continue

    try:
        price = card.find_element(By.XPATH, ".//div[contains(@class,'_30jeq3')]").text
    except:
        price = "N/A"

    try:
        rating = card.find_element(By.XPATH, ".//div[contains(@class,'_3LWZlK')]").text
    except:
        rating = "No rating"

    try:
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = "N/A"

    products.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Link": link
    })

driver.quit()

# Save results
df = pd.DataFrame(products)
df.to_csv("flipkart_laptops_final.csv", index=False)
print(df.head())

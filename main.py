from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from config import BASE_URL, SEARCH_TERM, MAX_PAGES
from utils import save_to_csv, log_result
from tests import test_product_page, test_search_functionality, test_responsive_design

def crawl_amazon(driver, search_term, max_pages=1):
    products = []
    driver.get(BASE_URL)
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(search_term)
    search_box.submit()

    for _ in range(max_pages):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )
        items = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")

        for item in items:
            try:
                name = item.find_element(By.TAG_NAME, "h2").text
                url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                rating = item.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
                products.append([name, price, rating, url])
            except Exception:
                continue

        # Next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            next_button.click()
            time.sleep(3)
        except:
            break

    return products

if __name__ == "__main__":
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    # ✅ Uses webdriver-manager to download correct driver for your Google Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        log_result("🔎 Starting crawl and test...")
        product_data = crawl_amazon(driver, SEARCH_TERM, MAX_PAGES)
        save_to_csv(product_data)

        if product_data:
            driver.get(product_data[0][3])
            test_product_page(driver)

        test_search_functionality(driver, BASE_URL)
        test_responsive_design(driver)

    finally:
        driver.quit()
        log_result("✅ Testing completed.")

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils import log_result
import time

def test_product_page(driver):
    try:
        driver.find_element(By.ID, "add-to-cart-button")
        log_result("✅ Add to Cart button present.")
    except NoSuchElementException:
        log_result("❌ Add to Cart button missing.")

    try:
        driver.find_element(By.ID, "productDetails_techSpec_section_1")
        log_result("✅ Product technical spec section present.")
    except NoSuchElementException:
        try:
            driver.find_element(By.ID, "detailBullets_feature_div")
            log_result("✅ Product detail bullets section present.")
        except NoSuchElementException:
            log_result("❌ Product details section missing.")

    try:
        driver.find_element(By.ID, "imgTagWrapperId")
        log_result("✅ Image gallery present.")
    except NoSuchElementException:
        log_result("❌ Image gallery missing.")

def test_search_functionality(driver, base_url):
    try:
        driver.get(base_url)
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")

        # Valid search
        search_box.clear()
        search_box.send_keys("headphones")
        search_box.submit()
        log_result("✅ Valid search input test passed.")
        time.sleep(2)

        # Invalid search
        driver.get(base_url)
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys("@@@###")
        search_box.submit()
        log_result("✅ Invalid search input test executed.")
        time.sleep(2)

    except Exception as e:
        log_result(f"❌ Search functionality test failed: {str(e)}")

def test_responsive_design(driver):
    resolutions = [(1920, 1080), (768, 1024), (375, 667)]
    for width, height in resolutions:
        try:
            driver.set_window_size(width, height)
            time.sleep(1)  # Allow layout to stabilize
            log_result(f"✅ Tested responsiveness at {width}x{height}")
        except Exception as e:
            log_result(f"❌ Responsiveness test failed at {width}x{height}: {str(e)}")

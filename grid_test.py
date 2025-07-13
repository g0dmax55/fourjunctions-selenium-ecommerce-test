from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from concurrent.futures import ThreadPoolExecutor
from utils import log_result
from config import BASE_URL

GRID_URL = "http://localhost:4444/wd/hub"

def run_test(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--no-sandbox")
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        raise ValueError("Unsupported browser")

    try:
        driver.get(BASE_URL)
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("monitor")
        search_box.submit()
        log_result(f"✅ Search test passed on {browser}")
    except Exception as e:
        log_result(f"❌ {browser} test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    browsers = ["chrome", "firefox"]
    with ThreadPoolExecutor() as executor:
        executor.map(run_test, browsers)

    log_result("✅ Selenium Grid parallel test completed.")

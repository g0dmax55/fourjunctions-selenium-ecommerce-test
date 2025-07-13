import csv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def save_to_csv(products, filename="results/product_data.csv"):
    """Save extracted product data to a CSV file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Ratings", "URL"])
        writer.writerows(products)

def log_result(message, filename="results/test_log.txt"):
    """Log a result message to a log file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(message + "\n")

def switch_screen_size(driver, width, height):
    """Change the browser window size to simulate responsiveness."""
    driver.set_window_size(width, height)

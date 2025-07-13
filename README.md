````markdown
# FourJunctions Selenium E-commerce Test

## ✅ 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

## ✅ 3. Run the Main Script

```bash
python main.py
```

---

## ✅ 4. (Bonus) Run Selenium Grid Test

Start the Selenium Grid using Docker:

```bash
docker-compose up -d
```

Then run the parallel cross-browser test:

```bash
python grid_test.py
```

---

## 📁 Project Structure

```
fourjunctions-selenium-ecommerce-test/
├── main.py               # Main crawling & testing logic
├── config.py             # Constants (search term, URL, page count)
├── tests.py              # UI, functionality, and responsive tests
├── utils.py              # Logging, CSV writing, screen resizing
├── grid_test.py          # Bonus: parallel execution on Selenium Grid
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Grid setup (hub + nodes)
├── README.md             # This file
└── results/
    ├── product_data.csv  # Output of crawled product data
    └── test_log.txt      # Log of test execution results
```

---

## 🧪 Features

* ✅ Crawls Amazon search results for **laptops**
* ✅ Extracts: Product Name, Price, Rating, Product URL
* ✅ Functional Testing:

  * Add to Cart button presence
  * Product details section
  * Image gallery
* ✅ Search Testing:

  * Valid query: `"headphones"`
  * Invalid query: `"@@@###"`
* ✅ Responsive UI Testing:

  * Desktop (1920x1080)
  * Tablet (768x1024)
  * Mobile (375x667)
* ✅ Multi-page crawl via `MAX_PAGES`
* ✅ Bonus: Selenium Grid parallel test on Chrome + Firefox

---

## 🧰 Tools and Frameworks Used

* Python 3.8+
* Selenium 4
* WebDriver Manager
* Docker (for Selenium Grid)
* Amazon.in as target website

---

## 📁 Output Files

| File                      | Description                       |
| ------------------------- | --------------------------------- |
| results/product\_data.csv | Crawled laptop product data       |
| results/test\_log.txt     | Log of all test steps and results |

---

## 📌 Assumptions & Constraints

* Target site is Amazon India
* Assumes Amazon DOM layout is stable (may break if site changes)
* Some products may not have ratings — handled gracefully
* Selenium Grid testing assumes Docker is installed and port 4444 is open
* Only DOM-based scraping is performed (no JS-rendered elements)

---
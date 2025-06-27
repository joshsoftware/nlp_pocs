# LawRato Q&A Web Scraper 🕷️

This Python project performs web crawling and scraping on [LawRato](https://lawrato.com) to extract legal questions and answers from advice-related pages. The extracted data is saved into a CSV file.

---

## Features

- Crawls all internal URLs ending with `-advice` on `https://lawrato.com`
- Scrapes legal questions (`<h2>`) and their corresponding answers (`<p>`)
- Converts relative links to absolute URLs
- Deduplicates entries
- Saves the data into a `qa_data.csv` file

---

## Technologies Used

- Python 3
- `requests` – for HTTP requests
- `BeautifulSoup` (bs4) – for HTML parsing
- `csv` – for writing output
- `urllib.parse` – to join base URL with relative links

---

## How to Run

1. **Install dependencies** (if not already installed):

   ```bash
   pip install requests beautifulsoup4

2. **Run the script**
  
   ```bash
   python crawler-python.py

2. **Output**
   - The file qa_data.csv will be created in the same directory.
   - It will contain two columns: Question, Answer.

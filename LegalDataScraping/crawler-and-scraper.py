import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def get_question_answer_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.select('h2')
    answers = soup.select('p')

    data = []

    # Only pair up to the shortest list length to avoid index mismatch
    for q, a in zip(questions, answers):
        question = q.get_text(strip=True)
        answer = a.get_text(strip=True)
        data.append([question, answer])
    
    return data

def scrape():
    base_url = 'https://lawrato.com/free-legal-advice'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_links = soup.select('a')
    urls = []

    for link in all_links:
        href = link.get('href')
        if href:
            full_url = urljoin(base_url, href)
            if full_url.startswith('https://lawrato.com/') and full_url.endswith('-advice'):
                urls.append(full_url)

    urls = list(set(urls))  # remove duplicates

    all_data = []
    for url in urls:
        print(f"Scraping: {url}")
        qa_data = get_question_answer_from_url(url)
        all_data.extend(qa_data)

    # Write to CSV
    with open('qa_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Question', 'Answer'])
        writer.writerows(all_data)

if __name__ == '__main__':
    scrape()


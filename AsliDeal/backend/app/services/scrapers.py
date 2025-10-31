from typing import List
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_page(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def scrape_discount(self, product_url: str) -> dict:
        page_content = self.fetch_page(product_url)
        soup = BeautifulSoup(page_content, 'html.parser')

        # Example selectors, these should be updated based on the actual website structure
        title = soup.select_one('h1.product-title').get_text(strip=True)
        current_price = float(soup.select_one('span.current-price').get_text(strip=True).replace('Rs.', '').replace(',', ''))
        original_price = float(soup.select_one('span.original-price').get_text(strip=True).replace('Rs.', '').replace(',', ''))
        
        discount_percentage = ((original_price - current_price) / original_price) * 100

        return {
            'title': title,
            'current_price': current_price,
            'original_price': original_price,
            'discount_percentage': discount_percentage
        }

    def scrape_multiple_products(self, product_urls: List[str]) -> List[dict]:
        results = []
        for url in product_urls:
            try:
                result = self.scrape_discount(url)
                results.append(result)
            except Exception as e:
                results.append({'error': str(e), 'url': url})
        return results
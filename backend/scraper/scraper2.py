import requests
from bs4 import BeautifulSoup

def scrape_njuskalo_listings(url: str, max_pages: int = 10):
    all_listings = []
    page = 1

    while True:
        paginated_url = f"{url}&page={page}" if page > 1 else url
        print(f"Scraping page: {paginated_url}")

        try:
            response = requests.get(paginated_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            listings = soup.find_all('article', class_='entity-body')
            
            if not listings:
                break

            for listing in listings:
                # Naslov
                title_element = listing.find('h3', class_='entity-title')
                title = title_element.text.strip() if title_element else 'N/A'

                # Link
                link_element = title_element.find('a') if title_element else None
                link = 'https://www.njuskalo.hr' + link_element['href'] if link_element and link_element.get('href') else 'N/A'

                # Slika
                img_element = listing.find('img', class_='entity-thumbnail-img')
                raw_url = img_element.get('data-src') or img_element.get('src') or ''
                image_url = ''
                if raw_url.startswith('//'):
                    image_url = 'https:' + raw_url
                elif raw_url.startswith('/'):
                    image_url = 'https://www.njuskalo.hr' + raw_url
                elif raw_url.startswith('http'):
                    image_url = raw_url

                # Filter defaultne slike (ikone itd.)
                if "static.njuskalo.hr" in image_url and "image-" not in image_url:
                    image_url = ''

                # Lokacija i površina sa cijenom 
                details_element = listing.find('div', class_='entity-description-main')
                location, size = 'N/A', 'N/A'
                if details_element:
                    text_lines = details_element.text.strip().split('\n')
                    for line in text_lines:
                        if 'Lokacija:' in line:
                            location = line.replace('Lokacija:', '').strip()
                        if 'površina:' in line.lower() and 'm2' in line.lower():
                            size = line.strip()

                price_element = listing.find('strong', class_='price')
                price = price_element.text.strip() if price_element else 'N/A'

                # Dodavanje u listu
                all_listings.append({
                    'title': title,
                    'link': link,
                    'image_url': image_url,
                    'location': location,
                    'size_price': f"{size} • {price}"
                })

            page += 1
            if page > max_pages:
                break

        except Exception as e:
            break

    # micanje duplikate
    unique_listings = list({listing['link']: listing for listing in all_listings}.values())
    return unique_listings

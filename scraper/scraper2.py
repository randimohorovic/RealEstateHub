import requests
from bs4 import BeautifulSoup


def scrape_real_estate_listings(url: str, max_pages: int = 10, listings_per_page: int = 12):
    all_listings = []
    page = 1

    while True:
        
        paginated_url = f"{url}&offset={listings_per_page * (page - 1)}"
        print(f"Scraping page: {paginated_url}") # 

        try:
            # http request salje
            response = requests.get(paginated_url)
            response.raise_for_status() 

            # parser
            soup = BeautifulSoup(response.content, 'html.parser')

            #bitan dio html-a di se nalaze sve objave
            main_content = soup.find('main', class_='iro-content-wrap')
            listings = main_content.find_all('div', class_='col-md-4 col-sm-4 col-xs-12 iro-list-realestate')
            
            if not listings:
                break

            # exctraction of data
            for listing in listings:
                title = listing.find('h2').text.strip()
                link = listing.find('a')['href']
                image_url = listing.find('img')['src']
                details = listing.find('ul').find_all('li')
                location = details[0].text.strip() if len(details) > 0 else 'N/A'
                size_price = details[1].text.strip() if len(details) > 1 else 'N/A'

                # trenutno spremanje podataka lokalno, baza je potrebna
                all_listings.append({
                    'title': title,
                    'link': link,
                    'image_url': image_url,
                    'location': location,
                    'size_price': size_price
                })

            page += 1  # prolazim kroz stranice, cim hita max pages stane
            if page > max_pages:
                break  

        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            break  
    
    unique_listings = list({listing['link']: listing for listing in all_listings}.values()) 
    # hvata mi duplikate, moguce zbog offseta da uhvati vise puta isti listing..
    return unique_listings


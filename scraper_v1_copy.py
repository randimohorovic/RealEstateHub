import requests
from bs4 import BeautifulSoup

# Function to scrape listings
def scrape_real_estate_listings(url):
    # Send request to the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main container with all listings
    main_content = soup.find('main', class_='iro-content-wrap')

    # Find all listings (they are inside 'iro-list-realestate')
    listings = main_content.find_all('div', class_='col-md-4 col-sm-4 col-xs-12 iro-list-realestate')

    # Loop through each listing and extract data
    for listing in listings:
        # Extract the title and link (from <h2> and <a> tags)
        title = listing.find('h2').text.strip()
        link = listing.find('a')['href']
        
        # Extract the image URL
        image_url = listing.find('img')['src']

        # Extract the location and price/size from the <ul> list
        details = listing.find('ul').find_all('li')
        location = details[0].text.strip() if len(details) > 0 else 'N/A'
        size_price = details[1].text.strip() if len(details) > 1 else 'N/A'

        # Print or store the extracted information
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Image URL: {image_url}")
        print(f"Location: {location}")
        print(f"Size & Price: {size_price}")
        print('-' * 80)

# Example usage:
url = 'https://mondo-nekretnine.hr/hr/realestate'  # Replace with the actual URL of the page
scrape_real_estate_listings(url)

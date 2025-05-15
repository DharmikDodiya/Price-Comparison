import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_flipkart_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    search_url = f"https://www.flipkart.com/search?q={product_name}"
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    product_container = soup.find('a', {'class': 'CGtC98'})
    
    if not product_container:
        return {"error": "Product not found on Flipkart"}
    
    # Extracting product name, price, and specifications
    try:
        product_price = product_container.find('div', {'class': 'yKfJKb row'}).find('div', {'class': 'Nx9bqj _4b5DiR'}).text.strip()
        # product_img = product_container.find('img', {'class': 'DByuf4'})['src']
        details_container = product_container.find('div', {'class': 'yKfJKb row'})
        product_name_tag = details_container.find('div', {'class': 'Nx9bqj _4b5DiR'})
        # specs_list = details_container.find('ul', {'class': 'G4BRas'})
        product_name = product_name_tag.text.strip() if product_name_tag else "Product name not found"
        product_img = product_container.find('img', {'class': 'DByuf4'})['src']

        # Extract product URL, adding domain if needed
        href = product_container['href']
        if href.startswith('/'):
            product_url = "https://www.flipkart.com" + href
        else:
            product_url = href
        # specs = [li.text.strip() for li in specs_list.find_all('li')] if specs_list else ["No specifications available"]
    except Exception as e:
        print(f"Error extracting details: {e}")
        return {"error": "Failed to extract product details"}
    
    return {
        'Price': product_price,
        "URL": product_url,
        "Image_URL": product_img
    }

# def get_amazon_price(product_name):
#     search_url = f"https://www.amazon.in/s?k={quote_plus(product_name)}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                       "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept-Language": "en-US,en;q=0.9",
#     }

#     try:
#         response = requests.get(search_url, headers=headers, timeout=10)
#         response.raise_for_status()
#     except Exception as e:
#         return {"Price": "Price Not Available", "URL": ""}

#     soup = BeautifulSoup(response.text, "html.parser")
#     product_container = soup.find('div', {'data-component-type': 's-search-result'})

#     if not product_container:
#         return {"Price": "Price Not Available", "URL": ""}

#     try:
#         price_whole = product_container.find('span', {'class': 'a-price-whole'})
#         price_fraction = product_container.find('span', {'class': 'a-price-fraction'})
#         if price_whole:
#             product_price = price_whole.text.strip()
#             if price_fraction:
#                 product_price += "." + price_fraction.text.strip()
#             product_price = "₹" + product_price
#         else:
#             product_price = "Price Not Available"

#         product_img = product_container.find('img', {'class': 'DByuf4'})['src']
#         link_tag = product_container.find('a', {'class': 'a-link-normal s-no-outline'})
#         product_url = "https://www.amazon.in" + link_tag['href'] if link_tag else ""
#     except Exception as e:
#         return {"Price": "Price Not Available", "URL": ""}

#     return {"Price": product_price, "URL": product_url, "Image_URL": product_img}

def get_amazon_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Prepare the search URL
    search_url = f"https://www.amazon.in/s?k={quote_plus(product_name)}"
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first product container
    product_container = soup.find('div', {'data-component-type': 's-search-result'})
    if not product_container:
        print("Product container not found")
        return {"error": "Product not found on Amazon"}

    try:
        # Extract product name
        name_tag = (product_container.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}) or
        product_container.find('span', {'class': 'a-text-normal'}))
        # print(product_container)
        product_name = soup.select_one('h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal span')
        product_name = product_name.text.strip() if product_name else 'N/A'

        # Extract product price
        product_price = soup.select_one('span.a-price > span.a-offscreen')
        product_price = product_price.text.strip() if product_price else 'N/A'
        
        # Extract image
        img_tag = product_container.find('img', {'class': 's-image'})
        product_img = img_tag.get('src') if img_tag else "No image available"

        # Extract product URL
        product_link = product_container.find('a', {'class': 'a-link-normal s-no-outline'})
        product_url = "https://www.amazon.in" + product_link.get('href') if product_link else "No URL available"
        # print(product_name, product_price, product_img, product_url)
        return {
            # "Product Name": product_name,
            "Price": product_price,
            "Image_URL": product_img,
            "URL": product_url
        }

    except Exception as e:
        print(f"Error while extracting product details: {e}")
        return {"error": f"Could not extract product details: {e}"}




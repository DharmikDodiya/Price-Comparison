from priceapp.scrapping import get_flipkart_price, get_amazon_price

product_name = "Laptop"

amazon_result = get_amazon_price(product_name)

flipkart_result = get_flipkart_price(product_name)

print("Flipkart Result:", flipkart_result)
print("Amazon Result:", amazon_result)

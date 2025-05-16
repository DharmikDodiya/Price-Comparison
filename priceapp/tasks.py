from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Product, PriceHistory
from .scrapping import get_flipkart_price, get_amazon_price


@shared_task
def check_price_drops():
    products = Product.objects.all()

    for product in products:
        print(f"Checking price for: {product.name} ({product.user.username})")
        
        # **Flipkart Price Check**
        flipkart_data = get_flipkart_price(product.name)
        if "Price" in flipkart_data and flipkart_data["Price"] != "Price Not Available":
            try:
                flipkart_current_price = int(''.join(filter(str.isdigit, flipkart_data["Price"])))
            except ValueError:
                print(f"Error extracting Flipkart price for {product.name}")
                continue

            flipkart_last_price = product.last_flipkart_price or float('inf')

            if flipkart_current_price < flipkart_last_price:
                # Send Flipkart Price Drop Alert (HTML Email)
                context = {
                    'product_name': product.name,
                    'old_price': flipkart_last_price,
                    'new_price': flipkart_current_price,
                    'product_url': flipkart_data.get('URL', '#'),
                    'username': product.user.username,
                    'store_name': 'Flipkart',
                }
                subject = f"Price Drop Alert for {product.name} on Flipkart"
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [product.user.email]
                html_content = render_to_string('emails/price_drop_alert.html', context)
                
                email = EmailMultiAlternatives(subject, html_content, from_email, to_email)
                email.attach_alternative(html_content, "text/html")
                email.send()

            # Save Flipkart Price History
            PriceHistory.objects.create(
                product=product,
                price=flipkart_current_price,
                store="Flipkart"
            )
            product.last_flipkart_price = flipkart_current_price
            product.save()

        # **Amazon Price Check**
        amazon_data = get_amazon_price(product.name)
        if "Price" in amazon_data and amazon_data["Price"] != "Price Not Available":
            try:
                amazon_current_price = int(''.join(filter(str.isdigit, amazon_data["Price"])))
            except ValueError:
                print(f"Error extracting Amazon price for {product.name}")
                continue

            amazon_last_price = product.last_amazon_price or float('inf')

            if amazon_current_price < amazon_last_price:
                # Send Amazon Price Drop Alert (HTML Email)
                context = {
                    'product_name': product.name,
                    'old_price': amazon_last_price,
                    'new_price': amazon_current_price,
                    'product_url': amazon_data.get('URL', '#'),
                    'username': product.user.username,
                    'store_name': 'Amazon',
                }
                subject = f"Price Drop Alert for {product.name} on Amazon"
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [product.user.email]
                html_content = render_to_string('emails/price_drop_alert.html', context)
                
                email = EmailMultiAlternatives(subject, html_content, from_email, to_email)
                email.attach_alternative(html_content, "text/html")
                email.send()

            # Save Amazon Price History
            PriceHistory.objects.create(
                product=product,
                price=amazon_current_price,
                store="Amazon"
            )
            product.last_amazon_price = amazon_current_price
            product.save()


# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Product, PriceHistory
# from .scrapping import get_flipkart_price, get_amazon_price


# @shared_task
# def check_price_drops():
#     products = Product.objects.all()
    
#     for product in products:
#         print(product.name)
#         # Flipkart Price Check
#         flipkart_data = get_flipkart_price(product.name)
#         if "Price" in flipkart_data and flipkart_data["Price"] != "Price Not Available":
#             flipkart_current_price = int(''.join(filter(str.isdigit, flipkart_data["Price"])))
#             flipkart_last_price = product.last_flipkart_price or 0

#             if flipkart_current_price < flipkart_last_price:
#                 # Send Flipkart Price Drop Alert
#                 send_mail(
#                     f'Price Drop Alert for {product.name} on Flipkart',
#                     f'The price dropped from ₹{flipkart_last_price} to ₹{flipkart_current_price} on Flipkart!\nLink: {flipkart_data["URL"]}',
#                     settings.DEFAULT_FROM_EMAIL,
#                     [product.user.email],
#                 )
#             # Save Flipkart Price History
#             PriceHistory.objects.create(product=product, last_flipkart_price=flipkart_current_price, store="Flipkart")
#             product.last_flipkart_price = flipkart_current_price
#             product.save()

#         # Amazon Price Check
#         amazon_data = get_amazon_price(product.name)
#         if "Price" in amazon_data and amazon_data["Price"] != "Price Not Available":
#             amazon_current_price = int(''.join(filter(str.isdigit, amazon_data["Price"])))
#             amazon_last_price = product.last_amazon_price or 0

#             if amazon_current_price < amazon_last_price:
#                 # Send Amazon Price Drop Alert
#                 send_mail(
#                     f'Price Drop Alert for {product.name} on Amazon',
#                     f'The price dropped from ₹{amazon_last_price} to ₹{amazon_current_price} on Amazon!\nLink: {amazon_data["URL"]}',
#                     settings.DEFAULT_FROM_EMAIL,
#                     [product.user.email],
#                 )
#             # Save Amazon Price History
#             PriceHistory.objects.create(product=product, last_amazon_price=amazon_current_price, store="Amazon")
#             product.last_amazon_price = amazon_current_price
#             product.save()


# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Product, PriceHistory
# from .scrapping import get_flipkart_price, get_amazon_price


# @shared_task
# def check_price_drops():
#     products = Product.objects.all()

#     for product in products:
#         print(f"Checking price for: {product.name} ({product.user.username})")
        
#         # **Flipkart Price Check**
#         flipkart_data = get_flipkart_price(product.name)
#         if "Price" in flipkart_data and flipkart_data["Price"] != "Price Not Available":
#             try:
#                 flipkart_current_price = int(''.join(filter(str.isdigit, flipkart_data["Price"])))
#             except ValueError:
#                 print(f"Error extracting Flipkart price for {product.name}")
#                 continue

#             flipkart_last_price = product.last_flipkart_price or float('inf')

#             if flipkart_current_price < flipkart_last_price:
#                 # Send Flipkart Price Drop Alert
#                 send_mail(
#                     f"Price Drop Alert for {product.name} on Flipkart",
#                     f"Good news! The price dropped from ₹{flipkart_last_price} to ₹{flipkart_current_price} on Flipkart.\nLink: {flipkart_data.get('URL', '#')}",
#                     settings.DEFAULT_FROM_EMAIL,
#                     [product.user.email],
#                 )

#             # Save Flipkart Price History
#             PriceHistory.objects.create(
#                 product=product,
#                 price=flipkart_current_price,
#                 store="Flipkart"
#             )
#             product.last_flipkart_price = flipkart_current_price
#             product.save()

#         # **Amazon Price Check**
#         amazon_data = get_amazon_price(product.name)
#         if "Price" in amazon_data and amazon_data["Price"] != "Price Not Available":
#             try:
#                 amazon_current_price = int(''.join(filter(str.isdigit, amazon_data["Price"])))
#             except ValueError:
#                 print(f"Error extracting Amazon price for {product.name}")
#                 continue

#             amazon_last_price = product.last_amazon_price or float('inf')

#             if amazon_current_price < amazon_last_price:
#                 # Send Amazon Price Drop Alert
#                 send_mail(
#                     f"Price Drop Alert for {product.name} on Amazon",
#                     f"Great deal! The price dropped from ₹{amazon_last_price} to ₹{amazon_current_price} on Amazon.\nLink: {amazon_data.get('URL', '#')}",
#                     settings.DEFAULT_FROM_EMAIL,
#                     [product.user.email],
#                 )

#             # Save Amazon Price History
#             PriceHistory.objects.create(
#                 product=product,
#                 price=amazon_current_price,
#                 store="Amazon"
#             )
#             product.last_amazon_price = amazon_current_price
#             product.save()



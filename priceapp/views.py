from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .scrapping import PriceScraper
from .scrapping import get_amazon_price, get_flipkart_price
from django.contrib.auth import authenticate, login, logout

# def home(request):
#     return render(request, 'home.html')

# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     return render(request, 'login.html')

# @login_required
# def logout_user(request):
#     logout(request)
#     messages.success(request, "Successfully Logged Out")
#     # return redirect('login_user')
#     return render(request, 'login.html')

# @login_required
# def SearchView(request):
#     return render(request, 'search.html')

# @login_required
# def search(request):
#     if request.method == "POST":
#         search_query = request.POST.get('search', '').strip()
#         if not search_query:
#             return render(request, 'search.html')

# #    get_flipkart_price(search_query)     # Fetch product data from multiple e-commerce platforms
#         flipkart_data = get_flipkart_price(search_query)
#         amazon_data = get_amazon_price(search_query)  # Another scraper function
#         # print(amazon_data)
#         # print(flipkart_data)
#         # print(flipkart_data.get("Image_URL", ""))
#         # Pass the data to the template
#         formatted_flipkart = {
#             "name": flipkart_data.get("Product Name", "N/A"),  # Fix key
#             "price": flipkart_data.get("price", "N/A"),
#             "specifications": flipkart_data.get("Specifications", []),
#             "url": flipkart_data.get("URL", "#"),
#             "image_url": flipkart_data.get("Image_URL", ""),  # Ensure image URL is provided
#         }
#         if amazon_data.get("purlname", "#") in ("Flipkart","Amazon"):
#             if amazon_data.get("purl", "#") == "Flipkart":
#                 pass
#         formatted_amazon = {
#             "name": amazon_data.get("Product Name", "N/A"),
#             "price": amazon_data.get("Price", "N/A"),
#             "specifications": amazon_data.get("Specifications", []),
#             "url": amazon_data.get("URL", "#"),
#             "image_url": amazon_data.get("Image_URL", ""),
#             "pname":amazon_data.get("purlname", "#"),
#             "p_url": amazon_data.get("purllink", "#"),
             
#         }
#         return render(request, 'search.html', {
#             'flipkart': formatted_flipkart,
#             'amazon': formatted_amazon,
#             'name': search_query
#         })

#     return render(request, 'search.html')
# headers =({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36' ,'Accept-Language': 'en-US,en;q=0.8'})


def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('search_view')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login_user')


@login_required
def search_view(request):
    # Render the empty search page on GET request
    return render(request, 'search.html', {
        'search_query': '',
        'flipkart': None,
        'amazon': None,
    })

# @login_required
# def search(request):
#     if request.method == "POST":
#         search_query = request.POST.get('search', '').strip()
#         if not search_query:
#             messages.error(request, "Please enter a product name to search.")
#             return render(request, 'search.html')

#         flipkart_data = get_flipkart_price(search_query)
#         amazon_data = get_amazon_price(search_query)

#         return render(request, 'search.html', {
#             'flipkart': flipkart_data,
#             'amazon': amazon_data,
#             'search_query': search_query,
#         })

#     return redirect('search_view')

@login_required
def search(request):
    print("hello")
    if request.method == "POST":
        search_query = request.POST.get('search', '').strip()
        print(search_query)
        # Check for empty search query
        if not search_query:
            messages.error(request, "Please enter a product name to search.")
            return render(request, 'search.html', {
                'search_query': '',
                'flipkart': None,
                'amazon': None,
            })

        # Fetch data from both platforms
        try:
            flipkart_data = get_flipkart_price(search_query)
            amazon_data = get_amazon_price(search_query)
        except Exception as e:
            messages.error(request, f"Error fetching product data: {e}")
            return render(request, 'search.html', {
                'search_query': search_query,
                'flipkart': None,
                'amazon': None,
            })
        print(flipkart_data,amazon_data)
        # Return results to the template
        return render(request, 'search.html', {
            'search_query': search_query,
            'flipkart': flipkart_data,
            'amazon': amazon_data,
        })

    # Redirect to the main search view if accessed via GET
    return redirect('search_view')
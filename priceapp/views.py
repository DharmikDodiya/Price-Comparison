from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .scrapping import PriceScraper
from .scrapping import get_amazon_price, get_flipkart_price
from .models import Product
from django.contrib.auth import authenticate, login, logout
# from django import forms
from priceapp.forms import CustomUserCreationForm


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

def product_list(request):
    # Get all products for the logged-in user
    products = Product.objects.filter(user=request.user)
    return render(request, "product_list.html", {"products": products})

def register_user(request):
    if request.method == "POST":
        print("hello")
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

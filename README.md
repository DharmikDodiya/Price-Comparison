# Price-Comparison

**Price Comparison Platform: Develop a web scraping-based platform where users can compare product prices from different e-commerce websites.**

# Key Features

- User registration and login.
- Scraping data from Amazon, Flipkart.

**Installation Guide**

# Requirements

- To run this project, you will need to have the following things installed:

- Python 3.9
- Django 

# Installation

**First, clone the repository**

```git clone https://github.com/DharmikDodiya/Price-Comparison.git```

```cd Price-Comparison```

**Set up a virtual environment**

```python3 -m venv myenv```

```source task_venv/bin/activate```  

**Install project dependencies**

```pip freeze > requirements.txt```

**Run the following command to create the  database tables**

```python manage.py migrate```

**Run the project**

```python3 manage.py runserver```

- Your application will be served at http://127.0.0.1:8000/.


# Features

- Basic User Authentication registration , login, logout, 
- Basic navigation (home page, login, register)
- Compare product prices from different websites

**In the backend, use Celery to scrape product data from Amazon and Flipkart every hour, updating the latest prices and maintaining a price history.**

**Login Page**

![image](https://github.com/user-attachments/assets/6beb1575-f615-4d65-9352-ab0884ea23d6)

**Search Page**

![image](https://github.com/user-attachments/assets/86717db1-0a1f-4195-b2f3-391c8fd1f157)

**Scraping Data into Amazone and Flipcart**

![image](https://github.com/user-attachments/assets/db22d390-ed1f-4d75-b6e2-901fe87aa8a1)

**Login User Product List**

![image](https://github.com/user-attachments/assets/4c78664e-9bf8-49eb-abeb-8a4bd8e68d2f)



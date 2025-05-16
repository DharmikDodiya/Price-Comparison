# Price-Comparison

**Price Comparison Platform: Develop a web scraping-based platform where users can compare product prices from different e-commerce websites.**

# Key Features

- User Authentication: Secure user registration and login.

- Real-Time Price Scraping: Automated data collection from popular e-commerce sites like Amazon, Flipkart, and others.

- Price Drop Alerts: Real-time notifications for price changes using Celery for background processing.

- Scalable Architecture: Efficient, containerized deployment using Docker and PostgreSQL for data storage.

**In the backend, use Celery to scrape product data from Amazon and Flipkart every hour, updating the latest prices and maintaining a price history and send price is less than last price than send notification to user.**

**Send a notification for every new user login with welcome message.**

# Installation Guide

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

```source myenv/bin/activate```  

**Setup your.env file**

**Run Project using Docker**

```docker-compose up --build -d```

- Run command for execute celery crontab

```docker-compose exec django celery -A price_comparison worker --loglevel=info```

```docker-compose down```

# Images

**Login Page**

![image](https://github.com/user-attachments/assets/6beb1575-f615-4d65-9352-ab0884ea23d6)

**Register Page**

![image](https://github.com/user-attachments/assets/10e9e518-f0b3-419f-a3e4-134d1c05079b)

**Search Page**

![image](https://github.com/user-attachments/assets/86717db1-0a1f-4195-b2f3-391c8fd1f157)

**Scraping Data into Amazone and Flipcart**

![image](https://github.com/user-attachments/assets/db22d390-ed1f-4d75-b6e2-901fe87aa8a1)

**Login User Product List**

![image](https://github.com/user-attachments/assets/4c78664e-9bf8-49eb-abeb-8a4bd8e68d2f)



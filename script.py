import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Number of unique transactions
num_unique_transactions = 50

# Number of customers and products
num_customers = 50
num_products = 20

# Generate Customer Dimension Table
customer_data = {
    "CustomerID": np.arange(1, num_customers + 1),
    "CustomerName": [fake.name() for _ in range(num_customers)],
    "CustomerEmail": [fake.email() for _ in range(num_customers)],
    "CustomerPhone": [fake.phone_number() for _ in range(num_customers)],
    "CustomerAddress": [fake.address() for _ in range(num_customers)],
}
df_customers = pd.DataFrame(customer_data)

# Sample product names and brands for different categories
products = {
    "Electronics": {
        "brands": ["Sony", "Samsung", "Apple", "LG", "Panasonic"],
        "products": ["Laptop", "Smartphone", "Headphones", "Camera", "Smartwatch"]
    },
    "Clothing": {
        "brands": ["Nike", "Adidas", "Zara", "H&M", "Uniqlo"],
        "products": ["T-Shirt", "Jeans", "Jacket", "Sweater", "Dress"]
    },
    "Home & Kitchen": {
        "brands": ["Philips", "KitchenAid", "Tefal", "Bosch", "Dyson"],
        "products": ["Blender", "Toaster", "Microwave", "Cookware Set", "Vacuum Cleaner"]
    },
    "Books": {
        "brands": ["Penguin", "HarperCollins", "Simon & Schuster", "Hachette", "Macmillan"],
        "products": ["Mystery Novel", "Science Fiction", "Biography", "Self-help Book", "Cookbook"]
    },
    "Toys": {
        "brands": ["Lego", "Mattel", "Hasbro", "Fisher-Price", "Playmobil"],
        "products": ["Action Figure", "Board Game", "Puzzle", "Doll", "Building Blocks"]
    }
}

# Flatten the products dictionary for product dimension
product_data = []
for category, items in products.items():
    for brand in items["brands"]:
        for product in items["products"]:
            product_data.append([len(product_data) + 1, category, brand, f"{brand} {product}"])

df_products = pd.DataFrame(product_data, columns=["ProductID", "ProductCategory", "BrandName", "ProductName"])

# Number of total transactions (rows in fact table)
num_transactions = 100

# Indian store names and cities
indian_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur"]
store_names = ["Big Bazaar", "Reliance Fresh", "DMart", "HyperCity", "More", "Star Bazaar", "Spencer's", "Easyday", "Metro", "Spar"]

# Generate unique transactions with multiple products
transaction_data = []
for transaction_id in range(100, 150 + 1):
    customer_id = random.choice(df_customers["CustomerID"])
    transaction_date = fake.date_between(start_date='-1y', end_date='today')
    store_location = f"{random.choice(store_names)}, {random.choice(indian_cities)}"
    payment_method = random.choice(["Credit Card", "Cash", "Online Payment", "Debit Card"])
    
    # Each transaction has multiple products
    num_items_in_transaction = random.randint(1, 5)
    for _ in range(num_items_in_transaction):
        product_id = random.choice(df_products["ProductID"])
        quantity = random.randint(1, 10)
        price = round(random.uniform(5.0, 100.0), 2)
        total_amount = quantity * price
        
        transaction_data.append([
            transaction_id, customer_id, transaction_date, product_id, 
            quantity, price, total_amount, payment_method, store_location
        ])

# Create the fact table DataFrame
df_fact = pd.DataFrame(transaction_data, columns=[
    "TransactionID", "CustomerID", "TransactionDate", "ProductID", 
    "Quantity", "Price", "TotalAmount", "PaymentMethod", "StoreLocation"
])

# Save to CSV
dim_customer_csv = "dim_customer.csv"
dim_product_csv = "dim_product.csv"
fact_retail_csv = "fact_retail_rd.csv"

df_customers.to_csv(dim_customer_csv, index=False)
df_products.to_csv(dim_product_csv, index=False)
df_fact.to_csv(fact_retail_csv, index=False)

(dim_customer_csv, dim_product_csv, fact_retail_csv)

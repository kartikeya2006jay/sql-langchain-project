import sqlite3 
conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_email TEXT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price_per_unit REAL,
    total_price REAL,
    order_date TEXT,
    city TEXT,
    state TEXT,
    payment_method TEXT,
    order_status TEXT,
    discount REAL,
    is_returned BOOLEAN
)
""")


cursor.executemany(
    """
    INSERT INTO orders (
        customer_name, customer_email, product_name, category,
        quantity, price_per_unit, total_price, order_date,
        city, state, payment_method, order_status,
        discount, is_returned
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    [
        ("Aarav Sharma", "aarav@gmail.com", "iPhone 15", "Electronics", 1, 80000, 80000, "2024-01-10", "Mumbai", "Maharashtra", "Credit Card", "Delivered", 0, 0),
        ("Priya Verma", "priya@gmail.com", "Nike Shoes", "Fashion", 2, 4000, 8000, "2024-01-12", "Delhi", "Delhi", "UPI", "Delivered", 500, 0),
        ("Rohan Gupta", "rohan@gmail.com", "Samsung TV", "Electronics", 1, 50000, 50000, "2024-01-15", "Bengaluru", "Karnataka", "Debit Card", "Shipped", 2000, 0),
        ("Sneha Reddy", "sneha@gmail.com", "Laptop", "Electronics", 1, 70000, 70000, "2024-01-18", "Hyderabad", "Telangana", "Credit Card", "Delivered", 1000, 0),
        ("Kunal Mehta", "kunal@gmail.com", "Handbag", "Fashion", 3, 2500, 7500, "2024-01-20", "Chennai", "Tamil Nadu", "Cash on Delivery", "Delivered", 0, 1),
        ("Ananya Iyer", "ananya@gmail.com", "Headphones", "Electronics", 2, 3000, 6000, "2024-01-22", "Pune", "Maharashtra", "UPI", "Cancelled", 0, 0),
        ("Vikram Singh", "vikram@gmail.com", "Watch", "Accessories", 1, 10000, 10000, "2024-01-25", "Kolkata", "West Bengal", "Debit Card", "Delivered", 500, 0),
        ("Meera Nair", "meera@gmail.com", "Refrigerator", "Appliances", 1, 45000, 45000, "2024-01-28", "Ahmedabad", "Gujarat", "Credit Card", "Delivered", 3000, 0),
        ("Arjun Patel", "arjun@gmail.com", "Sofa", "Furniture", 1, 30000, 30000, "2024-02-01", "Jaipur", "Rajasthan", "UPI", "Shipped", 2000, 0),
        ("Ishita Kapoor", "ishita@gmail.com", "Tablet", "Electronics", 2, 20000, 40000, "2024-02-05", "Lucknow", "Uttar Pradesh", "Credit Card", "Delivered", 1500, 0),
        ("Rahul Joshi", "rahul@gmail.com", "Air Conditioner", "Appliances", 1, 35000, 35000, "2024-02-08", "Noida", "Uttar Pradesh", "Debit Card", "Delivered", 2500, 0),
        ("Pooja Chawla", "pooja@gmail.com", "Dining Table", "Furniture", 1, 25000, 25000, "2024-02-10", "Indore", "Madhya Pradesh", "Cash on Delivery", "Shipped", 1000, 0),
        ("Manish Yadav", "manish@gmail.com", "Smartwatch", "Electronics", 2, 7000, 14000, "2024-02-12", "Patna", "Bihar", "UPI", "Delivered", 0, 0),
        ("Divya Malhotra", "divya@gmail.com", "Microwave Oven", "Appliances", 1, 12000, 12000, "2024-02-14", "Chandigarh", "Punjab", "Credit Card", "Delivered", 800, 0),
        ("Siddharth Rao", "sid@gmail.com", "Gaming Console", "Electronics", 1, 45000, 45000, "2024-02-16", "Visakhapatnam", "Andhra Pradesh", "Debit Card", "Cancelled", 0, 0),
    ]
)

conn.commit()
conn.close()

print("Indian E-commerce database initialized!")
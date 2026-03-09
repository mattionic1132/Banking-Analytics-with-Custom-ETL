"""
SIMPLE Banking Analytics Setup Script
======================================
This creates a small database with sample data for learning SQL

Run this to get started quickly!
"""

import sqlite3
from datetime import datetime, timedelta
import random

# Create database
print("Creating database...")
conn = sqlite3.connect('data/banking.db')
cursor = conn.cursor()

# Create tables
print("Creating tables...")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    customer_segment TEXT,
    customer_status TEXT,
    registration_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    account_type TEXT,
    current_balance DECIMAL(15,2),
    opening_date DATE,
    account_status TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    transaction_date TIMESTAMP,
    transaction_type TEXT,
    amount DECIMAL(15,2),
    channel TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS loans (
    loan_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    loan_type TEXT,
    loan_amount DECIMAL(15,2),
    interest_rate DECIMAL(5,4),
    loan_status TEXT,
    origination_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Create indexes
cursor.execute("CREATE INDEX IF NOT EXISTS idx_accounts_customer ON accounts(customer_id)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_transactions_account ON transactions(account_id)")

conn.commit()

# Generate simple sample data
print("Generating sample data...")

# Sample data arrays
first_names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
segments = ['Retail', 'Premium', 'VIP']
account_types = ['Checking', 'Savings', 'Money Market']
transaction_types = ['Deposit', 'Withdrawal', 'Transfer', 'Payment']
channels = ['Mobile', 'Online', 'ATM', 'Branch']
loan_types = ['Personal', 'Auto', 'Mortgage']

# Generate 100 customers
customers = []
for i in range(1, 1001):
    customer = (
        i,
        random.choice(first_names),
        random.choice(last_names),
        f"customer{i}@email.com",
        random.choice(segments),
        random.choice(['Active', 'Inactive']),
        (datetime.now() - timedelta(days=random.randint(30, 1000))).strftime('%Y-%m-%d')
    )
    customers.append(customer)

cursor.executemany("""
    INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)
""", customers)

print(f"✓ Created {len(customers)} customers")

# Generate 200 accounts (2 per customer on average)
accounts = []
account_id = 1
for customer_id in range(1, 1001):
    num_accounts = random.randint(1, 3)
    for _ in range(num_accounts):
        account = (
            account_id,
            customer_id,
            random.choice(account_types),
            round(random.uniform(100, 50000), 2),
            (datetime.now() - timedelta(days=random.randint(1, 900))).strftime('%Y-%m-%d'),
            'Active'
        )
        accounts.append(account)
        account_id += 1

cursor.executemany("""
    INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?)
""", accounts)

print(f"✓ Created {len(accounts)} accounts")

# Generate 1000 transactions
transactions = []
for i in range(1, 10001):
    trans = (
        i,
        random.randint(1, len(accounts)),
        (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d %H:%M:%S'),
        random.choice(transaction_types),
        round(random.uniform(10, 5000), 2),
        random.choice(channels)
    )
    transactions.append(trans)

cursor.executemany("""
    INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?)
""", transactions)

print(f"✓ Created {len(transactions)} transactions")

# Generate 30 loans
loans = []
for i in range(1, 31):
    loan = (
        i,
        random.randint(1, 100),
        random.choice(loan_types),
        round(random.uniform(5000, 100000), 2),
        round(random.uniform(0.03, 0.08), 4),
        random.choice(['Current', 'Paid Off']),
        (datetime.now() - timedelta(days=random.randint(30, 800))).strftime('%Y-%m-%d')
    )
    loans.append(loan)

cursor.executemany("""
    INSERT INTO loans VALUES (?, ?, ?, ?, ?, ?, ?)
""", loans)

print(f"✓ Created {len(loans)} loans")

conn.commit()
conn.close()

print("\n" + "="*50)
print("✅ DATABASE CREATED SUCCESSFULLY!")
print("="*50)
print(f"\nDatabase location: data/banking.db")
print("\nYou now have:")
print(f"  • {len(customers)} customers")
print(f"  • {len(accounts)} accounts")
print(f"  • {len(transactions)} transactions")
print(f"  • {len(loans)} loans")
print("\nNext steps:")
print("1. Open DB Browser for SQLite")
print("2. Open data/banking.db")
print("3. Start running SQL queries!")
print("\nExample query to try:")
print("  SELECT * FROM customers LIMIT 10;")
print()

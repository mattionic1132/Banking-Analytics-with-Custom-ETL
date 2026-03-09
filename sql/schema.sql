-- Banking Analytics Database Schema

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('M', 'F', 'Other')),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT DEFAULT 'USA',
    registration_date DATE NOT NULL,
    customer_status TEXT CHECK(customer_status IN ('Active', 'Inactive', 'Churned')) DEFAULT 'Active',
    customer_segment TEXT CHECK(customer_segment IN ('Retail', 'Premium', 'VIP')) DEFAULT 'Retail',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    account_type TEXT CHECK(account_type IN ('Checking', 'Savings', 'Money Market', 'CD')) NOT NULL,
    account_status TEXT CHECK(account_status IN ('Active', 'Closed', 'Frozen')) DEFAULT 'Active',
    opening_date DATE NOT NULL,
    closing_date DATE,
    current_balance DECIMAL(15, 2) DEFAULT 0.00,
    available_balance DECIMAL(15, 2) DEFAULT 0.00,
    interest_rate DECIMAL(5, 4) DEFAULT 0.0000,
    minimum_balance DECIMAL(15, 2) DEFAULT 0.00,
    monthly_fee DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    transaction_date TIMESTAMP NOT NULL,
    transaction_type TEXT CHECK(transaction_type IN ('Deposit', 'Withdrawal', 'Transfer', 'Payment', 'Fee', 'Interest')) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2),
    description TEXT,
    channel TEXT CHECK(channel IN ('ATM', 'Online', 'Mobile', 'Branch', 'Phone')) DEFAULT 'Online',
    merchant_category TEXT,
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_category TEXT CHECK(product_category IN ('Deposit', 'Loan', 'Credit Card', 'Investment', 'Insurance')) NOT NULL,
    product_type TEXT NOT NULL,
    interest_rate DECIMAL(5, 4),
    annual_fee DECIMAL(10, 2) DEFAULT 0.00,
    minimum_amount DECIMAL(15, 2),
    maximum_amount DECIMAL(15, 2),
    term_months INTEGER,
    product_status TEXT CHECK(product_status IN ('Active', 'Discontinued')) DEFAULT 'Active',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS loans (
    loan_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    loan_type TEXT CHECK(loan_type IN ('Personal', 'Auto', 'Mortgage', 'Student', 'Business')) NOT NULL,
    loan_amount DECIMAL(15, 2) NOT NULL,
    interest_rate DECIMAL(5, 4) NOT NULL,
    term_months INTEGER NOT NULL,
    monthly_payment DECIMAL(15, 2) NOT NULL,
    outstanding_balance DECIMAL(15, 2) NOT NULL,
    origination_date DATE NOT NULL,
    maturity_date DATE NOT NULL,
    loan_status TEXT CHECK(loan_status IN ('Current', 'Delinquent', 'Default', 'Paid Off', 'Charged Off')) DEFAULT 'Current',
    payment_due_date INTEGER CHECK(payment_due_date BETWEEN 1 AND 28),
    total_payments_made INTEGER DEFAULT 0,
    late_payments INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE INDEX IF NOT EXISTS idx_customers_status ON customers(customer_status);
CREATE INDEX IF NOT EXISTS idx_customers_segment ON customers(customer_segment);
CREATE INDEX IF NOT EXISTS idx_accounts_customer ON accounts(customer_id);
CREATE INDEX IF NOT EXISTS idx_transactions_account ON transactions(account_id);
CREATE INDEX IF NOT EXISTS idx_loans_customer ON loans(customer_id);
# Banking Customer Analytics - Data Engineering Project

A beginner-friendly end-to-end data engineering project built to learn SQL, Python, and ETL pipelines through hands-on practice with AI assistance.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![SQL](https://img.shields.io/badge/SQL-SQLite-lightgrey.svg)

---

## 🎯 Project Overview

This project simulates a complete banking analytics system with:
- **1,000+ customers** across different segments (Retail, Premium, VIP)
- **2,000+ accounts** (Checking, Savings, Money Market, CDs)
- **20,000+ transactions** with realistic patterns
- **100+ loans** across different types

**Learning Goal:** Build production-like data engineering skills from scratch by creating a realistic banking database, writing SQL queries, and developing ETL pipelines.

---

## 🛠️ Technology Stack

- **Database:** SQLite
- **Language:** Python 3.8+
- **Libraries:** pandas, numpy, matplotlib, seaborn, plotly, Faker
- **Tools:** Jupyter Notebook, DB Browser for SQLite

---

## 📁 Project Structure
```
banking_analytics_project/
├── data/
│   ├── banking.db                    # Main database
│   └── raw/                          # ETL source files
├── sql/
│   ├── schema.sql                    # Database schema
│   └── queries.sql                   # 22+ example queries
├── notebooks/
│   ├── 01_sql_exploration.ipynb      # SQL learning
│   ├── 02_data_analysis.ipynb        # EDA
│   └── 03_etl_project_1.ipynb        # ETL pipeline
├── quick_setup.py                    # Quick database setup
├── enhanced_data_generator.py         # Realistic data generator
├── requirements.txt                  # Dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/yourusername/banking-analytics-project.git
cd banking-analytics-project

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate Database
```bash
# Option 1: Quick setup (100 customers, fast)
python quick_setup.py

# Option 2: Enhanced setup (1000 customers, realistic)
python enhanced_data_generator.py
```

### 3. Explore the Data
```bash
# Open with DB Browser for SQLite, or:
sqlite3 data/banking.db
SELECT * FROM customers LIMIT 10;
```

---

## 📚 What I Built & Learned

### Part 1: Database Design & SQL

**Created:**
- Normalized relational schema (6 tables)
- Primary/foreign key relationships
- Indexes for performance
- Views for common queries

**Sample Query:**
```sql
-- Customer account summary with JOIN
SELECT 
    c.first_name,
    c.last_name,
    c.customer_segment,
    COUNT(a.account_id) as num_accounts,
    SUM(a.current_balance) as total_balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id
ORDER BY total_balance DESC
LIMIT 10;
```

**Skills:** SELECT, JOINs, GROUP BY, window functions, CTEs, query optimization

---

### Part 2: Data Generation

**Created:**
- Synthetic data generator using Faker library
- Realistic patterns (age distribution, income ranges)
- Customer behavior logic (VIP customers have higher balances)
- Time-series transaction data (2022-2024)

**Example:**
```python
# Generate realistic customer
customer = {
    'first_name': fake.first_name(),
    'email': fake.email(),
    'customer_segment': random.choices(['Retail', 'Premium', 'VIP'], 
                                       weights=[0.70, 0.25, 0.05])[0]
}
```

**Skills:** Python, Faker, data patterns, realistic simulation

---

### Part 3: Exploratory Data Analysis

**Analyzed:**
- Customer segmentation distribution
- Account balance patterns
- Transaction trends over time
- Channel usage preferences

**Example:**
```python
# Load data and analyze
conn = sqlite3.connect('data/banking.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)

# Customer segment distribution
customers_df['customer_segment'].value_counts().plot(kind='bar')
```

**Skills:** pandas, matplotlib, SQL+Python integration, data visualization

---

### Part 4: ETL Pipeline

**Built:** Multi-source data integration pipeline

**Scenario:** Bank acquired "Community Bank" with data in CSV, JSON, and Excel formats. Built pipeline to integrate their 500 customers into our system.

**Pipeline Steps:**
1. **Extract** - Read CSV, JSON, Excel files
2. **Transform** - Clean data, validate emails, remove duplicates
3. **Load** - Insert into database with error handling
4. **Report** - Generate execution statistics

**Example Output:**
```
=========================================================
ETL PIPELINE COMPLETED
=========================================================
Execution Statistics:
  Records Extracted:   300
  Records Loaded:      90
  Duplicates Removed:  8
  Errors Encountered:  2
Success Rate: 30.0%
=========================================================
```

**Skills:** ETL development, data quality validation, duplicate detection, error handling, logging

---

## 🎓 Key Learnings

### Technical Skills
- ✅ SQL: Schema design, complex queries, JOINs, window functions
- ✅ Python: pandas, data manipulation, file I/O
- ✅ ETL: Extract-Transform-Load pipelines
- ✅ Data Quality: Validation, deduplication, error handling

### Concepts Understood
- Database normalization and relationships
- Difference between simulated and real data
- Data quality importance (garbage in = garbage out)
- ETL pipeline architecture
- Production-like error handling

### Real-World Context
- How companies actually collect and store data
- OLTP (operational) vs OLAP (analytical) databases
- Why data pipelines are critical
- Data engineering best practices

---

## 📊 Sample Queries
```sql
-- 1. Total deposits by customer segment
SELECT 
    customer_segment,
    COUNT(*) as customers,
    SUM(current_balance) as total_deposits
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY customer_segment;

-- 2. Monthly transaction trends
SELECT 
    strftime('%Y-%m', transaction_date) as month,
    COUNT(*) as transaction_count,
    SUM(amount) as total_volume
FROM transactions
GROUP BY month
ORDER BY month DESC;

-- 3. Top 10 customers by balance
SELECT 
    c.first_name || ' ' || c.last_name as customer_name,
    SUM(a.current_balance) as total_balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id
ORDER BY total_balance DESC
LIMIT 10;
```

---

## 🔮 Future Enhancements

- [ ] Build dimensional data warehouse (star schema)
- [ ] Add real-time transaction processing pipeline
- [ ] Implement fraud detection algorithms
- [ ] Create Quarto dashboard for visualization
- [ ] Add machine learning (churn prediction)
- [ ] Integrate with cloud storage (AWS S3)

---

## 📝 Documentation

Detailed guides available in `docs/`:
- `DATABASE_DESIGN_GUIDE.md` - Database design tutorial
- `COMPLETE_SQL_SETUP_GUIDE.md` - Setup from scratch
- `HOW_REAL_COMPANIES_USE_DATA.md` - Real-world context
- `ETL_PROJECTS_GUIDE.md` - ETL documentation
- `data_dictionary.md` - Complete schema reference

---

## 🤝 Learning Approach

This project was built through **AI-assisted learning**:
- Started with "I want to learn SQL"
- Asked questions, debugged errors, learned concepts
- Built progressively: SQL → Data Generation → Analysis → ETL
- Focused on understanding "why" not just "how"

**What worked:**
- Starting simple and adding complexity
- Building real projects instead of tutorials
- Asking questions when stuck
- Documenting the journey

---

## 💼 For Recruiters

**This project demonstrates:**
- SQL proficiency (schema design to complex queries)
- Python + data engineering skills
- ETL pipeline development
- Data quality management
- Self-directed learning ability
- Production-like code quality

**Interview talking points:**
- Database design decisions
- ETL architecture choices
- Data quality strategies
- How to scale from 100 to 1M+ records

---

## ⭐ Acknowledgments

Built with curiosity, iteration, and AI assistance (Claude by Anthropic). 

If this helped you learn data engineering, feel free to ⭐ star and fork!

---

*A beginner's journey into data engineering - built to learn, documented to share.*

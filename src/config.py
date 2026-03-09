"""
Configuration settings for Banking Analytics Project
"""
import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'

# Database configuration
DATABASE_PATH = DATA_DIR / 'banking.db'
DATABASE_URL = f'sqlite:///{DATABASE_PATH}'

# Data generation settings
RANDOM_SEED = 42
NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 20
TRANSACTION_START_DATE = '2022-01-01'
TRANSACTION_END_DATE = '2024-12-31'

# Customer segment distribution (percentages)
SEGMENT_DISTRIBUTION = {
    'Retail': 0.70,
    'Premium': 0.25,
    'VIP': 0.05
}

# Account type distribution
ACCOUNT_TYPE_DISTRIBUTION = {
    'Checking': 0.50,
    'Savings': 0.35,
    'Money Market': 0.10,
    'CD': 0.05
}

# Transaction channel distribution
CHANNEL_DISTRIBUTION = {
    'Mobile': 0.45,
    'Online': 0.30,
    'ATM': 0.15,
    'Branch': 0.08,
    'Phone': 0.02
}

# Analysis parameters
CHURN_THRESHOLD_DAYS = 90
RFM_QUANTILES = 4

# Visualization settings
PLOT_STYLE = 'seaborn-v0_8-darkgrid'
COLOR_PALETTE = 'husl'
FIGURE_DPI = 100

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
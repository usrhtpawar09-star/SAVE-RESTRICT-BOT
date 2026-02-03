"""
Save Restricted Content Bot Configuration

Developed by: usrht
Telegram: @usrhtff09

Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8243335683:AAG2TZVHBoqiDadEKhEkWk_6t1NphWjFFK8")
API_ID = int(os.environ.get("API_ID", "36455116"))
API_HASH = os.environ.get("API_HASH", "dddbb57121805c7b1434734390ff2e08")


# ==============================
# Admin Configuration
# ==============================

# Add admin user IDs separated by commas in environment variables
ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "8327837344").split(",") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "mongodb+srv://dbm491565_db_user:ffVHN5tdzA8wpd6l@cluster0.r1gowvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted2")


# ==============================
# Logging Configuration
# ==============================

# Replace with your Telegram log channel ID (example: -1001234567890)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))


# ==============================
# Error Handling
# ==============================

# Set to True to send error messages to users
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"

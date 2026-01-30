"""
Configuration for SHEIN Verse Product Monitor Bot
Works on Termux + Railway
Compatible with python-telegram-bot v20+
"""

import os
from pathlib import Path

# --------------------------------------------------
# Load .env file (for Termux / local use)
# Railway uses environment variables directly
# --------------------------------------------------
try:
    from dotenv import load_dotenv
    env_path = Path(".") / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        print("[CONFIG] Loaded .env file")
except Exception:
    pass

# --------------------------------------------------
# TELEGRAM CONFIGURATION
# --------------------------------------------------

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN",
    "7201368733:AAG3Yp-E5g-DExLHEN-ETrv74zeqwuTIhNM"
)

if not TELEGRAM_BOT_TOKEN or ":" not in TELEGRAM_BOT_TOKEN:
    raise RuntimeError("Invalid TELEGRAM_BOT_TOKEN")

# Allowed Telegram User IDs (admins)
TELEGRAM_CHAT_IDS = os.getenv(
    "TELEGRAM_CHAT_IDS",
    "7194175926,1950577113"
).split(",")

TELEGRAM_CHAT_IDS = [cid.strip() for cid in TELEGRAM_CHAT_IDS]

# --------------------------------------------------
# SCRAPER CONFIGURATION
# --------------------------------------------------

# Maximum products to scrape per run
MAX_PRODUCTS = int(os.getenv("MAX_PRODUCTS", "90"))

# Interval between checks (minutes)
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", "1"))

# Cache expiry time (minutes)
CACHE_EXPIRY_MINUTES = int(os.getenv("CACHE_EXPIRY_MINUTES", "10"))

# --------------------------------------------------
# HUMAN-LIKE DELAYS (seconds)
# --------------------------------------------------

DEFAULT_WAIT_MIN = float(os.getenv("DEFAULT_WAIT_MIN", "1.5"))
DEFAULT_WAIT_MAX = float(os.getenv("DEFAULT_WAIT_MAX", "3.0"))

# --------------------------------------------------
# DATABASE CONFIGURATION
# --------------------------------------------------

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "./shein_monitor.db"
)

# --------------------------------------------------
# LOGGING
# --------------------------------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# --------------------------------------------------
# STARTUP DEBUG INFO
# --------------------------------------------------

print("[CONFIG] Token loaded ✔")
print("[CONFIG] Allowed users:", TELEGRAM_CHAT_IDS)
print("[CONFIG] Max products:", MAX_PRODUCTS)
print("[CONFIG] Check interval:", CHECK_INTERVAL_MINUTES, "minute(s)")
print("[CONFIG] Cache expiry:", CACHE_EXPIRY_MINUTES, "minutes")
print("[CONFIG] Database path:", DATABASE_PATH)
print("[CONFIG] Log level:", LOG_LEVEL)

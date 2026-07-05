
import os

# ==========================
# Telegram
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==========================
# APIs
# ==========================

SILVER_API = "https://api.metals.live/v1/spot/silver"

# ==========================
# تحلیل
# ==========================

# ضریب ارزش منصفانه بازار ایران
MARKET_PREMIUM = 3.2

# محدوده‌های تصمیم
BUY_LIMIT = -10
NORMAL_LIMIT = 15

# ==========================
# زمان‌بندی
# ==========================
REQUEST_TIMEOUT = 15

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36"

MAX_RETRY = 3

REPORT_HOUR = 12
REPORT_MINUTE = 0

# ==========================
# منابع قیمت
# ==========================

PRICE_SOURCES = [
    "https://www.tgju.org/profile/silver_999",
    "https://tajnoghreh.com/silver-price/"
]

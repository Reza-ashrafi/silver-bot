import requests
from bs4 import BeautifulSoup

def get_silver_price():
    try:
        url = "https://www.tgju.org/profile/silver_999"
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")

        price_tag = soup.find("span", {"data-col": "info.last"})
        if not price_tag:
            return None

        price_text = price_tag.text.replace(",", "").strip()
        return float(price_text)

    except Exception as e:
        print("SILVER ERROR:", e)
        return None


def analyze():
    silver = get_silver_price()

    if not silver:
        return {
            "silver": 0,
            "usd": 0,
            "intrinsic": 0,
            "market": 0,
            "bubble": 0,
            "score": 0,
            "decision": "❌ دیتا در دسترس نیست (خطا در دریافت قیمت)"
        }

    usd = 60000  # فعلاً ثابت برای جلوگیری از خطا

    intrinsic = silver * usd
    market = intrinsic * 1.05  # شبیه‌سازی ساده

    bubble = ((market - intrinsic) / intrinsic) * 100

    score = max(0, 100 - abs(bubble) * 10)

    decision = "📈 مناسب بررسی خرید" if bubble < 5 else "⚠️ حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }
    intrinsic = intrinsic_value(silver, usd)

    # =========================
    # ارزش منصفانه بازار ایران
    # =========================
    fair_value = intrinsic * MARKET_PREMIUM

    bubble = ((market - fair_value) / fair_value) * 100

    # =========================
    # امتیاز خرید (0 تا 100)
    # =========================
    score = 100

    # هر چی حباب بیشتر → امتیاز کمتر
    if bubble > 0:
        score -= bubble * 2

    # محدودسازی
    if score < 0:
        score = 0
    if score > 100:
        score = 100

    # =========================
    # تصمیم نهایی
    # =========================
    if bubble < BUY_LIMIT:
        decision = "🟢 فرصت خرید خوب"
    elif bubble < NORMAL_LIMIT:
        decision = "🟡 نرمال / بررسی بیشتر"
    else:
        decision = "🔴 پرریسک / حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "market": market,
        "intrinsic": intrinsic,
        "fair_value": fair_value,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }

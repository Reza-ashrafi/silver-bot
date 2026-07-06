import requests

def get_silver_price():
    try:
        url = "https://www.tgju.org/profile/silver_999"
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        text = r.text

        # خیلی ساده و مقاوم (بدون BeautifulSoup حساس)
        import re
        match = re.search(r'data-col="info.last".*?>([\d,]+)</span>', text)

        if not match:
            return None

        return float(match.group(1).replace(",", ""))

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
            "decision": "❌ خطا در دریافت قیمت نقره (سایت در دسترس نیست)"
        }

    usd = 60000

    intrinsic = silver * usd
    market = intrinsic * 1.03

    bubble = ((market - intrinsic) / intrinsic) * 100 if intrinsic else 0
    score = max(0, 100 - abs(bubble) * 10)

    decision = "📈 مناسب بررسی" if bubble < 5 else "⚠️ حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
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

def analyze():
    print("ANALYZE CALLED")

    silver = 28.5
    usd = 60000

    intrinsic = silver * usd
    market = intrinsic * 1.03

    fair_value = intrinsic * 1.02

    bubble = ((market - fair_value) / fair_value) * 100

    score = 100 - abs(bubble) * 2

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    if bubble < 5:
        decision = "🟢 فرصت خرید خوب"
    elif bubble < 15:
        decision = "🟡 نرمال"
    else:
        decision = "🔴 پرریسک / حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "fair_value": fair_value,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }

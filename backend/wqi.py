def classify_wqi(wqi):

    if wqi <= 50:
        return "Excellent"

    elif wqi <= 100:
        return "Good"

    elif wqi <= 200:
        return "Poor"

    elif wqi <= 300:
        return "Very Poor"

    else:
        return "Unsuitable"


def calculate_wqi(
    ph,
    nitrate,
    do,
    tds,
    turbidity,
    ammonia,
    fluoride
):

    wqi = (
        (ph * 0.1) +
        (nitrate * 0.2) +
        (do * 0.2) +
        (tds * 0.1) +
        (turbidity * 0.1) +
        (ammonia * 0.15) +
        (fluoride * 0.15)
    )

    return round(wqi, 2)
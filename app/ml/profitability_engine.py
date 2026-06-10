def calculate_profitability(
    revenue,
    operating_cost
):

    profit = revenue - operating_cost

    margin = 0

    if revenue > 0:
        margin = (profit / revenue) * 100

    return {
        "profit": round(profit, 2),
        "margin": round(margin, 2)
    }
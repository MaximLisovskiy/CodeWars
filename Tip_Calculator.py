import math
import time


def calculate_tip(amount, rating):
    if rating.lower() == "terrible":
        return 0
    if rating.lower() == "poor":
        return math.ceil((amount * 5) / 100)
    if rating.lower() == "good":
        return math.ceil((amount * 10) / 100)
    if rating.lower() == "great":
        return math.ceil((amount * 15) / 100)
    if rating.lower() == "excellent":
        return math.ceil((amount * 20) / 100)
    else:
        return "Rating not recognised"


print(calculate_tip(107.65, "GReat"))  # -> 2

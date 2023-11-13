import json


def task() -> float:
    with open("input.json", "r") as input_f:
        data = json.load(input_f)

    total = 0.0
    for review in data:
        score = review["score"]
        weight = review["weight"]
        product = score * weight
        total += product

    return round(total, 3)

print(task())

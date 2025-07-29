
# This script simulates generating training data and retraining
import json
import random

cars = list("ABCDEFGH")

def generate_example():
    random.shuffle(cars)
    return {
        "input": cars.copy(),
        "output": random.sample(cars, 5)
    }

data = [generate_example() for _ in range(10)]

with open("feedback.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Training data generated.")

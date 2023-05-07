import random

NUM_QUICK_PICKS = 5
NUMBERS_PER_PICK = 6
MIN_NUM = 1
MAX_NUM = 45

# Generate the quick picks
quick_picks = []
for i in range(NUM_QUICK_PICKS):
    # Generate a random list of unique numbers
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    quick_picks.append(numbers)

# Display the quick picks
print(f"How many quick picks? {NUM_QUICK_PICKS}")
for numbers in quick_picks:
    print(" ".join(f"{num:2}" for num in numbers))

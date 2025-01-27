# region imports
from random import random
# endregion

# region functions
def rollFairDie():
    """
    Simulates rolling a fair die with equal probability (1/6) for each face.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()  # Random float between 0.0 and 1.0
    if x <= 1 / 6:
        return 1
    elif x <= 2 / 6:
        return 2
    elif x <= 3 / 6:
        return 3
    elif x <= 4 / 6:
        return 4
    elif x <= 5 / 6:
        return 5
    else:
        return 6


def rollUnFairDie():
    """
    Simulates rolling an unfair die where the probability of rolling a 1 is 0.2,
    and the probability of rolling each number from 2–6 is equal (0.8/5 each).
    :return: an integer between 1 and 6 inclusive
    """
    x = random()  # Random float between 0.0 and 1.0
    if x <= 0.2:  # Probability of 1
        return 1
    elif x <= 0.2 + 0.8 / 5:  # Probability of 2
        return 2
    elif x <= 0.2 + 2 * (0.8 / 5):  # Probability of 3
        return 3
    elif x <= 0.2 + 3 * (0.8 / 5):  # Probability of 4
        return 4
    elif x <= 0.2 + 4 * (0.8 / 5):  # Probability of 5
        return 5
    else:  # Remaining probability for 6
        return 6
# endregion

# Main guarding
if __name__ == "__main__":
    print("Rolling fair die:")
    for _ in range(5):  # Test 5 rolls
        print(rollFairDie())

    print("\nRolling unfair die:")
    for _ in range(5):  # Test 5 rolls
        print(rollUnFairDie())

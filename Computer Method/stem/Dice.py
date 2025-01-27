##For this, I work with Brian and use chatgpt
# region imports
import random

# Mocking the Die module with local class definitions
class FairDie:
    @staticmethod
    def roll():
        return random.randint(1, 6)  # Simulate a fair die roll

class UnFairDie:
    @staticmethod
    def roll():
        weights = [0.2, 0.16, 0.16, 0.16, 0.16, 0.16]  # Probabilities for each face 1 through 6
        return random.choices(range(1, 7), weights=weights)[0]
# endregion

# region functions
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    :return: an integer between 1 and 6 inclusive
    """
    x = random.random()  # Generate a random float between 0.0 and 1.0
    if x <= 1.0 / 6:
        return 1
    elif x <= 2.0 / 6:
        return 2
    elif x <= 3.0 / 6:
        return 3
    elif x <= 4.0 / 6:
        return 4
    elif x <= 5.0 / 6:
        return 5
    else:
        return 6

def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2.
    All other integers have equal probability (0.16 each for 2-6).
    :return: an integer between 1 and 6 inclusive
    """
    x = random.random()  # Generate a random float between 0.0 and 1.0
    if x <= 0.2:
        return 1
    else:
        # Map the remaining range to 2-6
        return 2 + int((x - 0.2) // (0.8 / 5))

def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    total_score = 0
    for _ in range(N):
        total_score += FairDie.roll()  # Using the mocked FairDie class
    return total_score

def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    total_score = 0
    for _ in range(N):
        total_score += UnFairDie.roll()  # Using the mocked UnFairDie class
    return total_score
# endregion

# region main
if __name__ == "__main__":
    # Simulate a single roll of a fair die
    print("Fair Die Roll:", rollFairDie())

    # Simulate a single roll of an unfair die
    print("UnFair Die Roll:", rollUnFairDie())

    # Simulate rolling 5 fair dice
    print("Total score after rolling 5 Fair Dice:", rollDice(N=5))

    # Simulate rolling 5 unfair dice
    print("Total score after rolling 5 UnFair Dice:", rollUnFairDice(N=5))
# endregion

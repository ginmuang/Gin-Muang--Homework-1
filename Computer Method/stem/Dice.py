# region imports
# Mocking the Die module with local class definitions
class FairDie:
    @staticmethod
    def roll():
        import random
        return random.randint(1, 6)  # Simulate a fair die roll

class UnFairDie:
    @staticmethod
    def roll():
        import random
        weights = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]  # Probabilities for each face 1 through 6
        return random.choices(range(1, 7), weights=weights)[0]
# endregion

# region functions
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


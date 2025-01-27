import random  # region imports
# endregion

# region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 2  # number of dice
    nMinScore = nDice * 1  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1  # number of possible scores
    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 10000  # how many times to roll the dice

    for _ in range(nRolls):  # each loop rolls dice and increments a score
        score = sum(random.randint(1, 6) for _ in range(nDice))  # roll nDice times and sum up
        nTally[score - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start

    print("After {} rolls of {} fair dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = i + nMinScore
        probability = nTally[i] / nRolls
        print(f"Score {score}: {probability:.2f}")

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 2  # number of dice
    nMinScore = nDice * 1  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1  # number of possible scores
    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 10000  # how many times to roll the dice

    # Assuming each die has different probabilities for each face
    weights = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]  # Probabilities for 1, 2, 3, 4, 5, 6

    for _ in range(nRolls):  # each loop rolls dice and increments a score
        score = sum(random.choices(range(1, 7), weights=weights)[0] for _ in range(nDice))  # roll nDice times
        nTally[score - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start

    print("After {} rolls of {} unfair dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = i + nMinScore
        probability = nTally[i] / nRolls
        print(f"Score {score}: {probability:.2f}")

# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()

##Use the help of ChatGPT for every problem for HW1
import random  # region imports


# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc. Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = random.randint(1, 6)  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

    # print the result
    for i in range(6):
        print(f"Probability of rolling {i + 1}: {scores[i] / n:.2f}")


def main2():
    """
    This function rolls a fair die 10000 times and tallies the number of 1's, 2's etc. Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6
    n = 10000
    for i in range(n):
        score = random.randint(1, 6)
        scores[score - 1] += 1

    for i in range(6):
        print(f"Probability of rolling {i + 1}: {scores[i] / n:.2f}")


def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc. Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    # Assuming we have predefined weights for the unfair die
    weights = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]  # Probabilities for 1, 2, 3, 4, 5, 6
    scores = [0] * 6
    n = 10000
    for i in range(n):
        score = random.choices(range(1, 7), weights=weights)[0]
        scores[score - 1] += 1

    for i in range(6):
        print(f"Probability of rolling {i + 1}: {scores[i] / n:.2f}")


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()

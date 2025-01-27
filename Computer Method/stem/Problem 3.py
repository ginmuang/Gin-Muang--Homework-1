# region imports
import random as rnd
# endregion

# region functions
def between(num, low, high, inclusivelow=True, inclusivehigh=True):
    """
    Returns a boolean indicating if num is in the range [low, high].
    :param num: the number to check
    :param low: the low end of the range
    :param high: the high end of the range
    :param inclusivelow: bool to include the low end
    :param inclusivehigh: bool to include the high end
    :return: bool indicating if between low and high limits
    """
    if inclusivelow and inclusivehigh:
        return low <= num <= high
    elif inclusivelow:
        return low <= num < high
    elif inclusivehigh:
        return low < num <= high
    else:
        return low < num < high

def main():
    """
    Generates an array of numbers from a normally distributed population and checks
    the percentage within 1, 2, and 3 standard deviations of the mean.
    :return: nothing
    """
    N = 1000  # size of array
    mean = 0  # the mean of the normal distribution
    stdev = 1  # the standard deviation

    bin1 = 0  # normal dist should contain 68% within +/-1stdev
    bin2 = 0  # normal dist should contain 95.5% within +/-2stdev
    bin3 = 0  # normal dist should contain 99.7% within +/-3stdev

    # find edges of the limits for the various bins
    bin1low = mean - stdev
    bin1high = mean + stdev

    bin2low = mean - 2 * stdev
    bin2high = mean + 2 * stdev

    bin3low = mean - 3 * stdev
    bin3high = mean + 3 * stdev

    arr = []  # array for storing the numbers
    for i in range(N):  # this loop generates the numbers
        num = rnd.gauss(mean, stdev)  # generate a number from normal distribution
        arr.append(num)

        # check which bin(s) the current number is in
        if between(num, bin1low, bin1high):
            bin1 += 1
        if between(num, bin2low, bin2high):
            bin2 += 1
        if between(num, bin3low, bin3high):
            bin3 += 1

    # Uncomment to see the actual array
    # print(arr)
    print("{:.1f}% of data within +/-1 StDev of mean.".format(100 * bin1 / N))
    print("{:.1f}% of data within +/-2 StDev of mean.".format(100 * bin2 / N))
    print("{:.1f}% of data within +/-3 StDev of mean.".format(100 * bin3 / N))

# endregion

if __name__ == "__main__":
    main()  # calls the function main

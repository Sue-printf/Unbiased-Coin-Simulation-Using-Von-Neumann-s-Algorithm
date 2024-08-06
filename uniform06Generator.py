# Import the unbiasedCoin function from another file
from unbiased_coin_simulation import unbiasedCoin

# Define the uniform06Generator function
def uniform06Generator():
    # Toss the unbiased coin three times
    toss1 = unbiasedCoin()
    toss2 = unbiasedCoin()
    toss3 = unbiasedCoin()

    # Map the sequence of three outcomes to a number in {0, 1, 2, 3, 4, 5, 6}
    if toss1 == 'head' and toss2 == 'head' and toss3 == 'head':
        return 0
    elif toss1 == 'head' and toss2 == 'head' and toss3 == 'tail':
        return 1
    elif toss1 == 'head' and toss2 == 'tail' and toss3 == 'head':
        return 2
    elif toss1 == 'head' and toss2 == 'tail' and toss3 == 'tail':
        return 3
    elif toss1 == 'tail' and toss2 == 'head' and toss3 == 'head':
        return 4
    elif toss1 == 'tail' and toss2 == 'head' and toss3 == 'tail':
        return 5
    else:  # toss1 == 'tail' and toss2 == 'tail' and toss3 == 'tail'
        return 6

# Test the uniform06Generator function
num_trials = 10000
counts = [0] * 7  # Initialize counts for each number from 0 to 6

for _ in range(num_trials):
    result = uniform06Generator()
    counts[result] += 1

# Calculate probabilities
probabilities = [count / num_trials for count in counts]

# Print results
for number, probability in enumerate(probabilities):
    print(f"Probability of {number}: {probability}")

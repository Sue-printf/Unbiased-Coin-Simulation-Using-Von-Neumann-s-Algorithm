import random

def biasedCoin():
    p = 0.8
    return 'head' if random.random() < p else 'tail'

def unbiasedCoin():
    while True:
        outcome1 = biasedCoin()
        outcome2 = biasedCoin()
        if outcome1 != outcome2:
            return 'head' if outcome1 == 'head' else 'tail'

# Proof that unbiasedCoin() is unbiased
# Let's define the events:
# H: Getting a head
# T: Getting a tail

# We want to show that P(H) = P(T) = 0.5

# From the given biased coin function:
# P(head) = 0.8
# P(tail) = 0.2

# In Von Neumann's algorithm, we consider pairs of outcomes from the biased coin
# and discard the pairs with the same outcome (HH or TT).
# The remaining pairs are either HT or TH.

# P(HT) = P(head) * P(tail) = 0.8 * 0.2 = 0.16
# P(TH) = P(tail) * P(head) = 0.2 * 0.8 = 0.16

# Since P(HT) = P(TH), the probability of getting a head or a tail after discarding
# the pairs with the same outcome is equal to 0.5.

# P(H) = P(HT) + P(TH) = 0.16 + 0.16 = 0.32 / 0.32 + 0.32 = 0.5
# P(T) = P(TH) + P(HT) = 0.16 + 0.16 = 0.32 / 0.32 + 0.32 = 0.5

# Therefore, the probability of getting a head or a tail using unbiasedCoin() is 0.5,
# which means it is an unbiased coin.

# Generate random tosses and report the number of heads and tails
for n in [10, 100, 1000, 10000, 1000000]:
    heads, tails = 0, 0
    for _ in range(n):
        outcome = unbiasedCoin()
        if outcome == 'head':
            heads += 1
        else:
            tails += 1
    print(f"For {n} tosses, heads: {heads}, tails: {tails}")
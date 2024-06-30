import random
"""on average, how many flips are needed for the sequence to contain both 
heads and tails?"""


def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


sequence = 0
flip = 0

for trial in range(10_000):
    n = coin_flip()
    flip += 1
    while coin_flip() == n:
        flip += 1
    sequence += 1
    flip += 1


print(f"Flips: {flip}\nSequence: {sequence}\nAverage: {flip/sequence}")

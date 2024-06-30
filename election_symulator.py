# simulation of election between two candidates
# candidate A and candidate B
# A - region 1: 87% chance of winning, region 2: 65%, region 3: 17%
# write a program that simulates the election 10,000 times and prints the
# percentage of where candidate A wins. win when win in at least 2 regions


import random


def voting(chances_a):
    """returns randomly A or B"""
    if random.random() < chances_a:
        return 'A'
    else:
        return 'B'


wins_a = 0

for trial in range(10_000):
    votes_a = 0
    if voting(.87) == 'A':
        votes_a += 1
    if voting(.65) == 'A':
        votes_a += 1
    if voting(.17) == 'A':
        votes_a += 1
    if votes_a >= 2:
        wins_a += 1

print(f"A wins: {wins_a}\nPercentage: {wins_a/10_000:%}")

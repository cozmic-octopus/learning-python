import random


nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes",
         "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against",  "after",  "into", "beneath", "upon", "for", "in", "like",
                "over", "within"]
adverbs = ["curiously",  "extravagantly", "tantalizingly", "furiously", "sensuously"]

adj1 = random.choice(adjectives)
adj2 = random.choice(adjectives)
adj3 = random.choice(adjectives)
noun1 = random.choice(nouns)
noun2 = random.choice(nouns)
noun3 = random.choice(nouns)
verb1 = random.choice(verbs)
verb2 = random.choice(verbs)
verb3 = random.choice(verbs)
prep1 = random.choice(prepositions)
prep2 = random.choice(prepositions)
adverb1 = random.choice(adverbs)

if adj1 == "incredulous" or adj1 == "exuberant":
    an = "An"
else:
    an = "A"
print(f"{an} {adj1} {noun1}\n")
print(f"{an} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
print(f"{adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")

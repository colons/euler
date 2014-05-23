from common import alphabet


with open('p22.names.txt') as namefile:
    names = sorted([n.strip('"') for n in namefile.read().split(',')])


def score_for(name):
    score = 0

    for letter in name.lower():
        score += (alphabet.index(letter) + 1)

    return score * (names.index(name) + 1)


total_score = 0

for name in names:
    total_score += score_for(name)

print total_score

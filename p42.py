from common import alphabet

triangle_cache = []


def triangle(n):
    return int(n/2. * (n + 1))


def is_triangle(n):
    while (not triangle_cache) or triangle_cache[-1] < n:
        triangle_cache.append(triangle(len(triangle_cache)))

    return n in triangle_cache


def word_value(word):
    value = 0

    for letter in word.lower():
        value += alphabet.index(letter) + 1

    return value


with open('p42.words.txt') as wordfile:
    words = [w.strip('"') for w in wordfile.read().split(',')]


count = 0


for word in words:
    if is_triangle(word_value(word)):
        count += 1


print count

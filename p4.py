from common import is_palindrome


if __name__ == '__main__':
    pool = range(100, 1000)

    palindromes = []

    for x, y in [(x, y) for x in pool for y in pool]:
        product = x * y
        word = str(product)

        if is_palindrome(word):
            palindromes.append(product)

    print max(palindromes)

pool = range(100,1000)

def is_palindrome(word):
    rev = ''
    for l in word:
        rev = l+rev

    if rev == word:
        return True
    else:
        return False

palindromes = []

for x, y in [(x, y) for x in pool for y in pool]:
    product = x * y
    word = str(product)

    if is_palindrome(word):
        palindromes.append(product)

print max(palindromes)

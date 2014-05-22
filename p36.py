from p4 import is_palindrome


total = 0

for i in xrange(10**6 + 1):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        total += i

print total

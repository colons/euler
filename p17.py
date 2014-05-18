ones = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def wordify(number):
    number_string = str(number)

    if number < 10:
        return ones[number]

    elif 10 < number < 20:
        return teens[number-10]

    elif number < 100:
        return tens[int(number_string[-2])] + wordify(int(number_string[-1]))

    elif number < 1000:
        hundred_count = wordify(int(number_string[-3])) + 'hundred'
        if number % 100 == 0:
            return hundred_count
        else:
            return hundred_count + 'and' + wordify(int(number_string[-2:]))

    elif number == 1000:
        return 'onethousand'


letters = 0

for i in xrange(1, 1001):
    word = wordify(i)
    letters += len(word)

print letters

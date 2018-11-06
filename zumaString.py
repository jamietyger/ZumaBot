import re
import random


ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]

twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]

thousands = ["","thousand ","million ", "billion ", "trillion "]


def num999(n):
    c = n % 10 # singles digit
    b = ((n % 100) - c) / 10 # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[int(a)] + "hundred "
    elif a != 0:
        t = ones[int(a)] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[int(b)] + ones[int(c)]
    st = t + h
    return st

def num2word(num):
    if num == 0:
        return 'zero'
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    return word[:-1]

def main():
    text = input('Enter message: ')
    print(zumify(text))

def zumify(num):
    var = (int(float(num)))
    random.shuffle(thousands)
    return  num2word(var)
#main()

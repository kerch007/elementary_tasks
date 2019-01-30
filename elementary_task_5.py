#!/usr/bin/env python
# coding: utf-8

# In[5]:


ONES = [None, 'один', 'два', 'три', 'четыре',
    'пять', 'шесть', 'семь', 'восемь', 'девять']

TEENS = ['десять', 'одиннадцать', 'двеннадцать', 'тринадцать', 'четырнадцать',
    'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']

TENS = [None, None, 'двадцать', 'тридцать', 'сорок',
    'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

HUNDREDS = [None, "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

POWERS_OF_1000 = ['', ' тысяч', ' миллион', ' миллиард', ' триллион', ' квадрильон', ' квинтилион', ' секстиллион', 
                  ' септилион', ' октилион']

ZERO = ['ноль']
def number_to_chunks(number):
    try:
        while number >0:
            number, n = divmod(number, 1000)
            yield n
    except:
        print("No.. incorrect input. Please enter positive number")

def words_1_to_999(a, i=1):
    try:
        if a==0:
            return (ZERO[0])
        if a <0:
            print('Enter positive number')
        else:
            n_100 = a // 100
            n_10 = a % 100 // 10
            n_1 = a % 10
            res = []

        res.append(HUNDREDS[n_100])
        gender_digits=ONES
        if n_10 == 1:
            res.append(gender_digits[10*n_10 + n_1])
        else:
            res.append(TENS[n_10])
        res.append(gender_digits[n_1])
        return(" ".join([s for s in res if s != None]))
    except :
       print("No.. incorrect input. Please enter positive number")

def number_to_words(number=None):
    try:
        if number == None:
            print('Please enter positive number and you will get this number in words')

        if number == 0:
            return (ZERO[0])
        res = []
        for i, chunk in enumerate(number_to_chunks(number)):
            res.append(words_1_to_999(chunk, i))
            res[i] = res[i]+str(POWERS_OF_1000[i])


            if i == 1:
                if chunk % 10 == 1:
                    res[i] = res[i] + 'а'
                if 2 <= chunk % 10 <=4 :
                    res[i] = res[i] + 'и'
            if i > 1:
                if 5 <= chunk % 10 <= 9:
                    res[i] = res[i] + 'ов'
                if 2 <= chunk % 10 <=4 :
                    res[i] = res[i] + 'а'
        result = " ".join([s for s in res[::-1] if s != None])
        result = result.replace('два тысячи', 'две тысячи')
        result = result.replace('один тысяча', 'одна тысяча')
        return (result)
    except :
       print("No.. incorrect input. Please enter positive number")


if __name__ == "__main__":

    print(number_to_words(135254))


from itertools import product

vowel = ['A','E','I','O','U']
lst = []
for i in range(1,6):
    for item in product(vowel, repeat = i):
        lst.append(item)
lst.sort()

def solution(word):
    wordtp = []
    for j in word:
        wordtp.append(j)
    wordtp = tuple(wordtp)
    answer = lst.index(wordtp)+1
    return answer

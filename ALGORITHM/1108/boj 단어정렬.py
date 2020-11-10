import sys
sys.stdin = open('boj 단어정렬.txt')

N = int(input())

words = list()

for n in range(N):
    word = input()
    word_length =len(word)
    words.append((word,word_length))
words_list = list(set(words))
# print(words)
# print(words_list)
words_list.sort(key= lambda x : (x[1],x[0]))

for a,b in words_list:
    print(a)
import sys
sys.stdin = open('BOJ 1152 단어의 개수.txt')

sentence = input()
word = sentence.count(" ")+1
if sentence.startswith(" ") == True:
    word = word-1
if sentence.endswith(" ") == True:
    word = word-1
print(word)
import sys
sys.stdin = open()


answer = []
person1 = '12345'
person2 = '21232425'
person3 = '3311224455'
scores = [0, 0, 0]

cnt = 0
while answers:
    a = answers.pop(0)
    if a == person1[cnt % 5]:
        scores[0] += 1
    if a == person2[cnt % 8]:
        scores[1] += 1
    if a == person3[cnt % 10]:
        scores[2] += 1

    cnt += 1
for i in range(len(scores)):
    if scores[i] == max(scores):
        answer.append(i + 1)
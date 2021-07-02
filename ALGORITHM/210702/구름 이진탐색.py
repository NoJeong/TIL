user_input1 = raw_input()
user_input2 = raw_input()
user_input3 = raw_input()
user_input3 = int(user_input3)
array = list(map(int, user_input2.split()))
answer = -1
left = 0
right = len(array) - 1

while left <= right:
    mid = (left + right) // 2
    if array[mid] == user_input3:
        answer = mid
        break
    elif array[mid] > user_input3:
        right = mid - 1
    elif array[mid] < user_input3:
        left = mid + 1

if answer == -1:
    print('X')
else:
    print(answer + 1)
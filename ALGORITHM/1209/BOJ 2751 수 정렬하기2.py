import sys
sys.stdin = open('BOJ 2751 수 정렬하기2.txt')

def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)


def merge(left, right):
    i = 0
    j = 0
    sorted_list = []
    if left and right:
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
    if left:
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
    if right:
        while j < len(right):
            sorted_list.append(right[j])
            j += 1

    return sorted_list


N = int(input())

base = [int(input()) for _ in range(N)]

a = merge_sort(base)
for j in a:
    print(j)
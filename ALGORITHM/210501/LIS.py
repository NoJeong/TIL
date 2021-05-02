import sys
sys.stdin = open('LIS.txt')


def findLIS(s):
    sequence = [0]
    length = 0

    for i in s:
        if i > sequence[-1]:
            sequence.append(i)
            length += 1
            continue

        start = 0
        end = length
        while start < end:
            mid = (start+end) // 2
            if i < sequence[mid]:
                end = mid
            else:
                start = mid + 1
        sequence[end] = i
    return length


_s_cnt = int(input())
_s_i = 0
_s = []
while _s_i < _s_cnt:
    _s_item = int(input());
    _s.append(_s_item)
    _s_i += 1

res = findLIS(_s);
print(res)


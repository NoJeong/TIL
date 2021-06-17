import bisect

language = ['cpp', 'java', 'python']
part = ['backend', 'frontend']
career = ['junior', 'senior']
food = ['chicken', 'pizza']


def calc(sorted_info, a, b, c, d, e):
    cnt = 0
    if a == '-':
        for item in language:
            cnt += calc(sorted_info, item, b, c, d, e)
    elif b == '-':
        for item in part:
            cnt += calc(sorted_info, a, item, c, d, e)
    elif c == '-':
        for item in career:
            cnt += calc(sorted_info, a, b, item, d, e)
    elif d == '-':
        for item in food:
            cnt += calc(sorted_info, a, b, c, item, e)
    else:
        index = bisect.bisect_left(sorted_info[a][b][c][d], e)
        cnt = len(sorted_info[a][b][c][d]) - index

    return cnt


def solution(info, query):
    answer = []
    sorted_info = {}

    for i in language:
        sorted_info[i] = {}
        for j in part:
            sorted_info[i][j] = {}
            for k in career:
                sorted_info[i][j][k] = {}
                for f in food:
                    sorted_info[i][j][k][f] = []

    for i in info:
        a, b, c, d, e = i.split()
        sorted_info[a][b][c][d].append(int(e))

    for a in language:
        for b in part:
            for c in career:
                for d in food:
                    sorted_info[a][b][c][d].sort()
    for q in query:
        a, aa, b, bb, c, cc, d, e = q.split()
        answer.append(calc(sorted_info, a, b, c, d, int(e)))

    return answer
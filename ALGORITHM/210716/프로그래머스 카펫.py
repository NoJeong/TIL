def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if not total % i:
            a, b = i, total // i
            if (a - 2) * (b - 2) == yellow:
                if a < b:
                    a, b = b, a
                answer.append(a)
                answer.append(b)
                break

    return answer
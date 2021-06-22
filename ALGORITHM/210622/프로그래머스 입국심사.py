def solution(n, times):
    answer = 0
    start = 1
    end = n * max(times)
    while start < end:
        mid = (start+end) // 2
        total = 0
        for time in times:
            total += mid//time
        if n <= total:
            answer = mid
            end = mid
        else:
            start = mid + 1
    return answer
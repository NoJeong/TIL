def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop(-1)

    return len(d)
def solution(s):
    answer = len(s)
    # 압축하려는 길이
    for i in range(1, int(len(s) / 2) + 1):
        position = 0
        length = len(s)

        while position + i <= len(s):
            unit = s[position:position + i]
            position += i

            cnt = 0
            while position + i <= len(s):
                if unit == s[position:position + i]:
                    cnt += 1
                    position += i
                else:
                    break

            if cnt > 0:
                length -= i * cnt
                cnt = str(cnt + 1)
                length += len(cnt)

        answer = min(answer, length)
    return answer
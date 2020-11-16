
#주어진 문자열 안에 특정 패턴이 존재하는지 여부를 출력하는
#프로그램 작성

str = "Hello world! Nice to meet you"
pattern = "mae"
#target 안에서 pattern찾으면 True 아니면 False 반환
# [][][][][][] : 6
# [][][] : 3
# len(target) - len(pattern) + 1
def search(target,pattern):
    for i in range(len(target)-len(pattern)):
        for j in range(len(pattern)):
            #똑같으면 다음것 비교 진행,
            #다르면 즉시 종료
            if pattern[j] != target[i+j]:
                break
            # 위 작은 반복문에서 break가 걸리면,
            # 해당 비교에서 pattern을 못찾음
        else: # for 반복문에서 break가 안걸리면, 패턴 찾은것!
            return True

    return False


result = search(str,pattern)
print(result)
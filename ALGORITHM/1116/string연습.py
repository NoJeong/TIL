#문자열 뒤집기

def str_rev(str):
    #str -> list
    arr = list(str)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    #list -> str
    str = "".join(arr)
    return str

str = "algorithm"
str1 = str_rev(str)

print(str1)

#-----------------------------------------------------
#문자열 뒤집기 2
a = "Reverse this sentence"
reversed_str = list()
#문자열을 뒤에서부터 한 인덱스씩 줄여가면서 조회
for i in range(len(a)-1,-1,-1):
    reversed_str.append(a[i])
print("".join(reversed_str))

b = a[::-1]
print(b)

c = reversed(a)
print(list(c))
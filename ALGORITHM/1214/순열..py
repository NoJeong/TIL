def perm(n,k):
    if k == n:
        print(arr)
    else:
        for i in range(k,n):
            arr[k],arr[i] = arr[i],arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

def powerset(selected,idx,sum):
    if sum > 5:
        return

    if idx == N:
        # print(selected)
        for i in range(N):
            if selected[i] == 1:
                print(arr[i],end=" ")
        print()
        return
    selected[idx] = 1
    powerset(selected,idx + 1,sum + arr[idx])
    selected[idx] = 0
    powerset(selected,idx + 1,sum)



arr = [1,2,3]
N = len(arr)
perm(N,0)
N, A, B = map(int, input().split())
result = 0
for i in range(N+1):
    if i >= 10:
        j = i // 10
        k = i - j * 10
        if A <= j + k <= B:
            result += j + k
    else:
        if A <= i <= B:
            result += i
print(result)

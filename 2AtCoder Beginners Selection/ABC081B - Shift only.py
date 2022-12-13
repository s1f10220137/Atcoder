#n = int(input())
#a = map(int, input().split())
#s = a % 2 
#if s == 0:
#    print(a / 2)

N = int(input())
A = list(map(int, input().split()))
flag = 0
count = 0
while True:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = 1
    if flag == 1:
        break
    for i in range(N):
        A[i] = A[i] // 2
    count += 1
print(count)






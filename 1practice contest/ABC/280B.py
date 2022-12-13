""" N=int(input())
kari=""
for i in range(N):
  a="a"+str(i) #a1
  li=[].append(a) #[a1, a2, a3]
  kari+=a+", " #a1, a2, a3
print(kari)
kari=map(int(), input().split()) #数字 #リストで囲めば良かった
result=""
for j in str(kari):
    result+=j
print(j) """

n=int(input())
s=list(map(int, input().split()))
a=[s[0]]*n
print(a)
for i in range(1,n):
    a[i]=s[i]-s[i-1]
    print(a)
print(*a) #リストに*を付けて関数の引数に指定すると、それぞれの要素が展開され個別の引数として渡される。
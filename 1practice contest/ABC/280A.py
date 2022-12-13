H, w = map(int, input().split())
result=0
for i in range(H):
    gyo=input()
    for k in gyo:
        if k=="#":
            result+=1
print(result)
    
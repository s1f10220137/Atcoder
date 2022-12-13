A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
#X_A = X - A

#while X_A >= 0:
#    X_A = X - A
#X_A_B = X_A - B
#while X_A_B >= 0:
#    X_A_B = X_A - B
#X_A_B_C = X_A_B - C
#while X_A_B_C >= 0:
#    X_A_B_C = X_A_B - C

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X:
                count += 1
print(count)





from decimal import Decimal, ROUND_HALF_UP
de, di=map(int, input().split())
de=de/10
h=""

if 33.75<=de<56.25:
    h="NE"
elif 56.25<=de<78.75:
    h="ENE"
elif 78.75<=de<101.25:
    h="E"
elif 101.25<=de<123.75:
    h="ESE"
elif 123.75<=de<146.25:
    h="SE"
elif 146.25<=de<168.75:
    h="SSE"
elif 168.75<=de<191.25:
    h="S"
elif 191.25<=de<213.75:
    h="SSW"
elif 213.75<=de<236.25:
    h="SW"
elif 236.25<=de<258.75:
    h="WSW"
elif 258.75<=de<281.25:
    h="W"
elif 281.25<=de<303.75:
    h="WNW"
elif 303.75<=de<326.25:
    h="NW"
elif 326.25<=de<348.75:
    h="NNW"
else:
    h="c"

di=str(di/60)
di=Decimal(di).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

p=""
if 0.0<=di<=0.2:
    p=0
elif 0.3<=di<=1.5:
    p=1
elif 1.6<=di<=3.3:
    p=2
elif 3.4<=di<=5.4:
    p=3
elif 5.5<=di<=7.9:
    p=4
elif 8.0<=di<=10.7:
    p=5
elif 10.8<=di<=13.8:
    p=6
elif 13.9<=di<=17.1:
    P=7
elif 17.2<=di<=20.7:
    p=8
elif 20.8<=di<=24.4:
    p=9
elif 24.5<=di<=28.4:
    p=10
elif 28.5<=di<=32.6:
    p=11
else:
    p=12
    
print(di)
print(h, p)
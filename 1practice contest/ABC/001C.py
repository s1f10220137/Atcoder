"""from decimal import Decimal, ROUND_HALF_UP
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
print(h, p)"""

Deg, Dis = map(int, input().split())
 
if 113 <= Deg <= 337:
    Dir = 'NNE'
elif 338 <= Deg <= 562:
    Dir = 'NE'
elif 563 <= Deg <= 787:
    Dir = 'ENE'
elif 788 <= Deg <= 1012:
    Dir = 'E'
elif 1013 <= Deg <= 1237:
    Dir = 'ESE'
elif 1238 <= Deg <= 1462:
    Dir = 'SE'
elif 1463 <= Deg <= 1687:
    Dir = 'SSE'
elif 1688 <= Deg <= 1912:
    Dir = 'S'
elif 1913 <= Deg <= 2137:
    Dir = 'SSW'
elif 2138 <= Deg <= 2362:
    Dir = 'SW'
elif 2363 <= Deg <= 2587:
    Dir = 'WSW'
elif 2588 <= Deg <= 2812:
    Dir = 'W'
elif 2813 <= Deg <= 3037:
    Dir = 'WNW'
elif 3038 <= Deg <= 3262:
    Dir = 'NW'
elif 3263 <= Deg <= 3487:
    Dir = 'NNW'
else:
    Dir = 'N'
 
if Dis <= 14:
    W = 0
elif 15 <= Dis <= 92:
    W = 1
elif 93 <= Dis <= 200:
    W = 2
elif 201 <= Dis <= 326:
    W = 3
elif 327 <= Dis <= 476:
    W = 4
elif 477 <= Dis <= 644:
    W = 5
elif 645 <= Dis <= 830:
    W = 6
elif 831 <= Dis <= 1028:
    W = 7
elif 1029 <= Dis <= 1244:
    W = 8
elif 1245 <= Dis <= 1466:
    W = 9
elif 1467 <= Dis <= 1706:
    W = 10
elif 1707 <= Dis <= 1958:
    W = 11
else:
    W = 12
 
if W == 0:
    Dir = 'C'
 
print(Dir, W)
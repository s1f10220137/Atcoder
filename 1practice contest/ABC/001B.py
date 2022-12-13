m=int(input())
VV=""
if m<100:
    VV="00"
elif 100<=m<1000:
    VV="0"+str(m//100)
elif 1000<=m<=5000:
    VV=str(m//100)
elif 6000<=m<=30000:
    VV=str(m//1000+50)
elif 35000<=m<=70000:
    VV=str((m//1000-30)//5+80)
elif 70000<=m:
    VV="89"
print(VV)

    
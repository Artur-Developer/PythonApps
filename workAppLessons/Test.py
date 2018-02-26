r=0
for i in range (100,999,1):
    if (i**2)%1000==i:
        r+=1
        print(i)

print(r)
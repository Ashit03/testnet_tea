index1 = 0
index2 = 1000
lst=[]
print("Prime numbers between {0} and {1} are :\n".format(index1,index2))
for num in range(index1, index2+1):
    if num > 1:
        isDivisible = False
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True
            if not isDivisible:
                lst.append(num)
print(lst)
f=[]
s=[]
for k in range(len(lst)-1):
    m=[]
    if abs(lst[k]-lst[k+1])==2:
        m.append(lst[k])
        m.append(lst[k+1])
        s.append(m)
for h in s:
    if len(h)==2:
        f.append(h)
print("\nTwim Prime list : \n")
print(f)


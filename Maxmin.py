t1=(1,3,5,7,9,2,4,6,8,10)
ln=len(t1)
print("Given tuple",t1)
print('tuple that represented in 2 lines",end=""')
print(t1[:ln//2])
print(t1[ln//2:])
print("tuple that containing only even numbers",end="")
t3=[]
for x in t1:
    if x%2==0:
        t3.append(x)
t3=tuple(t3)
print("\n",t3)
t2=(11,13,15)
t1=t1+t2
print('tuple after concatenation')
print(t1)
print("Maximum value in the tuple",max(t1))
print("Minimum value in the tuple",min(t1))

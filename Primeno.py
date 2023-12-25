from array import*
a=array('i',[])
n=int(input('Enter how many numbers: '))
print('Enter',n,'Elemets')
for i in range(n):
    a.append(int(input()))
print("Given list")
for i in range(n):
    print(a[i],end="")
print("\nPrime number in the list are")
for i in range(n):
    flag=True
    if a[i]==1:
        flag=False
    else:
        for j in range(2,a[i]//2+1):
            if(a[i]%j==0):
                flag=False
                break
            
    if(flag==True):
        print(a[i],end="")

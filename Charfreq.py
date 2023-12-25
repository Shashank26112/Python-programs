def char_frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
st=input("Enter a string: ")
freq=char_frequency(st)
print("Character Frequency")
for key,value in freq.items():
    if key=="":
        continue
    print(key,'  :  ',value)
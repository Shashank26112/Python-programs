def multi(sample):
return sample*2
img=map(multi,[2,3,4,5])
print("after multilication",list(img))

 def vote(sample):
if sample>18:
return sample
s=filter(vote,[20,21,13,15,18]) print("eligible age is",list(s))

from functools import reduce
def add(x,y):
return x+y
l=reduce(add,[2,3,45,5,6])
print("sum of all elements number is",l)
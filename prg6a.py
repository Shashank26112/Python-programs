from collections import Counter
def mean(sample):
    return sum(sample)/len(sample)
print("Mean is",mean([1,2,3,4,5]))
def median(sample):
    n=len(sample)
    index=n//2
    if n%2==0:
        return sorted(sample)[index]
    else:
        return sum(sorted(sample)[index -1:index +1])/2
print("Median is ",median([1,2,3,4,5]))
def mode(sample):
    c=Counter(sample)
    return[k for k,v in c.items() if v==c.most_common(1)[0][1]]
print("Mode is",mode([1,2,3,4,5]))

from collections import Counter

def find_duplicates(lst):
    counter = Counter(lst)
    duplicates = [item for item, count in counter.items() if count > 1]
    return duplicates

# Example usage
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10]

duplicates = find_duplicates(data)
print("Duplicates:",duplicates)
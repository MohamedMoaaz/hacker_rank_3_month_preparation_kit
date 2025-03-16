# Migratory Birds

from collections import Counter

def most_frequent_smallest_bird(arr):
    #When you call Counter(arr), it returns a dictionary-like object where:
    #Keys are the unique elements from arr.
    #Values are the counts of those elements.
    birds = Counter(arr)  # More efficient for counting
    max_count = max(birds.values())  # Compute max once
    return min(bird for bird, count in birds.items() if count == max_count)

# another solution

def migratoryBirds(arr):
    birds = {bird: arr.count(bird) for bird in set(arr)}
    return min(typ for typ, freq in birds.items() if freq == max(birds.values()))

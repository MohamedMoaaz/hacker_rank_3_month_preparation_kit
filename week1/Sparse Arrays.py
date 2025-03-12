# Sparse Arrays

def matchingStrings(strings, queries):
    string_counts = {}
    for string in strings:
        if string in string_counts:
            string_counts[string] += 1
        else:
            string_counts[string] = 1
    
    result = []
    for query in queries:
        result.append(string_counts.get(query, 0))
    
    return result

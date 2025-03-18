def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)  # Sort in descending order to get the largest perimeter first
    
    # Iterate from the largest values to the smallest
    for i in range(len(sticks) - 2):
        a, b, c = sticks[i], sticks[i+1], sticks[i+2]
        
        if a < b + c:  # Triangle inequality condition
            return [c, b, a]  # Return sorted in ascending order (as required)

    return [-1]  # No valid triangle found

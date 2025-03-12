# Counting Valleys

def countingValleys(steps, path):
    level = 0
    vallies = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                vallies +=1
        elif step == 'D':
            level -= 1
    return vallies

# Mars Exploration

def marsExploration(s):
    c = 0
    for i in range (len(s)):
        if i % 3 == 1:
            if s[i] != 'O':
                c += 1
        else:
            if s[i] != 'S':
                c += 1
    return c

def birthday(s, d, m):
    current_sum = sum(s[:m])
    count = 1 if current_sum == d else 0
    
    for i in range(m, len(s)):
        current_sum += s[i]
        current_sum -= s[i - m]
        if current_sum == d:
            count += 1
    return count

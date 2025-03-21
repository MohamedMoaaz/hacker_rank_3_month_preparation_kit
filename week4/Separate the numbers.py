def separateNumbers(s):
    length = len(s) // 2 + 1
    for i in range(1, length):
        f = int(s[:i])
        pattern = str(f)
        next = f
        while len(pattern) < len(s):
            next += 1
            pattern += str(next)
        
        if pattern == s:
            print(f"YES {f}")
            return
    print("NO")

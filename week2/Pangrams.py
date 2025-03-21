def pangrams(s):
    return "pangram" if len({c.lower() for c in s if c != ' '}) == 26 else "not pangram"

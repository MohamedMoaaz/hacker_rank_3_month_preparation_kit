def lonelyinteger(a):
    for i in a:
        count = a.count(i)
        if count == 1:
            return i  

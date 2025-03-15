# Sock Merchant

def sockMerchant(n, ar):
    pairs = 0
    socks_dict = {}
    for sock in ar:
        if sock in socks_dict:
            socks_dict[sock] +=1
        else :
            socks_dict[sock] =1
             
    for value in socks_dict.values():
        pairs += value // 2
    return pairs

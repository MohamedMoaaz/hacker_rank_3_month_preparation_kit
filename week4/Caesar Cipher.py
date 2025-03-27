def caesarCipher(s, k):
    result = ""
    for string in s:
        if string.isalpha():
            ascii = ord(string)
            if string.isupper():
                result += chr(65 + ((ascii + k - 65) % 26))
            else:
                result += chr(97 + ((ascii + k - 97) % 26))
        else:
            result += string
    return result

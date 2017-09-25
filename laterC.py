#Keyword Key Cipher
def keywordKeyCipher(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyString = ""
    end = ""
    l = len(text)
    p = 0

    for x in range (0, len(key)):
        if key[x:x+1] == " ":
            key = key[:x] + key[x+1:]

    lk = len(key)
    a = l/lk
    for y in range (0, a+1):
        keyString = keyString + key

    for z in range (0, l):
        b = text[z:z+1]
        if b == " ":
            end = end + " "
        else:
            c = alphabet.index(b)
            k = alphabet.index(keyString[p])
            d = c + k
            if d > 25:
                d = d - 26
            e = alphabet[d]
            end = end + e
            p = p + 1

    return end

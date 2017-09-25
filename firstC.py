#Reverse Cipher function
def reverseCipher(text):
    end = ""
    l = len(text)

    for x in range (0, l):
        end = end + text[l-(x+1):l-x]
        x = x + 1

    return end

#Cesar Cipher function
def cesarCipher(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    end = ""
    l = len(text)
    keyn = alphabet.index(key) + 1

    for x in range (0, l):
        a = text[x]
        if a == " ":
            end = end + " "
        else:
            b = alphabet.index(a)
            c = b + keyn
            if c > 25:
                c = c - 26
            d = alphabet[c]
            end = end + d

    return end

#Reverse-Self Cipher function (reverse text, use as key)
def reverseSelfCipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    end = ""
    key = ""
    l = len(text)
    z = 0

    for x in range (0, l):
        if text[x:x+1] == " ":
            key = text[:x] + text[x+1:]
        x = x + 1

    nkey = reverseCipher(key)
    nkey = nkey + "ABC"

    for y in range (0, l):
        a = text[y]
        if a == " ":
            end = end + " "
        else:
            b = alphabet.index(a)
            k = nkey[z]
            n = alphabet.index(k) + 1
            c = b + n
            if c > 25:
                c = c - 26
            d = alphabet[c]
            end = end + d
            z = z + 1

    return end

#Keyword Cipher (use keyword to create new order of alphabet, use as key)
def keywordCipher(text, key):
    end = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyAlphabet = ""
    key = key + alphabet
    l = len(text)
    lk = len(key)

    for x in range (0, lk):
        if key[x] not in keyAlphabet:
            if key[x] == " ":
                keyAlphabet = keyAlphabet
            else:
                keyAlphabet = keyAlphabet + key[x]
        else:
            pass

    for y in range (0, l):
        a = text[y]
        if a == " ":
            end = end + " "
        else:
            b = alphabet.index(a)
            c = keyAlphabet[b]
            end = end + c

    return end

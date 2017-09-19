#Just a little project to encrypt messages with simple ciphers

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

#Start of the interactive part of the program
first_name = raw_input("What's your name? ")
print "Hello %s" % first_name
playing = True

while playing == True:

    print "Here are the ciphers: \n 1 = Reverse cipher \n 2 = Cesar Cipher \n 3 = Reverse Self Cipher \n 4 = Keyword Cipher"
    choice = raw_input("What do you choose? ")

    if choice == "1":
        print "You have chosen the Reverse Cipher"
        text = raw_input("What would you like your mesage to say?\n")
        print reverseCipher(text.upper())
        playing = False

    elif choice == "2":
        print "You have chosen the Cesar Cipher"
        text = raw_input("What would you like your mesage to say?\n")
        key = raw_input("What would you like your one letter key to be? ")
        print cesarCipher(text.upper(), key.upper())
        playing = False

    elif choice == "3":
        print "You have chosen the Reverse-Self Cipher"
        text = raw_input("What would you like your message to say?\n")
        print reverseSelfCipher(text.upper())
        playing = False

    elif choice == "4":
        print "You have chosen the Keywork Cipher"
        text = raw_input("What would you like your message to say?\n")
        key = raw_input("What would you like your word/phrase key to be? ")
        print keywordCipher(text.upper(), key.upper())
        playing = False

    else:
        print "I'm afraid I don't understand what you're saying"

    wannaPlay = raw_input("Would you like to encrypt something else? (Y/N): ")

    if wannaPlay.upper() == "Y":
        playing = True
    else:
        playing = False
        break

print "Bye bye!"

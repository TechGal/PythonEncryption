#Just a little project to encrypt messages with simple ciphers

import firstC
import laterC

first_name = raw_input("What's your name? ")
print "Hello %s" % first_name
playing = True

while playing == True:

    print "Here are the ciphers: \n 1 = Reverse cipher \n 2 = Cesar Cipher \n 3 = Reverse Self Cipher \n 4 = Keyword Cipher \n 5 = Keyword Key Cipher"
    choice = raw_input("What do you choose? ")

    if choice == "1":
        print "You have chosen the Reverse Cipher"
        text = raw_input("What would you like your mesage to say?\n")
        print firstC.reverseCipher(text.upper())
        playing = False

    elif choice == "2":
        print "You have chosen the Cesar Cipher"
        text = raw_input("What would you like your mesage to say?\n")
        key = raw_input("What would you like your one letter key to be? ")
        print firstC.cesarCipher(text.upper(), key.upper())
        playing = False

    elif choice == "3":
        print "You have chosen the Reverse-Self Cipher"
        text = raw_input("What would you like your message to say?\n")
        print firstC.reverseSelfCipher(text.upper())
        playing = False

    elif choice == "4":
        print "You have chosen the Keywork Cipher"
        text = raw_input("What would you like your message to say?\n")
        key = raw_input("What would you like your word/phrase key to be? ")
        print firstC.keywordCipher(text.upper(), key.upper())
        playing = False

    elif choice == "5":
        print "You have chosen the Keyword Key Cipher"
        text = raw_input("What would you like your message to say?\n")
        key = raw_input("What would you like your word/phrase key to be? ")
        print laterC.keywordKeyCipher(text.upper(), key.upper())
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

#Decryptinator
def welcome():
    print ("\nWelcome to the Decryptinator!\n")
    print (" ***The Fallout Computer Password Decryptor by Jon Collins***")
    print ("\n"*4)


def enterWords():
    #input
    char = float (input ("Enter number of characters for word sets: "))
    print ("\nType all words shown on screen. When done, type the letter 'd', then Enter.\n")

    tryList = []
    inpt = 0

    while inpt != "d":

        inpt = input ("Enter word: ")
        tryList.append (inpt)
        if (len(inpt) != char and inpt != "d"):
            print ("Error: Word does not have correct number of characters. Please check your spelling and try again.")
            tryList.pop ()
        if (inpt == "d"):
            tryList.remove("d")
            break

    return tryList



def tryUnlock(workSet):

    trywrd = input ("Enter try word: ")
    trynum = float (input ("Enter number correct: "))
    workSet.remove (trywrd)

    count = 0

    for word in workSet:

        for letter in word:
            if word[let] == trywrd[let]:
                count += 1

                # exit loop if has more letters than trynum
                if count > trynum:
                    workSet.remove(word)
                    break
        """
        if (trynum == 0 and count == 0):
            b.append (a[tag])
        el
        """
        if count < trynum:
            workSet.remove(word)


    return workSet




def main():

    welcome()

    workSet = enterWords()

    for i in range(0,2):
        workSet = tryUnlock(workSet)

    print ('Good Luck!!!')

main()

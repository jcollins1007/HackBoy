#Decryptinator
def welcome():
    print ("\nWelcome to the Decryptinator!\n")
    print (" ***The Fallout Computer Password Decryptor by Jon Collins***")
    print ("\n"*4)


def enterWords():
    #input
    char = int (input ("Enter number of characters for word sets: "))
    print ("\nType all words shown on screen. When done, type the letter 'd', then Enter.\n")

    tryList = {}
    inpt = 0

    while inpt != "d":

        inpt = input ("Enter word: ")
        if (inpt == "d"):
            break
        tryList[inpt] = 0
        if (len(inpt) != char and inpt != "d"):
            print ("Error: Word does not have correct number of characters. Please check your spelling and try again.")
            tryList.remove(inpt)


    return tryList



def tryUnlock(workSet):

    trywrd = input ("Enter try word: ")
    strTryNum = input ("Enter number correct: ")
    trynum = int(strTryNum)
    workSet[trywrd] = 1

    for word in workSet:
        print (workSet)
        count = 0
        for i in range(0,len(trywrd)):
            print (word[i], trywrd[i])
            if word[i] == trywrd[i]:
                count += 1

        print (trywrd, word, count)

        # exit loop if has more letters than trynum
        if count != trynum:
            workSet[word] = 1
            #break
    print (workSet)


    dictOutList = {}
    for word in workSet:

        if workSet[word] == 0:
            dictOutList[word] = 0


    return dictOutList




def main():

    welcome()

    workSet = enterWords()

    for i in range(0,3):
        workSet = tryUnlock(workSet)
        print (workSet)

    print ("\nGood Luck!!!\n")

main()

#Decryptinator

print ()
print ("Welcome to the Decryptinator!")
print ()
print (" ***The Fallout Computer Password Decryptor by Jon Collins***")

#input

print ()
char = float (input ("Enter number of characters for word sets: "))
print ()
print ("Type all words shown on screen. When done, type the letter 'd', then Enter.")
print ()

a = []
inpt = 0

while inpt != "d":

    inpt = input ("Enter word: ")
    a.append (inpt)
    if (len(inpt) != char and inpt != "d"):
        print ("Error: Word does not have correct number of characters. Please check your spelling and try again.")
        a.pop ()
    if (inpt == "d"):
        a.remove("d")
        break


#Try 1

trywrd = input ("Enter try word: ")
trynum = float (input ("Enter number correct: "))
a.remove (trywrd)


tag = -1
b = []    
    
while tag < len(a)-1:

    tag += 1
    count = 0
    let = -1
    while let < len(a[tag])-1:
        let += 1
           
        if a[tag][let] == trywrd[let]:
            count += 1

    if (trynum == 0 and count == 0):
        b.append (a[tag])
    elif count == trynum:
        b.append (a[tag])


print ('Possibles are: ', b)

#Try 2

trywrd = input ("Enter try word: ")
trynum = float (input ("Enter number correct: "))
b.remove (trywrd)


tag = -1
c = []    
    
while tag < len(b)-1:

    tag += 1
    count = 0
    let = -1
    while let < len(b[tag])-1:
        let += 1
           
        if b[tag][let] == trywrd[let]:
            count += 1

    if (trynum == 0 and count == 0):
        c.append (b[tag])
    elif count == trynum:
        c.append (b[tag])


print ('Possibles are: ', c)

#Try 3

trywrd = input ("Enter try word: ")
trynum = float (input ("Enter number correct: "))
c.remove (trywrd)


tag = -1
d = []    
    
while tag < len(c)-1:

    tag += 1
    count = 0
    let = -1
    while let < len(c[tag])-1:
        let = let + 1
           
        if c[tag][let] == trywrd[let]:
            count += 1

    if (trynum == 0 and count == 0):
        d.append (c[tag])
    elif count == trynum:
        d.append (c[tag])


print ('Possibles are: ', d)
print ()
print ('Good Luck!!!')



#Create a Polybius Square using the key!
def polybiusSquare(key):
    square = list()
    for row in range(5):
        rows = list()
        for column in range(5):
            rows.append(None)
        square.append(rows)

    alphabets = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    row = 0
    column = 0

    #Populate the Polybius square with the key from the user
    for alpha in key:
        if any(alpha in sublist for sublist in square) == False:
            square[row][column] = alpha
            if column >= 4:
                row += 1
                column = 0
            else:
                column += 1

    #Populate the remaining spots with unique characters from the alphabets
    for alpha in alphabets:
        if any(alpha in sublist for sublist in square) == False:
            square[row][column] = alpha
            if column >= 4:
                row += 1
                column = 0
            else:
                column += 1

#    printPolybius(square)

    return square

def printPolybius(square):
    print ("--------------------")
    for i in range(5):
        print("|",end='')
        for j in range(5):
            print (square[i][j],"|",end=' ')
        print ("\n--------------------")

def encryption(encryptString, polybius):
    #if length of the message is not even, then add a least used character to the string to make it even
    if len(encryptString)%2 != 0:
        encryptString = encryptString + "q"

    if len(encryptString)%2 == 0:
        #Since the polybius square can accommodate only 25 characters, j is excluded. All j's are replaced with i's.
        encryptString = encryptString.replace('j','i')

        #Initialize new lists for rows and columns
        rows = list()
        columns = list()
        for char in encryptString:
            #For all characters in encryptString, populate the row and column indices
            for row,listIndices in enumerate(polybius):
                if char in listIndices:
                    rows.append(row)
                    columns.append(listIndices.index(char))

        wholeList = rows + columns
        joinedList = "".join(str(item) for item in wholeList)

        encryptedString = ""
        #Group indices according to Bifid cipher and find the corresponding character to create an encryptedString
        for item in range(0,len(joinedList),2): 
            row = int(joinedList[item])
            column = int(joinedList[item+1])
            encryptedString = encryptedString + polybius[row][column]

    return encryptedString


def decryption(decryptString, polybius):
    #Ensure the length of string is even
    if len(decryptString)%2 == 0:
        wholeList = list()
        for char in decryptString:
            for row,listIndices in enumerate(polybius):
                if char in listIndices:
                    wholeList.append(row)
                    wholeList.append(listIndices.index(char))

        rows = list()
        columns = list()

        splitLen = int(len(wholeList)/2)
        #Split the list into rows and columns
        rows = wholeList[0:splitLen]
        columns = wholeList[splitLen:]

        decryptedString = ""
        #Retrieve the appropriate character from the polybius square
        for item in range(0,len(rows)): 
            decryptedString = decryptedString + polybius[rows[item]][columns[item]]

        #If additional 'q' was added to the string, remove the addition to get the original string
        if decryptedString[-1] == "q":
            decryptedString = decryptedString[:-1]

        return decryptedString


if __name__ == "__main__":

    choice = 1
    while(choice == 1 or choice == 2):
        print("")
        print("=====================================")
        print("|         BIFID CIPHER MENU         |")
        print("|           1. Encryption           |")
        print("|           2. Decryption           |")
        print("|           3. Exit                 |")
        print("=====================================")
        print("")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                encryptString = input("Enter secret string to encrypt: ")
                keyphrase = input("Enter keyphrase to use for encryption: ")
                polybius = polybiusSquare(keyphrase)
                #Convert all characters to lowercase
                encryptString = encryptString.lower()
                #Remove all special characters present in the input string
                encryptString = ''.join(e for e in encryptString if e.isalnum())
                encryptedString = encryption(encryptString, polybius)
                print("\nYour encrypted string for the secret message: ",encryptedString,"\n")

            case 2:
                decryptString = input("Enter encrypted string to decrypt: ")
                keyphrase = input("Enter keyphrase to use for decryption: ")
                polybius = polybiusSquare(keyphrase)
                decryptedString = decryption(decryptString, polybius)
                print("\nYour secret message: ",decryptedString,"\n")

            case default:
                print("\nThank you for using Bifid Cipher!\n")
                break


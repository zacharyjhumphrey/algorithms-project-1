import numpy

print('hello world')

print ('All we have to decide is what to do with the time that is given us.')

print('please tell me you see this')

#stores messages before encryption and after decryption
decryptedMsgs = []
#stores messages after they are encrypted
encryptedMsgs = []
#stores signatures to be verified
signatures = []

def mainMenu():
    
    #print menu
    print("\nPlease select your user type:\
    \n\t1. A public user\
    \n\t2. The owner of the keys\
    \n\t3. Exit program")
   
    #get user input
    option = input("\nEnter your choice: ")
    
    #enter public user menu
    if option == "1":
        publicUserMenu()
    #enter owner of keys menu
    elif option == "2":
        keyOwnerMenu()
    #exit program
    elif option == "3":
        return
    #catch case
    else:
        print("please enter '1', '2', or '3'")
        mainMenu()
    
    
    
def publicUserMenu():
    #print menu
    print("\nAs a public user, what would you like to do?\
    \n\t1. Send an encrypted message\
    \n\t2. Authenticate a digital signature\
    \n\t3. Exit")
    
    #get user input
    option = input("\nEnter your choice: ")
    
    #accepts message and stores in decryptedMsgs
    if option == "1":
        decryptedMsgs.append(input("\nEnter a message: "))
        #moves from decrypted to encrypted with basic encryption tester
        encryptedMsgs.append(decryptedMsgs.pop(decryptedMsgs.count(str) - 1))
        #
        #add call to run encryption on last decrypted message added
        #
        print("message encrypted and sent.")
        publicUserMenu()
    #checks for signatures
    elif option == "2":
        if signatures == []:
            print("There are no signatures to authenticate")
        #show signature options
        else:
            print("The following messages are available:")
            for s in signatures:
              print("\t"+str(signatures.index(s)+1)+". "+s) 
            selectedSig = signatures[int(input("Enter your choice: "))-1]
            print(selectedSig)
        #
        #add call to verify signature
        #
        publicUserMenu()
    #exit to main menu
    elif option == "3":
        mainMenu()
    #catch case
    else:
        print("please enter '1', '2', or '3'")
        publicUserMenu()
    
def keyOwnerMenu():
    #print menu
    print("\nAs the owner of the keys, what would you like to do?\
    \n\t1. decrypt a received message\
    \n\t2. digitally sign a message\
    \n\t3. Exit")
    
    #get user input
    option = input("\nEnter your choice: ")
    
    #checks for enctyped messages
    if option == "1":
        if encryptedMsgs == []:
            print("There are no messages available.")
        else:
            print("The following messages are available:")
            #display encrypted Messages by length
            for s in encryptedMsgs:
              print("\t"+str(encryptedMsgs.index(s)+1)+". (length = "+str(len(s))+")") 
            selectedMsg = encryptedMsgs[int(input("Enter your choice: "))-1]
            #show selected msg
            #
            #insert call to decryption method
            #
            print(selectedMsg)
        keyOwnerMenu()
    #add signature to signatures list
    elif option == "2":
        signatures.append(input("Enter a message:"))
        print("Message signed and sent.")
        keyOwnerMenu()
    #exit to mainmenu
    elif option == "3":
        mainMenu()
    #catch case
    else:
        print("please enter '1', '2', or '3'")
        keyOwnerMenu()
        

    

#once mainMenu is ran stuck in recursive loop between menus
#functions unless option 3 is selected while in the main menu
mainMenu()

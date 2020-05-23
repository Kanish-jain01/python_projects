def addNew():
    print("How many new contacts do you like to add?\n")
    numberOfContacts=int(input())
    while(numberOfContacts>0):
        fp=open("contact.txt","w")
        print("Name of the new contact:\n")
        newContact=input()
        newContact=newContact.lower()
        print("Contact Number:\n")
        contact=int(input())
        if(len(str(contact))!=10):
            print("There must be 10 digits in the contact number\n")
            print("Please insert again\n")
            contact=int(input())
        fp.write("Name:")
        fp.write(str(newContact))
        fp.write("\n")
        fp.write("Contact:")
        fp.write(str(contact))
        fp.write("\n")
        print("Would you like to add to group?\n")
        print("Please type 1 for yes and 2 for no\n")
        addGroup=int(input())
        if(addGroup==1):
            fp.close()
            addToGroup(newContact,contact)
        print("Would you like to add to favourites?\n")
        print("Please type 1 for yes and 2 for no\n")
        addFav=int(input())
        if(addFav==1):
            fp.close()
            addToFav(newContact,contact)
        numberOfContacts=numberOfContacts-1
    fp.close()

def addToGroup(newContact,contact):
    print("There are 4 groups available\n")
    print("\n1.Friends\n2.Family \n3.Emergency \n4.Others\n")
    print("Which Group would you like to add?\n")
    print("Please insert the number against your desired group\n")
    group=int(input())
    if(group==1):
        friends.append([newContact,contact])
        print("Added to friends\n")
    elif(group==2):
        family.append([newContact,contact])
        print("Added to family\n")
    elif(group==3):
        emergency.append([newContact,contact])
        print("Added to emergency \n")
    else:
        other.append([newContact,contact])
        print("Added to other \n")
    return 0

def displayGroup():
    for i in friends:
        print(i)
    for j in family:
        print(j)
    for k in emergency:
        print(k)
    for l in other:
        print(l)

def addToFav(newContact,contact):
    fav.append([newContact,contact])
    print("Added to Favourites\n")
    return 0

def displayFavourites():
    for k in fav:
        print(k)

def displayAll():
    fp=open("contact.txt","r")
    for i in fp:
        print(i)
    fp.close()

#main code
print("Welcome\n")
print("\nThis is a contact book\n")
print("\nInstructions\n")
print("\n1. In this contact book you can save upto 200 contacts \n")
print("\n2. Operations available in the contact book are \na.Add new contact \nb.Update existing contact \nc.Delete contact \nd.Add to favorites \ne.Add to a group \nf.List all the saved contacts\n")
print("\nNow create your contact book\n")
print("\n***************************\n")
print("\nYour name: \n")
name=input()
friends=[]
family=[]
emergency=[]
other=[]
fav=[]
print("\nYour Phone Number: \n")
yournumber=input()
print("\nHow many operations would you like to do?\n")
numberOfOperations=int(input())
while(numberOfOperations>0):
    print("\nWhat would you like to do?\n")
    print("\n1.Add new contact \n2.Display all the contacts \n3.Display contacts of particular group \n4.Display all favourites contact\n")
    print("\nPlease input the number against your desired operation\n")
    operation=int(input())
    if(operation==1):
        numberOfOperations=numberOfOperations-1
        addNew()
    elif(operation==2):
        numberOfOperations=numberOfOperations-1
        displayAll()
    elif(operation==3):
        numberOfOperations=numberOfOperations-1
        displayGroup()
    elif(operation==4):
        numberOfOperations=numberOfOperations-1
        displayFavourites()



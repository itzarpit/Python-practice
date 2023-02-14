import pymongo
import addContact
import phonebook
import delete_all
from flask import Flask


client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]

app=Flask(__name__)


@app.route('/',methods=['GET','POST','PUT','DELETE'])
def menu():
        print("\tYou can now perform the following operations on this phonebook\n")
        print("1. Add multiple contacts")
        print("2. Add a new contact")
        print("3. Remove an existing contact")
        print("4. Delete all contacts")
        print("5. Search for a contact")
        print("6. Update a contact present in directory")
        print("7. Display all contacts")
        print("8. Exit phonebook")
        choice=int(input("Please Enter Your Choice : "))
        return (choice)
ch = 1
while ch in (1, 2, 3, 4, 5, 6, 7):
    ch = menu()
    if ch==1:
        x=phonebook.phonebook()
    elif ch == 2:
        x = addContact.add_contact(self)
    elif ch == 3:
        x = delete_contact()
    elif ch == 4:
        x = delete_all.delete()
    elif ch == 5:
        x = search_contact()
        if x == -1:
            print("The contact does not exist. Please try again")
    elif ch==6:
        x = update_contact()
    elif ch == 7:
        display_all()
    else:
        thanks()
import sys
import Server
import pymongo


client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]


def phonebook():
    rows=int(input("Please enter the number of contacts to be inserted : "))
    col=5
    phone_book=[]
    for i in range(rows):
        mydoc={}
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
    # Input field's which are predefined and shown to user when asked to save the number
        category0="_id"
        id=input("Enter the id : ")
        mydoc[category0]=id


        category1="Name"
        name=input("Enter the name : ")
        mydoc[category1]=name
        if mydoc[category1]=='' or mydoc[category1]==' ':
            sys.exit("Mandatory Field")


        category2="Number"
        num=int(input("Enter the number : "))
        mydoc[category2]=num


        category3="Email"
        mail=input("Enter the mail id : ")
        mydoc[category3]=mail


        category4="DOB"
        print("Enter details of dob")
        date=input("Enter date : ")
        month=input("Enter month : ")
        year=input("Enter Year : ")
        dob=date+"/"+month+"/"+year


        mydoc[category4]=dob
        category5="Category"
        category=input("Enter category(Family/Friends/Work/Others): ")
        mydoc[category5]=category 
        
          
        phone_book.append(mydoc)
    x=Server.insert_many(phone_book)
    return x  



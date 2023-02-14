import Server
from flask import Flask,request
import sys
import menu

app=Flask(__name__)



@app.route('/addContact',methods=['GET','POST'])
def add_contact(self):




    #category0="_id"
    #id=input("Enter ID : ")
    #myContact[category0]=id

    try:
        myContact={}

        category1="Name"
        self.name=input("Enter the name : ")
        request_data=request.get_json()
        self.new={"Name":request_data["Name"]}
        myContact.append(self.new)
        #myContact[category1]=name
        if myContact[category1]=='' or myContact[category1]==' ':
            sys.exit("Mandatory Field")


        category2="Number"
        num=int(input("Enter the number : "))
        myContact[category2]=num


        category3="Email"
        mail=input("Enter the mail id : ")
        myContact[category3]=mail


        category4="DOB"
        print("Enter details for your dob")
        date=input("Enter date : ")
        month=input("Enter month : ")
        year=input("Enter Year : ")
        dob=date+"/"+month+"/"+year
        myContact[category4]=dob


        category5="Category"
        category=input("Enter category(Family/Friends/Work/Others): ")
        myContact[category5]=category 
        x=Server.insert_one(myContact) 

        return x
    
    except:
        print("Enter the valid Input")

if __name__=='__main__':
    app.run(debug=True,port=8002)
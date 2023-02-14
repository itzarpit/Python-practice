import Contact_book 
from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route('/addMultipleContact',methods='POST')
def addMultiple():
    object1=Contact_book.phonebook()
    request_data=request.get_json()
    new=[{"_id":request_data["_id"]},{"name":request_data["name"]
    },{"number":request_data["number"]},{"Email":request_data["Email"]},{"DOB":request_data["DOB"]},{"Category":request_data["Category"]}]
    object1.append(new)
    return object1

object2=Contact_book.menu()

object3=Contact_book.add_contact()

object4=Contact_book.delete_contact()

object5=Contact_book.delete_all()

object6=Contact_book.search_contact()

object7=Contact_book.update_contact()

object8=Contact_book.display_all()


if __name__=='__main__':
    app.run(debug=True,port=8001)
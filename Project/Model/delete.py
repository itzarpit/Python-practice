from flask import Flask,jsonify
import pymongo


client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]

app=Flask(__name__)


@app.route('/deleteExisting',methods=['DELETE'])
def delete_contact():
    try:
        name=input("Enter name to delete : ")
        myquery={"Name":name}
        mycol.delete_one(myquery)
        return mycol
    except:
        return jsonify({"Status":"Enter a valid name"}),422


if __name__=='__main__':
    app.run(debug=True,port=8002)
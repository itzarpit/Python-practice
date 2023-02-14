from flask import Flask,request
from bson import json_util
import json
import pymongo

client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]

app=Flask(__name__)

@app.route('/',methods=['GET'])
def searchContact():
    @app.route('/search/<string:name>',methods=['GET'])
    def search(name):
        query={"name":name}
        data=request.get_json()
        documents=mycol.find()
        arr=[]
        for document in documents:
            document['name']=str(document['name'])
            arr.append(document)

        return json.dump(arr, indent=4, default=json_util.default)
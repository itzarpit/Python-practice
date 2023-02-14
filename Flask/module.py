from flask import *
import pymongo
import json
from bson import json_util


app=Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://arpit:12345@cluster0.de4wpvp.mongodb.net/?retryWrites=true&w=majority")
db = client['School']
coll = db['Teacher']

        

@app.route('/dataSend',methods=['POST'])
def insert():
    data=request.get_json()
    coll.insert_many(data)

    return jsonify({"status": "Connection Successful"})

@app.route('/',methods=['GET'])
def fetch(name):
    query={"name":name}
    data=request.get_json()
    documents=coll.find()
    arr=[]
    for document in documents:
        document['name']=str(document['name'])
        arr.append(document)

    return json.dumps(arr, indent=4, default=json_util.default)

@app.route('/update/<string:name>',methods=['PUT'])
def update(self):
    query={"name":self.name["name"]}
    data=request.get_json()
    newvalue={"$set":{"Deadline in days":data[["deadline in days"]]}}
    coll.update_one(query,newvalue)

    return jsonify({"status":"Connection Successful"})

@app.route('/delete',methods=['DELETE'])
def delete(name):
    query={"name":name}
    coll.delete_many(query)

    return jsonify({"Status":"Deletion Successful"})

if __name__=="__main__":
    app.run(debug=True,port=9001)  
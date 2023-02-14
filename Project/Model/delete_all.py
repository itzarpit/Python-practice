from flask import Flask
import Server

object=Server.server()


app=Flask(__name__)

@app.route('/delete',methods=['DELETE'])
def delete():
    mycol.delete_many({})
    return mycol
from flask import Flask , request  
from flask_marshmallow import Marshmallow
from marshmallo import Schema, fields



app=Flask(__name__)
ma=Marshmallow(app)

class AddProjectRequestSchema(Schema):
    Name=fields.Str(required=True)

@app.route('/project',methods=['GET','POST'])
def project():
    if request.method=='POST':
        errors=AddProjectRequestSchema().validate(request.json)

        if errors:
            return errors,422
        
        project_request_dict=AddProjectRequestSchema().load(request.json)
        
        return project_request_dict
    
if __name__=='__main__':
    app.run(debug=True,port=8001)
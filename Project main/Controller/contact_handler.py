from flask import *
from app import app
from Model.model import Functions


@app.route('/api', methods=['POST'])
def create_data():
    data = request.get_json()
    print(data)
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                            status=400)
    create_obj = Functions(data)
    response = create_obj.create_contact(data)
    return Response(response=json.dumps(response), status=200,
                        mimetype='application/json')

@app.route('/api', methods=['GET'])
def read_data():
    data = request.get_json()
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),status=400, mimetype='application/json')
    read_obj = Functions(data)
    response = read_obj.Search_Contact(data)
    return Response(response=json.dumps(response), status=200)

@app.route('/api', methods=['PUT'])
def update():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                            status=400)
    update_obj = Functions(data)
    response = update_obj.Update_Contact()
    return Response(response=json.dumps(response), status=200)

@app.route('/api', methods=['DELETE'])
def delete():
    data = request.form["Name"]
    if data is None or data == {} or 'Delete' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                            status=400)
    delete_obj = Functions(data)
    response = delete_obj.Delete_Contact(data)
    return Response(response=json.dumps(response), status=200)

@app.route('/sort', methods=['GET'])
def sorted():
    data = request.json
    if data is None or data == {} or 'sot' not in data:
        return Response(response=json.dumps({"Please provide Sort parameter"}), status=400)

    sorted_obj = Functions(data)
    respon = sorted_obj.Sort_Contact(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/limit', methods=['GET'])
def limited():
    data = request.json
    if data is None or data == {} or 'limit' not in data:
        return Response(response=json.dumps({"Please provide Sort parameter"}), status=400)
    limited_obj = Functions(data)
    respon = limited_obj.Limit_show(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/OnDate', methods=['GET'])
def date():
    data = request.json
    OnDate_obj = Functions(data)
    respon = OnDate_obj.OnDate(data)
    return Response(response=json.dumps(respon), status=200)
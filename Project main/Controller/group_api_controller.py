from flask import *
from app import app
from Model.model import Functions


@app.route('/cgrp', methods=['POST'])
def C_Group():
    data = request.json
    Cgrp_obj = Functions(data)
    respon = Cgrp_obj.Create_Group(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/sgrp', methods=['GET'])
def S_Group():
    data = request.json
    Sgrp_obj = Functions(data)
    respon = Sgrp_obj.Search_Group(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/dgrp', methods=['DELETE'])
def D_Group():
    data = request.json
    Dgrp_obj = Functions(data)
    respon = Dgrp_obj.Delete_Group(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/ugrp', methods=['PUT'])
def U_Group():
    data = request.json
    Ugrp_obj = Functions(data)
    respon = Ugrp_obj.Update_Group(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/dpagrp', methods=['PUT'])
def D_Pati_Group():
    data = request.json
    DPagrp_obj = Functions(data)
    respon = DPagrp_obj.Delete_From_Particular_Grp(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/dmnygrp', methods=['PUT'])
def D_Mny_Group():
    data = request.json
    Dmnygrp_obj = Functions(data)
    respon = Dmnygrp_obj.Delete_From_Many_Grp(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/dallgrp', methods=['PUT'])
def D_all():
    data = request.json
    Dallgrp_obj = Functions(data)
    respon = Dallgrp_obj.Delete_From_all(data)
    return Response(response=json.dumps(respon), status=200)

@app.route('/slike', methods=['GET'])
def S_Likewise_Group():
    data = request.json
    Slike_obj = Functions(data)
    respon = Slike_obj.Search_Contact(data)
    return Response(response=json.dumps(respon), status=200)

from pymongo import*
from bson.objectid import ObjectId
from bson import json_util
from bson.json_util import dumps
from flask import Flask
from datetime import datetime


app=Flask(__name__)

@app.route('/')
def MainPage():
    return ("Satus : Main Page is Working")

class Functions:
    def __init__(self,data):
        self.client = MongoClient(host="localhost",port=27017)
        self.database = data['database']
        self.collection = data['collection']
        self.cursor = self.client[self.database]
        self.collection = self.cursor[self.collection]
        self.data=data

    def TimeStp(self):
        now = datetime.now()
        dt_string =now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string


    def create_contact(self,data):
        new_document = data['Document']
        res = str(new_document)[1:-1]
        r=eval(res)
        r['CreateAt']=self.TimeStp()
        r['UpdateAt']=self.TimeStp()
        l=[r]
        response = self.collection.insert_many(l)
        output = {'Status': 'Successfully Inserted'}
        return output

    def Search_Contact(self,data):                 
        search = self.data['To_Search']
        for key,val in search.items():
            search=key
            searchName=val

        r={f'{search}':{'$regex':f'{searchName}'}}
        documents = self.collection.find(r)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
       

    def Update_Contact(self):                  
        filter = self.data['Filter']
        doc = self.collection.find(filter)
        li=(list(doc))
        res = str(li)[1:-1]
        r=eval(res)
        r['UpdateAt']=self.TimeStp()
        y=r.get('UpdateAt')
        p={'UpdateAt':y}
        updated_data = {"$set":self.data['DataToBeUpdated']}
        updated_time = {"$set":p}
        response = self.collection.update_many(filter, updated_time)
        response = self.collection.update_many(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    
    def Delete_Contact(self, data):   
        Dele_Nm_No = data['ToBeDelete']
        response = self.collection.delete_one(Dele_Nm_No)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

    def Sort_Contact(self,data):
        By_which_data_sort=data['sot']
        documents = self.collection.find().sort(By_which_data_sort["vale"],By_which_data_sort["sort"])
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    
    def Limit_show(self,data):
        li=data['limit']
        documents = self.collection.find().limit(li)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output


##############GROUPS OPERATIONS#################################

    def Create_Group(self,data):
        new_document = data['GrpDocument']
        p=[]
        for i in new_document:
            gpr=i['GroupName']
            for j in i['Value']:
                documents = self.collection.find(j)
                user = json.loads(dumps(documents))
                id_list=[(i['_id']['$oid']) for i in user]
                for i in id_list:
                    p.append(i)
        gp=f'"{gpr}"'
        l="{"+gp+':'f'{p}'+"}"
        n=eval(l)
        n['CreateAt']=self.TimeStp()
        n['UpdateAt']=self.TimeStp()
        m=[n]
        response = self.collection.insert_many(m)
        output = {'Status': 'Successfully Inserted'}
        return output
              

    def Search_Group(self,data):
        grp_search = data['GrpDocument']
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        p=[]
        for i in output:
            for j in i.keys():
                if j==grp_search:
                    a=(i.values())
                    for l in a:
                        for n in l:
                            out=[row for row in self.collection.find({"_id" : ObjectId(n)})]
                            p.append(out)
                    return {"Groups":f'{p}'}                                                    
                                    
        else:
            return{"Group":"Not Found"}
        

    def Delete_Group(self,data):
        grp_dele = data['Delete_Group']
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        for i in output:
            for j in i.keys():
                if j==grp_dele :
                    response = self.collection.delete_one(i)
                    return{'Status': 'Successfully Deleted'}
                    
                else:
                    return {'Status': 'Not Found'}


    def Update_Group(self,data):
        filter = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output


    def Delete_From_Particular_Grp(self,data):
               
            delete_data = data['ToBeDelete']
            grp_search = data['GrpName']
            # res=self.collection.update_many({},{'$pull':{'Mtalkz':{'$in':['63bc57aa169a5b1a0d3da0c4']}}})
            documents = self.collection.find()
            output = [{item: data[item] for item in data if item != '_id'} for data in documents]
            
            for i in self.collection.find(delete_data):
                w=i['_id']
            
            for i in output:
                for j in i.keys():
                    if j==grp_search:
                        a=(i.values())
                        for l in a:
                            for o in l:
                                if ((f'{o}')==f'{w}'):
                                    res=self.collection.update_many({},{'$pull':{f'{grp_search}':{'$in':[f'{w}']}}})
                                    return{'Status': 'Successfully Deleted'}
                    
                            
    def Delete_From_Many_Grp(self,data):
            delete_data = data['ToBeDelete']
            documents = self.collection.find()
            output = [{item: data[item] for item in data if item != '_id'} for data in documents]
            
            for i in self.collection.find(delete_data):
                w=i['_id']
            
            for i in output:
                for j in i.values():
                        if type(j)==list:
                            for m in i.keys():
                                grp_search=m
                                a=(i.values())
                                for l in a:
                                    for o in l:
                                        if ((f'{o}')==f'{w}'):
                                            res=self.collection.update_many({},{'$pull':{f'{grp_search}':{'$in':[f'{w}']}}})
            return{'Status': 'Successfully Deleted'}

    
    def Delete_From_all(self,data):
            delete_data = data['ToBeDelete']
            self.Delete_From_Many_Grp(data)
            self.Delete_Contact(data)
            return{'Status': 'Successfully Deleted'}

    def OnDate(self,data):
        date=self.data['Date']
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        flag=None
        sd="StartDate"
        ed="EndDate"
        for key,val in date.items():
            if(sd in date and ed in date):
                flag="Between"
            elif(sd in date):
                flag="After"
            elif(ed in date):
                flag="Before"
        l=[]
        l.clear()
        key="CreateAt"       
        for k in output:
            if(k[key]>val and flag=="After"):
                l.append({"After":k}) 
            elif(k[key]<val and flag=="Before"):
                l.append({"Before":k})

            elif( flag=="Between"):
                if((k[key]<=val) and (k[key]>=val)):
                        m=({"Between":k})
                        l.append(m)
        
        return(l) 
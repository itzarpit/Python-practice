import pymongo

def server():
    client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
    contact=client["Contact"]
    mycol=contact["Book"]

    return mycol
import pymongo

client = pymongo.MongoClient("mongodb+srv://DBadmin:DBpass%24123@cluster0-895fg.mongodb.net/Anvayam?"
                             + "retryWrites=true&w=majority")
db = client.Anvayam

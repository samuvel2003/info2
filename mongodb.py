import pymongo


client = pymongo.MongoClient("mongodb+srv://samuelra2003:2003@cluster0.pmzsboi.mongodb.net/?retryWrites=true&w=majority")
db = client.test


mydb = client["bbdd"]
mycol= mydb["clientes"]
myprov = mydb["proveedores"]

mydict_client = {"nombre": "juan","direccion": "C/Mayor 1"}
mydict_prov = {"nombre": "miguel","direccion": "calle 4"}

y = myprov.insert_one(mydict_prov)
x = mycol.insert_one(mydict_client)
print(x.inserted_id)
print(y.inserted_id)

#for x in mycol.find({ "nombre": 0}):

    #print(x)
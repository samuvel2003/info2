import pymongo

client = pymongo.MongoClient("mongodb+srv://samuelra2003:2003@cluster0.pmzsboi.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["veterinaria"]
mycol= mydb["mascotas"]
myprov = mydb["proveedores"]


mydict_client = {"nombre": "juan","direccion": "C/Mayor 1"}
mydict_prov = {"nombre": "miguel","direccion": "calle 4"}

y = myprov.insert_one(mydict_prov)
x = mycol.insert_one(mydict_client)
prov=list(myprov.find({"nombre":"miguel"}))
print(prov)
print("hola")
# print(x.inserted_id)
# print(y.inserted_id)

# for x in mycol.find({ "nombre": 0}):
#     print(x)

# for y in myprov.find():
#     print(y)

# myquery = {"nombre": "juan", "direccion": "C/Mayor 1"}
# newvalues = { "$set": {"nombre": "camilo"}}

# mycol.update_one(myquery,newvalues)
# #print "clientes" despues del update:
# for x in mycol.find():
#     print(x)
import pymongo
from pymongo import MongoClient

#conexión:
#con = MongoClient('localhost',27017)  #conexión local
con = pymongo.MongoClient("mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority")
db = con.datosprueba

#coleccion:
tuiteos = db.tuiteos1  

#querys:
resultado = tuiteos.find({"apporigen":"Twitter for Android"}).limit(1500)

#print ('fecha:', resultado['fecha'],'\n','usuario: ', resultado['usuario'])
#print (resultado[0]['fecha'], resultado[99]['fecha'])
#print (resultado)  #el pymongo muestra el cursor (cuando hay mas de un resultado) pero no el contenido...
#print (f"Fecha: {resultado['fecha']}, Usuario: {resultado['usuario']}")
#print (resultado)

#recorrer un cursor
for elemento in resultado:
    print(elemento)

#cerrar la conexión:
con.close()

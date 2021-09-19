import pymongo
from pymongo import MongoClient

#conexión
con = MongoClient('localhost',27017)
db = con.datosprueba

#coleccion
tuiteos = db.tuiteos

resultado = tuiteos.find().count()

#print ('fecha:', resultado['fecha'],'\n','usuario: ', resultado['usuario'])
#print (resultado[0]['fecha'], resultado[99]['fecha'])
#print (f"Fecha: {resultado['fecha']}, Usuario: {resultado['usuario']}")
print (resultado)
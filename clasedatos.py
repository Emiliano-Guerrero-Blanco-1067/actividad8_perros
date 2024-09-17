class Informacion():
    def mi_lista(self):
        lista_Nomperros=["boby","Dolar","fany"]
        for x in lista_Nomperros:
            print(x)
            
    def mi_tuplas(self):
        thistuple = ("boby","Dolar","fany")
        for x in thistuple:
            print(x)
    def mi_conjunto(self):
        thisset = {"boby","Dolar","fany"}
        for x in thisset:
            print(x)

    def mi_diccionario(self):
        thisdict =	{
        "Dalmata": "Boby",
        "Chihuahua": "Dolar",
        "Pug": "Fany"
        }
        for x, y in thisdict.items():
            print(x, y)

#creando el objeto

datos=Informacion()
print("---Listado de nombre de perros")
datos.mi_lista()
print("---Tuplas de nombre de perros")
datos.mi_tuplas()
print("---Conjunto de nombre de perros")
datos.mi_conjunto()
print("---Diccionario de nombre de perros")
datos.mi_diccionario()
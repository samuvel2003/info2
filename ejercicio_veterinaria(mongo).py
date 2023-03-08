import pymongo

class Medicamento:

    def __init__(self, client):
        mydb = client["Veterinaria"]
        self.__medicamentos = mydb[ "Medicamentos" ]

    def asignarNombreMed( self, nombreMed ):
        medicamento = { "Nombre medicamento": nombreMed }
        self.__medicamentos.insert_one( medicamento )

    def asignarDosisMed( self, nombreMed, dosisMed ):
        dicMedicamento= { "Nombre medicamento": nombreMed }
        dicDosis = { "$set" : { "Dosis": dosisMed } }
        self.__medicamentos.update_one( dicMedicamento, dicDosis )
    
    def asignarNumHistoria( self, nombreMed, numHistoria ):
        dicMedicamento= { "Nombre medicamento": nombreMed }
        my_historia = { "$set": { "Historia": numHistoria } }
        self.__medicamentos.update_one( dicMedicamento, my_historia )


class Mascota:

    def __init__( self, client, historia ):
        mydb = client["Veterinaria"]
        self.__mascota = mydb[ "Mascota" ]
        self.__historia = historia

    def asignarNomMascota(self,nombre):
        numHisto = {"Historia": self.__historia}
        lista = {"$set": { "Nombre": nombre }}
        self.__mascota.update_one(numHisto, lista)

    def asignarHistoMascota(self):
        numHisto = {"Historia": self.__historia}         
        self.__mascota.insert_one(numHisto)

    def asignarTipoMascota(self, tipo):    
        numHisto = { "Historia": self.__historia }
        lista = { "$set": { "Gato o Perro": tipo } }
        self.__mascota.update_one(numHisto, lista )

    def asignarIngresoMascota( self, fecha ):
        numHisto = { "Historia": self.__historia }
        lista = { "$set": { "Fecha": fecha } }
        self.__mascota.update_one(numHisto, lista )

    def asignarPesoMascota( self, peso ):
        numHisto = { "Historia": self.__historia }
        lista = { "$set": { "Peso": peso } }
        self.__mascota.update_one(numHisto, lista )

    def asignarMediMascota( self, medicamento ):
        numHisto = { "Historia": self.__historia }
        lista = { "$set": { "Medicamento": medicamento } }
        self.__mascota.update_one(numHisto, lista )


class Sistema:

    def __init__( self, client ):
        mydb = client["Veterinaria"]
        self.__mascota = mydb[ "Mascota" ]
        self.__medicamentos = mydb[ "Medicamentos" ]

    def SistemaEliminarMascota(self, histoClinica):
        lista = list(self.__mascota.find({ "Historia": histoClinica }))
        self.__mascota.delete_one( lista[-1] )
        lista2 = list(self.__medicamentos.find({"Historia": histoClinica}))
        for eliminar in lista2:
            self.__medicamentos.delete_one(eliminar)

    def SistemaVerMedicamento(self, histoClinica): 
        medicamentos = list(self.__medicamentos.find( { "Historia": histoClinica }))
        for medicamento in medicamentos:
            print(f" Nombre medicamneto:{medicamento['Nombre medicamento']}, Dosis: { medicamento['Dosis'] }")
            
    def SistemaVerFechaIngreso(self, histoClinica):
        lista = list(self.__mascota.find( { "Historia": histoClinica }))
        try:
            print(lista[-1]["Fecha"])
        except:
            print( "No hay ninguna fecha de ingreso registrada con ese numero de historia clinica" )        
    def SistemaVerNumeroDeMascotas(self):
        lista = list(self.__mascota.find())
        return len(lista)

    def verificarMascotaSist(self,histoClinica):
        ver = list(self.__mascota.find( { "Historia": histoClinica }))
        if len(ver) == 0:
            return False
        else: 
            return True 
#### VALIDACIONES ####

def validarEntero(a):
    try:
        a = int(a)
        return a
    except:
        b = input("Ingrese un numero entero: ")
        validarEntero(b)

######################
def main():
    client = pymongo.MongoClient("mongodb+srv://samuelra2003:2003@cluster0.pmzsboi.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    sistema = Sistema(client)

    while True:

        opc= input("""
        0- SALIR
        1- INGRESAR UNA MASCOTA
        2- ELIMINAR UNA MASCOTA
        3- VER FECHA DE INGRESO DE LA MASCOTA
        4- CONSULTAR MEDICAMENTOS DE UNA MASCOTA
        5- VER NUMERO DE MASCOTAS EN SERVICIO 
        Ingrese el numero correspondiente a su selección: """)

        if opc == '0':
            print("Fin del programa...")
            break

        elif opc == '1': 
            if sistema.SistemaVerNumeroDeMascotas() >= 10:
                print("Capacidad máxima alcanzada,no se pueden ingresar más mascotas")
                continue

            numHistoria = validarEntero(input("Número de la historia clinica de la mascota a ingresar: "))
            if sistema.verificarMascotaSist(numHistoria) == True:
                print("El numero de historia clinica ya esta registrado")
                continue
                
            nombre = input("Ingrese el nombre de la mascota: ")
            tipo = input("Ingrese CANINO o FELINO: ")
            peso = input("Ingrese el peso de la mascota en Kilogramos: ")
            fecha = input("Ingrese la fecha dd/mm/aaaa: ")
            numMed = validarEntero(input("Ingrese la cantidad de medicamentos: "))

            for i in range(0, numMed):
                medicamento = Medicamento(client)
                nombreMedicamento = input("Ingrese el nombre del medicamento: ")
                dosis = input("Ingrese la dosis del medicamento: ")
                medicamento.asignarNombreMed(nombreMedicamento)
                medicamento.asignarDosisMed(nombreMedicamento, dosis)
                medicamento.asignarNumHistoria(nombreMedicamento, numHistoria)
            
            mascota = Mascota(client, numHistoria)
            mascota.asignarHistoMascota()
            mascota.asignarNomMascota(nombre)
            mascota.asignarTipoMascota(tipo)
            mascota.asignarPesoMascota(peso)
            mascota.asignarIngresoMascota(fecha)

            print(f"Mascota {nombre} ingresada...")

        elif opc == '2':
            
            numHistoria = validarEntero(input("Ingrese el numero de la historia clinica que desea eliminar: "))
            if sistema.verificarMascotaSist(numHistoria) == False:
                print("El numero de la historia clinica ingresado no existe...")
                continue

            sistema.SistemaEliminarMascota(numHistoria)
            print("Mascota eliminada...")
        
        elif opc == '3': 
            
            numHistoria = validarEntero(input("Ingrese el numero de la historia clinica que desea ver la fecha de ingreso: "))
            if sistema.verificarMascotaSist(numHistoria) == False:
                print("El numero de la historia clinica ingresado no existe...")
                continue

            sistema.SistemaVerFechaIngreso(numHistoria)


        elif opc == '4': 
            
            numHistoria = validarEntero(input("Numero de historia de la mascota a la que le desea ver los medicamentos: "))
            if sistema.verificarMascotaSist( numHistoria ) == False:
                print("El numero de la historia clinica ingresado no existe...")
                continue

            sistema.SistemaVerMedicamento(numHistoria)
            

        elif opc == '5':
        
            print(sistema.SistemaVerNumeroDeMascotas())

        else:
            print( " Opcion no valida, ingrese el numero CORRESPONDIENTE a su selección!! " )

if __name__ == '__main__':
    main()
import pymongo

class Medicamento:

    def _init_(self, client):
        mydb = client["Veterinaria"]
        self.__medicamentos = mydb[ "Medicamentos" ]

    # LOS METODOS DE VER RESULTAN INNECESARIOS, ASI QUE LOS BORRAMOS 

    # METODOS PARA ASIGNAR
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

    def _init_( self, client, historia ):
        mydb = client["Veterinaria"]
        self.__mascota = mydb[ "Mascota" ]
        self.__historia = historia

    # ELIMINAMOS LOS METODOS DE VER YA QUE NO SON NECESARIOS

    # Metodos para asignar
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

    def _init_( self, client ):
        mydb = client["Veterinaria"]
        self.__mascota = mydb[ "Mascota" ]
        self.__medicamentos = mydb[ "Medicamentos" ]

    def SistemaEliminarMascota( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        self.__mascota.delete_one( lista[-1] )
        lista2 = list( self.__medicamentos.find( { "Historia": numHisCli } ) )
        for eliminar in lista2:
            self.__medicamentos.delete_one( eliminar )

    def SistemaVerMedicamento( self, numHisCli ): # que se esta aministrando a una mascota
        medicamentos = list( self.__medicamentos.find( { "Historia": numHisCli } ) )
        for medicamento in medicamentos:
            print( f" Nombre medicamneto: { medicamento['Nombre medicamento'] }, Dosis: { medicamento['Dosis'] } " )
            
    def SistemaVerFechaIngreso( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        try:
            print( lista[-1][ "Fecha" ] )
        except:
            print( "No hay ninguna fecha de ingreso registrada con ese numero de historia clinica" )        
    def SistemaVerNumeroDeMascotas( self ):
        lista = list( self.__mascota.find() )
        return len( lista )

    # ESTE METODO SIRVE SI SE QUIERE SALIR POR MEDIO DE ESTE, YO PUSE UN BREAK
    # def salir( self, bandera ): 
    #     bandera = False
    #     return bandera


    # ALGUNOS METODOS ADICIONALES PARA QUE EL CODIGO SEA MAS FUNCIONAL

    def SistemaVerificarMascota( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        if len( lista ) == 0:
            return False
        else: 
            return True 

######################## METODO VALIDAR INT ################################

def validarInt( a ):
    try:
        a = int( a )
        return a
    except:
        b = input( "Ingrese un numero entero: " )
        validarInt( b )

############################################################################


def main():

    client = pymongo.MongoClient("mongodb+srv://samuelra2003:2003@cluster0.pmzsboi.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    sistema = Sistema( client )

    while True:

        opcion = input( """
        (0) Salir
        (1) Ingresar mascota
        (2) Eliminar mascota
        (3) Fecha de ingreso de la mascota
        (4) Ver lista de medicamentos
        (5) Ver numero de mascotas
        > """ )

        if opcion == '0':
            print( "Fin del programa..." )
            break

        elif opcion == '1': # INGRESAR MASCOTA
            
            if sistema.SistemaVerNumeroDeMascotas() >= 10:
                print( "No hay espacio" )
                continue

            numHistoria = validarInt( input("Ingrese el numero de la historia clinica de la mascota: ") )
            if sistema.SistemaVerificarMascota( numHistoria ) ==  True:
                print( "El numero de historia clinica ya esta registrado" )
                continue
                
            name = input( "Ingrese el nombre de la mascota: " )
            type = input( "Ingrese CANINO o FELINO: " )
            weight = input( "Ingrese el peso de la mascota en Kilogramos: " )
            date = input( "Ingrese la fecha dd/mm/aaaa: " )
            med_num = validarInt( input( "Ingrese la cantidad de medicamentos: " ) )

            for i in range( 0, med_num ):
                medicamento = Medicamento( client )
                nombreMedicamento = input( "Ingrese el nombre del medicamento: " )
                dosis = input( "Ingrese la dosis del medicamento: " )
                medicamento.asignarNombreMed( nombreMedicamento )
                medicamento.asignarDosisMed( nombreMedicamento, dosis )
                medicamento.asignarNumHistoria( nombreMedicamento, numHistoria )
            
            pet = Mascota( client, numHistoria )
            pet.asignarHistoMascota()
            pet.asignarNomMascota( name )
            pet.asignarTipoMascota( type )
            pet.asignarPesoMascota( weight )
            pet.asignarIngresoMascota( date )

            print( f"Mascota {name} ingresada..." )

        elif opcion == '2': # ELIMINAR MASCOTA
            
            numHistoria = validarInt( input( "Ingrese el numero de la historia clinica que desea eliminar: " ) )
            if sistema.SistemaVerificarMascota( numHistoria ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaEliminarMascota( numHistoria )
            print( "Mascota eliminada..." )
        
        elif opcion == '3': # FECHA DE INGRESO DE LA MASCOTA
            
            numHistoria = validarInt( input( "Ingrese el numero de la historia clinica que desea ver la fecha de ingreso: " ) )
            if sistema.SistemaVerificarMascota( numHistoria ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaVerFechaIngreso( numHistoria )


        elif opcion == '4': # VER LISTA DE MEDICAMENTOS (que se esta administrando a una mascota)
            
            numHistoria = validarInt( input( "Numero de historia de la mascota a la que le desea ver los medicamentos: " ) )
            if sistema.SistemaVerificarMascota( numHistoria ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaVerMedicamento( numHistoria )
            

        elif opcion == '5': # VER NUMERO DE MASCOTAS
        
            print( sistema.SistemaVerNumeroDeMascotas() )

        else:
            print( "Opcion no valida" )

if __name__ == '_main_':
    main()
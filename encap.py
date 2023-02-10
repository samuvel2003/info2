class Ejemplo:

    def _init_( self ):
        self.__nombre = "samuel"
        self.__apellido = "velasquez"
        self.__edad = "19"

    def getNombre( self ):
        print( f"Tu nombre es: {self._nombre}, tu apellido es: {self.apellido}, tu edad es: {self._edad}" )

    def __Apellido( self ):
        print( self.__apellido )

    def getApellido( self ):
        return self.__Apellido()

persona_1 = Ejemplo()
persona_1.getNombre()
persona_1.getApellido()

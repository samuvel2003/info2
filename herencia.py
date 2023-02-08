class ave:

    def __init__(self, tipo, vuela):
        self.ave = tipo
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True

    # acciones basicas 
    def comer( self, comida ):
        print( "Este tipo de ave come normalmente " + comida )

    def volar( self ):
        print( "Este tipo de ave puede volar: " + self.vuelo )


class ganzo( ave ):

    def __init__( self, tipo, vuela, accion, pata ):
        ave.__init__(self, tipo, vuela)
        self.habilidad = accion
        self.patas = pata

    def destreza(self):
        print( "Esta ave se puede: " + self.habilidad )
    
class pato( ave ):
    pass

class gallina( ave ):
    pass

p1=ganzo("ramsey","True","volar",2)
p1.comer("arroz")
p1.volar()


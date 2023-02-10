class cosa:
    def __init__(self,publico:str="publico",protegido: str ="protegido",privado:str= "privado"):
        self.publico=publico
        self._protegido =protegido
        self.__privado =privado

    def informacion(self):
        print(
            (
                f"esta es una clase con atributos publicos: {self.publico}, "
                f"un atributo protegido: {self._protegido}, "
                f"y un archivo privado: {self.__privado}"
            )

        )

p1=cosa()
print(p1.publico)
print(p1._protegido)
print(p1.__privado)

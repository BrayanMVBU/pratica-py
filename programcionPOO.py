class Mueble:
    def __init__(self, cod,color,funcion):
        self.cod=cod
        self.color=color
        self.funcion=funcion
       
mesa=Mueble("uno","negro","comer")
print(mesa.color)




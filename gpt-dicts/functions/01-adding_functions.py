#En el contexto de la programación las funciones son la secuencia de sentencias de código con un nombre.
#Se parecen en algo a las variables en el sentido que son un simple nombre. En el caso de las variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una seria de sentencias que realizan una tarea espécifica.

#Podemos definir nuevas funciones para especificr un nombre junto con una secuencia de sentencias que se ejecutan cuando la funcion es "llamada" o "invocada"

verses = ["Mano hacia el frente", "Puño cerrado", "Dedo hacia arriba","Lengua afuera"]

def intro():
    print("Atención, copañia")

def chorus():
    print("chuchuwa,chuchuwa, chuchuwa wa wa")
    print("chuchuwa,chuchuwa, chuchuwa wa wa")

def outro():
    print("Lalala lalala lalala lala")
    print("Lalala lalala lalala lala")

for verse in verses:
    intro()
    print(verse)
    if verse != verses[-1]:
        chorus()
    else:
        outro()
    print("---------")
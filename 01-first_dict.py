#Un diccionario es como una lista, pero más general, es decir, en un diccionario los índices pueden ser casi de cualquier tipo.
#En los diccionarios los índices son llamados *llaves* o *keys* y tiene asociado sus respectivos valores.

#Ejemplo

emptydict = {} # Crea un diccionario vacío
english_to_spanish = {"one": "uno", "two": "dos"} #Crea un diccionario con dos elementos

#los elementos se agregan en pares, llave-valor

english_to_spanish ["hello"] = "hola"
english_to_spanish["bye"] ="chao"

print(english_to_spanish)

#Para acceder a el valor de una llave en específico usamos la notación con []
print(english_to_spanish["one"])

#El larfo de un Diccionario se puede obtener con la funcón len(), al igual que con las listas
print(len(english_to_spanish)) # =>4





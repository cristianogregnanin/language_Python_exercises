class persona:
    #viene creato un costruttore che a a sovrascrivere quello di default 
    def __init__ (self, nome, cognome, numero_telefono):
        #self permette di riferirsci alla nostra classe stabilendo così i relativi attributi
        self.nome = nome
        self.cognome = cognome
        self.numero_telefono = numero_telefono
    
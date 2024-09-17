print("Clases version 2 el constructor")

class Perro:
    #funcion constructor
    def __init__(self, color, edad):
        self.color=color
        self.edad=edad
    #funcion creada
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self, mensaje): 
        print(f"Chat perro: {mensaje}")
    def chatperra(self, mensajepe):
        print(f"Chat perro: {mensajepe}")
    def datos(self):
        print(f"Color {self.color} edad {self.edad}")
# crear el objeto
chihuas=Perro("Negro",2)
#llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi guggu ")
chihuas.chatperra("grrruuu......")
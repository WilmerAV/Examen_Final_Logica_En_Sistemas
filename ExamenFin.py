#inicio del programa
#importamos la libreria de Tkinter
from tkinter import ttk
from tkinter import *

# ("I Curso")
# ("II Semestre")
# ("III Su Nobre Completo")
# ("IV Su Número De Carné")
class Desk:
    def __init__(self, window):
        
        #ancho de la ventana
        ancho = 800
        
        #alto de la ventana
        alto = 500
        
        # asignamos la ventana a una VARIABLE
        self.wind = window

        #le asignamos el ancho y el alto a la ventana 
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana DEL PROGRAMA
        self.wind.title('Examen Final')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Calificaciones')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'Primer Numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Segundo Numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        

        Label(frame, text = 'Tercer Numero: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)
        

        #Creamos un boton para ejecutar las operaciones       
        Button (frame, text = 'Ejecutar', command = self.multiplicar).grid(row = 6, columnspan = 5, sticky = W + E)
        Button (frame, text = 'Imprimir', command = self.bottonImprimir).grid(row = 7, columnspan = 5, sticky = W + E)
        Button (frame, text = 'Reiniciar', command = self.multiplicar).grid(row = 7, columnspan = 5, sticky = W + E)   
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
   
    # esta es la función que ejecuta la multiplicacion de los 3 numeros
   
    def multiplicar(self):
            #aca intentamos hacer que las condiciones funcionen en el boton de ejecutar
        x=float(self.var1.get())
        y=float(self.var2.get())
        z=float(self.var3.get())
        if (x>z):
            print ("La Operacion es:", x*y*z)
            self.message['text'] = 'X es mayor La Operacion de Los Digitos es : {}'.format(x*y*z)

        elif(z==y==x):
            print ("La Suma De Estos 3 es:",x+y+z)
            self.message['text'] = 'Los 3 Digitos son Iguales : {}'.format(x+y+z)
        elif(y==0):
            print ("Ejecucion de una resta:",x-z)
            self.message['text'] = 'Y es Igual a 0 : {}'.format(x-z)
        else:
            print ("No se ingreso Ningun Numero")

    def bottonImprimir(self):
    
        x=float(self.var1.get())
        y=float(self.var2.get())
        z=float(self.var3.get())
        if(x,z,y):
          self.message['text'] = 'Concatenar : {}'.format('x''y''z')
        elif(x,z,y):
        
           self.message['text'] = 'Reptir numeros : {}'.format(x*y+z)
        else:
            print ("No se ingreso Ningun Numero")





    
#validamos si estamos en la aplicación inicial del programa
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()
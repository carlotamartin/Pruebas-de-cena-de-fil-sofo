import tkinter as tk



class window():
  def __init__ (self):
    #Creamos la ventana
    self.window = tk.Tk()
    self.window.title('La cena de los filósofos')
    self.window.configure(bg = 'gainsboro')
    self.window.geometry('600x600')


    #Creamos a los filósofos y los colocamos adecuadamente
    
    self.f1 = tk.Label(self.window, text= 'Filósofo 01', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=85, y=30)
    
    self.f1 = tk.Label(self.window, text= 'Filósofo 02', bg = 'floral white', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=160, y=75)
    
    self.f1 = tk.Label(self.window, text= 'Filósofo 03', bg = 'gold', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=170, y=130)
    
    self.f1 = tk.Label(self.window, text= 'Filósofo 04', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=50, y=130)
    
    self.f1 = tk.Label(self.window, text= 'Filósofo 05', bg = 'gold', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=30, y=75)
  


  #Hacemos el código de colores
    
    self.l1 = tk.Label(self.window, text= 'Código de colores', fg = 'black', width = 20, height = 1,font=("Arial", 14), anchor="w")
    self.l1.place(x=310, y=20)

    self.l2 = tk.Label(self.window, text= 'Filósofo entra a comer', bg = 'pale violet red', fg = 'black', width = 20, height = 1, anchor="w")
    self.l2.place(x=340, y=50)

    self.l3 = tk.Label(self.window, text= 'Filósofo tiene un tenedor', bg = 'cyan2', fg = 'black', width = 20, height = 1, anchor="w")
    self.l3.place(x=340, y=80)
    self.l4 = tk.Label(self.window, text= 'Filósofo está comiendo', bg = 'gold', fg = 'black', width = 20, height = 1, anchor="w")
    self.l4.place(x=340, y=110)

    self.l5 = tk.Label(self.window, text= 'Filósofo está pensando',bg = 'floral white',  fg = 'black', width = 20, height = 1, anchor="w")
    self.l5.place(x=340, y=140)

    self.l6 = tk.Label(self.window, text= 'Tenedor ocupado',  bg = 'blue2', fg = 'black', width = 20, height = 1, anchor="w")
    self.l6.place(x=340, y=170)

    self.l7 = tk.Label(self.window, text= 'Tenedor libre', bg = 'ivory2', fg = 'black', width = 20, height = 1, anchor="w")
    self.l7.place(x=340, y=200)


    #Creamos los botones de abajo

    self.boton_inicio= tk.Button(self.window,text = 'Iniciar',fg = 'black', width = 7, height = 1, command = self.run)
    self.boton_inicio.place(x = 50, y = 400)
    self.boton_pausar= tk.Button(self.window, text = 'Pausar',fg = 'black', width = 7, height = 1, command = self.close)
    self.boton_pausar.place(x = 150, y = 400)
    self.boton_reset= tk.Button(self.window, text = 'Reset',fg = 'black', width = 7, height = 1, command = self.close)
    self.boton_reset.place(x = 250, y = 400)
    self.boton_salir= tk.Button(self.window, text = 'Salir',fg = 'black', width = 7, height = 1, command = self.close)
    self.boton_salir.place(x = 350, y = 400)
    self.boton_creditos= tk.Button(self.window, text = 'Créditos', fg = 'black', width = 7, height = 1, command = self.close)
    self.boton_creditos.place(x = 450, y = 400)
    
    


    #Hacemos el cuadrado de texto de abajo
    
    self.texto = tk.Text(self.window, height=10, width = 30) #texto donde va a ir los filósofos pensando
    self.scroll = tk.Scrollbar(self.window) #establecemos que nuestra ventana va a tener una barra deslizante
    self.texto.configure(yscrollcommand = self.scroll.set) #configuramos netsra barra deslizante dentro de nuetro texto
    self.texto.place(x = 12,  y =190)
    self.scroll.config (command= self.texto.yview)
    self.scroll.pack(side = tk.RIGHT, fill=tk.Y)
  def imprimir(self, texto):
      self.texto.insert(tk.END, str(texto) + '\n')

  def close(self):
      self.window.withdraw()
    
  def run(self):
      self.window.mainloop()
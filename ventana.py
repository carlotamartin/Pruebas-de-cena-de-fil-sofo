import tkinter as tk



class window():
  def __init__ (self):
    self.root = tk.Tk()
    self.root.title('La cena de los filósofos')
    self.root.configure(bg = 'gainsboro')
    self.root.geometry('600x600')


    #Creamos a los filósofos
    self.f1 = tk.Label(self.root, text= 'Filósofo 01', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    
    self.f1.place(x=85, y=30)
    self.f1 = tk.Label(self.root, text= 'Filósofo 02', bg = 'floral white', fg = 'black', width = 9, height = 2)
    self.f1.place(x=160, y=75)
    self.f1 = tk.Label(self.root, text= 'Filósofo 03', bg = 'gold', fg = 'black', width = 9, height = 2)
    self.f1.place(x=170, y=130)
    self.f1 = tk.Label(self.root, text= 'Filósofo 04', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    self.f1.place(x=50, y=130)
    self.f1 = tk.Label(self.root, text= 'Filósofo 05', bg = 'gold', fg = 'black', width = 9, height = 2)
    self.f1.place(x=30, y=75)


    '''
    self.texto = tk.Text(self.root, height=12, width = 35) #texto donde va a ir los filósofos pensando
    self.scroll = tk.Scrollbar(self.texto, command = self.texto.yview) #establecemos que nuestra ventana va a tener una barra deslizante
    self.texto.configure(yscrollcommand = self.scroll.set) #configuramos netsra barra deslizante dentro de nuetro texto
    self.texto.place(x = 10,  y =185)
    self.scroll.config (command= self.texto.yview)
    self.scroll.pack(side = tk.RIGHT, fill= tk.Y)
'''




    #Hacemos el cuadrado de texto de abajo
    self.frame = tk.Frame(self.root,height=12, width = 35)

    self.frame.place(x = 10,  y =185)

    self.scrollbar = tk.Scrollbar(self.frame)
    self.textt= tk.Text(self.frame,height=10, width = 33, yscrollcommand = self.scrollbar.set)
    self.scrollbar.config(command = self.textt.yview)
    self.scrollbar.pack(side= tk.RIGHT, fill = tk.Y)
    self.textt.pack(side = 'left')

#Hacemos el código de colores
    
    self.l1 = tk.Label(self.root, text= 'Código de colores', fg = 'black', width = 20, height = 1,)
    self.l1.place(x=300, y=30)

    self.c2 = tk.Label(self.root, text= '', bg = 'pale violet red', width = 1, height = 1)
    self.c2.place(x=300, y=50)

    self.l2 = tk.Label(self.root, text= 'Filósofo entra a comer', fg = 'black', width = 20, height = 1)
    self.l2.place(x=330, y=50)

    self.c3 = tk.Label(self.root, text= '', bg = 'cyan2', width = 1, height = 1)
    self.c3.place(x=300, y=80)
    
    self.l3 = tk.Label(self.root, text= 'Filósofo tiene un tenedor', fg = 'black', width = 20, height = 1)
    self.l3.place(x=335, y=80)

    self.c4 = tk.Label(self.root, text= '', bg = 'cyan2', width = 1, height = 1)
    self.c4.place(x=300, y=80)

    self.l4 = tk.Label(self.root, text= 'Filósofo está comiendo', fg = 'black', width = 20, height = 1)
    self.l4.place(x=340, y=110)

    self.c5 = tk.Label(self.root, text= '', bg = 'gold', width = 1, height = 1)
    self.c5.place(x=300, y=80)

    self.l5 = tk.Label(self.root, text= 'Filósofo está pensando', fg = 'black', width = 20, height = 1)
    self.l5.place(x=340, y=140)

    self.c6 = tk.Label(self.root, text= '', bg = 'floral white', width = 1, height = 1)
    self.c6.place(x=300, y=80)

    self.l6 = tk.Label(self.root, text= 'Tenedor ocupado', fg = 'black', width = 20, height = 1)
    self.l6.place(x=340, y=170)

    self.c7 = tk.Label(self.root, text= '', bg = 'blue2', width = 1, height = 1)
    self.c7.place(x=300, y=80)

    self.l7 = tk.Label(self.root, text= 'Tenedor libre', fg = 'black', width = 20, height = 1)
    self.l7.place(x=340, y=200)

    self.c2 = tk.Label(self.root, text= '', bg = 'ivory2', width = 1, height = 1)
    self.c2.place(x=300, y=80)

    

    
  
    self.root.mainloop()

  def imprimir(self, texto):
    self.texto.insert(tk.END, str(texto) + '\n')


  def glosario(self):
    self.l1 = tk.Label(self.root, text= 'Código de colores', fg = 'black', width = 9, height = 2)
    self.l1.place(x=200, y=30)

    self.l2 = tk.Label(self.root, text= 'Filósofo entra a comer', fg = 'black', width = 9, height = 2)
    self.l2.place(x=210, y=50)
    self.l3 = tk.Label(self.root, text= 'Filósofo está comiendo', fg = 'black', width = 9, height = 2)
    self.l3.place(x=210, y=50)
    

  
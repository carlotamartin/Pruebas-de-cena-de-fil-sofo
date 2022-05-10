import tkinter as tk


class window():
  def __init__ (self):
    self.root = tk.Tk()
    self.root.title('La cena de los filósofos')
    self.root.configure(bg = 'gainsboro')
    self.root.geometry('500x400')


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


    
    self.texto = tk.Text(self.root, height=12, width = 35) #texto donde va a ir los filósofos pensando
    self.scroll = tk.Scrollbar(self.root) #establecemos que nuestra ventana va a tener una barra deslizante
    self.texto.configure(yscrollcommand = self.scroll.set) #configuramos netsra barra deslizante dentro de nuetro texto
    self.texto.place(x = 10,  y =185)
    self.scroll.config (command= self.texto.yview)
    self.scroll.pack(side = tk.RIGHT, fill= tk.Y)
  
    self.root.mainloop()

  def imprimir(self, texto):
    self.texto.insert(tk.END, str(texto) + '\n')

  
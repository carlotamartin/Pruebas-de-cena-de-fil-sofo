from tkinter import *


class window():
  def __init__ (self):
    self.root = Tk()
    self.root.title('La cena de los filósofos')
    self.root.configure(bg = 'gainsboro')
    self.root.geometry('500x400')


    #Creamos a los filósofos
    self.f1 = Label(self.root, text= 'Filósofo 01', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    self.f1.place(x=85, y=30)
    self.f1 = Label(self.root, text= 'Filósofo 02', bg = 'floral white', fg = 'black', width = 9, height = 2)
    self.f1.place(x=160, y=75)
    self.f1 = Label(self.root, text= 'Filósofo 03', bg = 'gold', fg = 'black', width = 9, height = 2)
    self.f1.place(x=155, y=120)
    self.f1 = Label(self.root, text= 'Filósofo 04', bg = 'pale violet red', fg = 'black', width = 9, height = 2)
    self.f1.place(x=50, y=130)
    self.f1 = Label(self.root, text= 'Filósofo 05', bg = 'gold', fg = 'black', width = 9, height = 2)
    self.f1.place(x=30, y=75)




    self.canvas = Canvas(self.root)
    self.canvas.place(x=9,y=150)
    self.scrollbar = Scrollbar(self.canvas, orient = VERTICAL)
    self.scrollbar.pack(side = RIGHT, fill = Y)

    #Button(self.root, text = 'Filósofo 1', width = 50, bg = 'blue', fg = 'white').place(x=85, y =75)

    '''
    self.frame_f = Frame (self.root, width = 480, height = 320)
    self.frame_f.pack(fill='both', expand=0.5)
    self.frame_f.config(cursor="pirate")
    self.frame_f.config(bg="lightblue")
    self.frame_f.config(bd=25)
    self.frame_f.config(relief="sunken")
    '''





    
    #self.frame_f.pack()
  
  
    self.root.mainloop()
#Daniel Enrique Zaldaña Castillo SMIS068421
#Moises Antonio Martínez SMIS071221
#Se importan todas las librerias que se van a usar 
from tkinter import Tk,Button,Label,filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

#Se crea una funcion que cargue una imagen
def update():
    
    archivo=filedialog.askopenfilename()
    global imagen1
    imagen1=Image.open(archivo)
    imagenresiz2=imagen1.resize((250,250), Image.Resampling.LANCZOS)
    render2=ImageTk.PhotoImage(imagenresiz2)
    label2.configure(image=render2)
    label2.image=render2
    label2.place(x=50,y=60)

#Se crea una funcion que agregue el filtro de B/N    
def filterBN():
   
    imagen2 = imagen1
    imagen2.mode
    imagen2 = imagen2.convert("L")
    messagebox.showinfo('PIL','La imagen se convirtio en B/N')
    imagen2.show()

#Se crea una funcion que agregue el filtro de Desenfoque     
def filterDes():
    
    imagen2 = imagen1.filter(ImageFilter.BLUR)
    messagebox.showinfo('PIL','La imagen se desenfoco')
    imagen2.show()

#Se crea una funcion que agregue el filtro de Contorno       
def filterCon():
    
    imagen2 = imagen1.filter(ImageFilter.CONTOUR)
    messagebox.showinfo('PIL','La imagen tiene contorno')
    imagen2.show()

#Se crea una funcion que agregue el filtro de Resaltar        
def filterRes():
    
    imagen2 = imagen1.filter(ImageFilter.EMBOSS)
    messagebox.showinfo('PIL','La imagen se resalto')
    imagen2.show()

#Se crea la ventana de la aplicacion 
ventana=Tk()
ventana.title("Gestor de pillow")
ventana.geometry("1500x1000")
ventana.configure(bg="#3DB134")

#Se crea un label donde se cargara la imagen
label2=Label(ventana, image="")
label2.place(x=20, y=70, width=800, height= 500)

#Se crea un boton que cargue la imagen
btn1= Button(ventana, text="Cargar imagen", command=update)
btn1.place(x=1050, y=400, width= 190)

#Se crea un boton que agrega el filtro B/N
btn2=Button(ventana, text="B/N", command= filterBN)
btn2.place(x=350, y=700)
 
 #Se crea un boton que agrega el filtro Desenfocar
btn3=Button(ventana, text="Desenfocar", command= filterDes)
btn3.place(x=550, y=700)

#Se crea un boton que agrega el filtro Contorno
btn4=Button(ventana, text="Contorno", command= filterCon)
btn4.place(x=750, y=700)

#Se crea un boton que agrega el filtro Resaltar
btn4=Button(ventana, text="Resaltar", command= filterCon)
btn4.place(x=950, y=700)
 



ventana.mainloop()


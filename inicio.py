from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import messagebox as mb
from signin import login
from formulario import formularios





def index():

    

    window = Tk()
    window.geometry("1100x900")
    window.config(bg="#2E4053")
    window.resizable(0,0)
    window.title("Vision Artificial")



        
        

    H1=Label(window, text="Reconocimiento Facial")
    H1.config(
            bg= "#274661",
            font=("Courier", 34, "bold"),
            pady=20,
            bd= 5,
            relief="ridge",
            fg="white",    
        )

    H1.grid(row=0,column=0, sticky="N", ipadx="280")
    image = Image.open("C:/Users/Kevin Jaramillo/Desktop/DjangoCurso/tkinter/imagenes/computer-vision.jpg")
    image = image.resize((500, 800), Image. ANTIALIAS)#Carga la imagen en la variable render   
            #biar el tamaño de la imagen ancho y alto
        
    render = ImageTk.PhotoImage(image)
    Label(window,image=render).place(x=3, y=100 )
        

    texto = Label(window,text="Accede con tus credenciales")
    texto.config(fg= "#DDDFE9",
            bg= "#2E4053",
            font=("Arial", 20, 
            "bold"),
            ),
    texto.place(x=575, y=150, width=450, height=50)

    
    entrar = Button(window, text="Acceder",cursor="hand2", command= login)
    entrar.config(
            bg= "#C0DC14",
            font=("Arial", 15, "bold"),
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        ),
    entrar.place(x=670, y= 340, width=250, height=80)

    registrar = Button(window, text="Registrarse", cursor="hand2",command= formularios)
    registrar.config(
            bg= "#C0DC14",
            font=("Arial", 15, "bold"),
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        )
    registrar.place(x=670, y= 520, width=250, height=85)

    window.mainloop()
    


index()











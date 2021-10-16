from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox
import sqlite3
import pymysql 
from scipy.optimize._root import root


def formularios():

    
    root = Tk()
    root.geometry("700x500")
    root.title("Formulario de Registro")
    root.resizable(0,0)
    root.iconbitmap("C:/Users/Kevin Jaramillo/Desktop/DjangoCurso/tkinter/imagenes/robot.ico")
   
   
    
    usuario_Entryf = StringVar()
    contraseña_Entryf = StringVar()
   
    


    etiq1= Label(root, text="Nombres ")
    etiq1.config(
                fg="black", padx=5, 
                
                font=("Courier", 14, "bold")
            )
    etiq1.grid( column=0, row=1, pady=17)

    nombre = Entry(root,)
    nombre.grid( column=1, row=1, ipadx=90, ipady=4)  




    etiq2= Label(root, text="Apellidos ")
    etiq2.config(
                fg="black", 
            
                
                font=("Courier", 14, "bold")
            )
    etiq2.grid( column=0, row=2, pady=17, ipadx=90, ipady=4)

    apellidos = Entry(root,)
    apellidos.grid( column=1, row=2, ipadx=90, ipady=4)  


    etiq3= Label(root, text="DNI" )
    etiq3.config(
                fg="black", padx=5, 
                
                font=("Courier", 14, "bold")
            )
    etiq3.grid( column=0, row=3, pady=17)

    dni = Entry(root)
    dni.grid( column=1, row=3, ipadx=90, ipady=4)  

    etiq4= Label(root, text="Correo")
    etiq4.config(
                fg="black", padx=5, 
                
                font=("Courier", 14, "bold")
            )
    etiq4.grid( column=0, row=4, pady=17)

    usuario_Entryf = Entry(root, )
    usuario_Entryf.grid( column=1, row=4, ipadx=90, ipady=4 )  



    etiq5 = Label(root, text="Password")
    etiq5.config(
            fg="black", padx=5, 
                
                font=("Courier", 14, "bold")
        )
    etiq5.grid( column=0, row=5, pady=17)

    contraseña_Entryf = Entry(root,  )
    contraseña_Entryf.grid( column=1, row=5, ipadx=90, ipady=4)


    registrate = Button(root, text="Registrate")
    registrate.config(
            width=20,
            background="#C0DC14",
        
            pady= 10,
            font=("Arial", 12, "bold"),
            bd= 0,
                highlightbackground="#C0DC14",#Border de la ventana
                highlightthickness=2

        )
    registrate.grid( column=1, row=6)
    
     


    mainloop()


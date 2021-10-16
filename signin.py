from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import messagebox as mb
import cv2
import imutils




    
    
def login():
   
    pantalla= Tk()
    pantalla.geometry("500x500")
    pantalla.title("Inicio de Sesion")
    pantalla.resizable(0,0)
    pantalla.iconbitmap("C:/Users/Kevin Jaramillo/Desktop/DjangoCurso/tkinter/imagenes/robot.ico")
    pantalla.config(bg="#2E4053")
    
    
    
    correo = Label(pantalla, text="Correo Electrónico")
    correo.config(fg= "#13267C",
            bg="#D5DBDB" ,
            justify="center",
            font=("Arial", 15, "bold"),
            ),
    correo.place(x= 120, y = 70, width=210, height=50)
        

    Ecorreo = Entry(pantalla, )
    Ecorreo.config(
            font=("Arial", 15, "bold"),
            fg= "#13267C",
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        
                                    
        )
    Ecorreo.place(x=60, y=140, width=340,height=35)

    password = Label(pantalla, text="Contraseña")
    password.config(fg= "#13267C",
            bg="#D5DBDB" ,
            justify="center",
            font=("Arial", 15, "bold"),
            ),
    password.place(x= 120, y =200, width=210, height=50)
        

    Epassword = Entry(pantalla, )
    Epassword.config(
            font=("Arial", 9, "bold"),
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        
                                    
        )
    Epassword.place(x=60, y=270, width=340,height=35)

    cam = Button(pantalla, text="CAM",cursor="hand2", command= video)
    cam.config(
            bg= "#C0DC14",
            font=("Arial", 15, "bold"),
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        )
    cam.place(x=30, y= 360, width=200, height=60)

    entrar = Button(pantalla, text="ENTRAR",cursor="hand2", command= video, state="disabled")
    entrar.config(
            bg= "#C0DC14",
            font=("Arial", 15, "bold"),
            justify="center",
            bd= 0,
            highlightbackground="#C0DC14",#Border de la ventana
            highlightthickness=2,
        )
    entrar.place(x=250, y= 360, width=200, height=60)

    
    
    pantalla.mainloop()



def video():
    faceClassif= cv2.CascadeClassifier('C:/Users/Kevin Jaramillo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/Users/Kevin Jaramillo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, imagen = cap.read()
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = imagen[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        if ret==True:
            cv2.imshow('Reconocimiento Facial', imagen)
            if cv2.waitKey(1) & 0xFF == ord('s'):#Tecla Salir
                break
        
    cap.release()
    cv2.destroyAllWindows()
            
        




    
    
    
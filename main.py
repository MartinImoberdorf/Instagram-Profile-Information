import time
from tkinter import *
import PIL.Image
import PIL.ImageTk
import instaloader
import requests 
import shutil
from tkinter import messagebox

def instagram(nombreUsuario):
        bot = instaloader.Instaloader()

        image_url = "imagen.png"
        profile = instaloader.Profile.from_username(bot.context, nombreUsuario)
        filename = image_url.split("/")[-1]

        nombre=profile.username
        id=profile.userid
        post=profile.mediacount
        seguidores=profile.followers
        seguidos=profile.followees
        bio=profile.biography

        image_url = profile.get_profile_pic_url()
        r = requests.get(image_url, stream = True)

        with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)

        if profile.is_private==True:
                privadoPublico="Usuario privado"
        else:
                privadoPublico="Usuario publico"
        
        return nombre,id,post,seguidores,seguidos,bio,privadoPublico


def dataRecuperada():

    global usuarioBuscar
    global dataUsuario
    usuarioBuscar=usuarioVar.get()
    if usuarioBuscar != "":
        usuarioVar.set("")
        messagebox.showinfo(title=None, message="Buscando información")
        dataUsuario=instagram(usuarioBuscar)
        time.sleep(5)
        ventanaSecundaria()

    else:
        messagebox.showwarning(title=None, message="Ingrese el usuario a buscar")
    


def ventanaInicial():
    root=Tk()

    ancho_ventana =300
    alto_ventana=250

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("Instagram")
    root.resizable(width=False,height=False)
    root.iconbitmap('logo.ico')



    titulo=Label(root,text="Instagram",width=25,background="white",fg="black",font=("Arial Black",30)).place(x=150,y=50,anchor=CENTER,height=40)

    global usuarioVar
    usuarioVar=StringVar()
    usuario=Entry(root,width=25,background="white",fg="black",font=("Calibri Light",15),relief="groove",textvariable=usuarioVar).place(x=150,y=120,anchor=CENTER,height=40)

    buscar=Button(root,text="Buscar",width=10,background="white",fg="black",font=("Calibri Light",15),relief="groove",command=dataRecuperada).place(x=150,y=175,anchor=CENTER,height=40)


    root.mainloop()


def ventanaSecundaria():
    
    root=Toplevel()

    ancho_ventana =600
    alto_ventana=300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("Instagram")
    root.resizable(width=False,height=False)
    root.iconbitmap('logo.ico')


    im = PIL.Image.open("imagen.png")
    photo = PIL.ImageTk.PhotoImage(im)


    imagenPerfil=Label(root,image=photo,height=200,width=200).place(x=30,y=30)

    nombreUsuario=Label(root,text=dataUsuario[0],height=1,width=15,background="white",fg="black",font=("Arial Black",25)).place(x=250,y=30)
    
    publicacionesLabel=Label(root,text="Publicaciones",height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=250,y=90)
    seguidoresLabel=Label(root,text="Seguidores",height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=368,y=90)
    seguidosLabel=Label(root,text="Seguidos",height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=485,y=90)

    numeroPublicaciones=Label(root,text=dataUsuario[2],height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=250,y=110)
    numeroSeguidores=Label(root,text=dataUsuario[3],height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=368,y=110)
    numerosSeguidos=Label(root,text=dataUsuario[4],height=1,width=15,background="white",fg="black",font=("Calibri Light",10)).place(x=485,y=110)

    biografia=Label(root,text=dataUsuario[5],height=5,width=48,background="white",fg="black",font=("Calibri Light",10),relief="groove").place(x=250,y=150)

    LabelID=Label(root,text="ID:",background="white",fg="black",font=("Calibri Light",10)).place(x=30,y=250)
    id=Label(root,text=dataUsuario[1],background="white",fg="black",font=("Calibri Light",10)).place(x=50,y=250)

    privadoPublico=Label(root,text=dataUsuario[6],background="white",fg="black",font=("Calibri Light",10)).place(x=500,y=250)

    root.mainloop()


if __name__ == '__main__':
        ventanaInicial()
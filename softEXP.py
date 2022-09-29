from tkinter import *



def Ingles():
    ventana.withdraw()
    ventana2 = Toplevel()
    ventana2.title("Guesser")
    ventana2.geometry("400x250")
    
    
    def calcular():
    
        k=num1.get()/9
        a=(num2.get()-k)/2
        b=(num2.get()+k)/2
        var= str(int(b)) + str(int(a))
        return resultado.set(var)

    

    num1=IntVar()
    num2=IntVar()
    resultado=IntVar()

    lbl1=Label(ventana2,text="1- Think of a two-digit number (not equal).")
    lbl1.place(x=20,y=0) 

    lbl2=Label(ventana2,text="2- Now reverse the order of the figures.") 
    lbl2.place(x=20,y=30)

    lbl3=Label(ventana2,text="3- So, subtract the number you thought first from the new number")
    lbl3.place(x=20,y=60)

    lbl4=Label(ventana2,text="Type the numbers you got ------->")
    lbl4.place(x=20,y=90)
    box1=Entry(ventana2,textvariable=num1,width=10)
    box1.place(x=250,y=90)

    lbl5=Label(ventana2,text="4- Now add the numbers of the number you thought at the beginning")
    lbl5.place(x=20,y=120)

    lbl6=Label(ventana2,text="Type the numbers you got ------->")
    lbl6.place(x=20,y=150)
    box2=Entry(ventana2,textvariable=num2,width=10)
    box2.place(x=250,y=150)

    btn=Button(ventana2,text="You thought: ", command=calcular)
    btn.place(x=20,y=200)

    res=Entry(ventana2,textvariable=resultado,width=10, state="readonly")
    res.place(x=150,y=200)


    bt_ingles=Button(ventana2,text="Cambiar a Ingles",command=Ingles)
    bt_ingles.place(x=20,y=250)

    ventana2.resizable(False,False)
    ventana2.mainloop()




ventana=Tk()
ventana.title("Adivinador")
ventana.geometry("350x300")


def calcular():
    
    k=num1.get()/9
    a=(num2.get()-k)/2
    b=(num2.get()+k)/2
    var= str(int(b)) + str(int(a))
    return resultado.set(var)


num1=IntVar()
num2=IntVar()
resultado=IntVar()

lbl1=Label(ventana,text="1- Piense un numero de 2 cifras que no sean iguales")
lbl1.place(x=20,y=0) 

lbl2=Label(ventana,text="2- Inverti el orden de las cifras") 
lbl2.place(x=20,y=30)

lbl3=Label(ventana,text="3- Reste el numero pensado con el invertido")
lbl3.place(x=20,y=60)

lbl4=Label(ventana,text="Ingrese el resultado de la resta ------->")
lbl4.place(x=20,y=90)
box1=Entry(ventana,textvariable=num1,width=10)
box1.place(x=250,y=90)

lbl5=Label(ventana,text="4- Suma los digitos del numero que pensaste al principio")
lbl5.place(x=20,y=120)

lbl6=Label(ventana,text="Ingrese el resultado de la suma ------->")
lbl6.place(x=20,y=150)
box2=Entry(ventana,textvariable=num2,width=10)
box2.place(x=250,y=150)

btn=Button(ventana,text="Tu numero es: ", command=calcular)
btn.place(x=20,y=200)

res=Entry(ventana,textvariable=resultado,width=10, state="readonly")
res.place(x=150,y=200)


bt_ingles=Button(ventana,text="Cambiar a Ingles",command=Ingles)
bt_ingles.place(x=250,y=270)


ventana.resizable(False,False)
ventana.mainloop()
from tkinter import *
alfabeto = "¨FCDE$AGHI1@JBKLM!N7PQ%SR3?TUVWX#4Z23Y56O890&*"

class Aplication:
    def __init__(self,root):

        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="Info", command=self.Info)
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)

        root.geometry("500x150")
        root.title("Gabscript")
        root.config(menu=self.menubar)

        self.contaneirL = Frame(root)
        self.contaneirL.pack()
        self.contaneir2Frase = Frame(root)
        self.contaneir2Frase.pack()
        self.contaneir2Chave = Frame(root)
        self.contaneir2Chave.pack()
        self.contaneir3 = Frame(root)
        self.contaneir3.pack()
        self.contaneir4 = Frame(root)
        self.contaneir4.pack(fill="both")

        self.lblLogo = Label(self.contaneirL,text="GABSCRIPT")
        self.lblLogo.pack()

        self.lblfrase = Label(self.contaneir2Frase, text="Frase:")
        self.lblfrase.pack(side = LEFT)
        self.frase = Entry(self.contaneir2Frase,width=50)
        self.frase.pack()

        self.lblchave = Label(self.contaneir2Chave, text="Chave:")
        self.lblchave.pack(side=LEFT)
        self.chave = Entry(self.contaneir2Chave, width=50)
        self.chave.pack()

        self.cript = Button(self.contaneir3,text="Criptografar",command=self.Cript)
        self.cript.pack(side=LEFT)
        self.decript = Button(self.contaneir3, text="Descriptografar", command=self.Decript)
        self.decript.pack(side=RIGHT)

        self.lbl = Label(self.contaneir4, text="Digite a frase que você deseja criptografar ou descriptografar com a senha de 0-6")
        self.lbl.pack(fill="both")
    def Cript(self):
        codigo = ''
        #alfabeto = "¨FCDE$AGHI1@JBKLM!N7P%SR3?TUVQWX#4Z23Y56O890&*"
        try:
            n = int(self.chave.get())
        except:
            self.lbl['text'] = "Digite um numero de 1-6"
        a = 0
        b = 0
        frase = self.frase.get()
        frase = frase.replace(" ", "¨")
        frase = frase.upper()
        while len(codigo) < len(frase):
            if len(frase) == a:
                a = 0
            if len(alfabeto) == b:
                b = 0
            if frase[a] == alfabeto[b]:
                g = b + n
                if g >= len(alfabeto):
                    g -= len(alfabeto)
                codigo += (alfabeto[g])
                b = 0
                a += 1
            b += 1
        Final = "Seu codigo é: "+codigo +" Com a chave: " + str(n)
        self.lbl['text'] = Final
    def Decript(self):
            codigo = ''
            #alfabeto = "¨FCDE$AGHI1@JBKLM!N7P%SR3?TUVQWX#4Z23Y56O890&*"
            n = int(self.chave.get())
            a = 0
            b = 0
            frase = self.frase.get()
            frase = frase.upper()
            while len(codigo) < len(frase):
                if len(frase) == a:
                    a = 0
                if len(alfabeto) == b:
                    b = 0
                if frase[a] == alfabeto[b]:
                    g = b - n
                    if g <= len(alfabeto):
                        g -= len(alfabeto)
                    codigo += alfabeto[g]
                    b = 0
                    a += 1
                b += 1
            codigo = codigo.replace("¨", " ")
            Final = "A frase é: " + codigo + " Com a chave: "+ str(n)
            self.lbl['text'] = Final
    def Info(self):
        info = Tk()
        self.lbl1 = Label(info,text="Gabriel Miranda 2019")
        self.lbl1.pack()
root = Tk()
Aplication(root)
mainloop()

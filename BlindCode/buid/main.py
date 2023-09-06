import os
import customtkinter as ctk
import tkinter as tk
import shutil
import getpass


app = ctk.CTk("black")
app.geometry("400x600")
app.title("BlindCode")
os.chdir(os.path.join(r"C:\Users",os.getlogin(), "Documents", "BlindCode","buid"))
app.iconbitmap("icon.ico")
app.resizable(False, False)

def pyblindit():
    print("BlindCode is running")
    os.chdir(r"C:\Users\kryst\Documents\BlindCode Outputs")
    os.mkdir(pyentry.get())
    os.chdir(pyentry.get())
    addons_INSTALL = open("MINSTALLER.bat", 'w')
    addons_INSTALL.write("pip install -r requirements.txt")
    addons_INSTALL.close()
    os.chdir(r"C:\Users\kryst\Documents\BlindCode_prepare_cache")
    reqdir_path = os.path.join(r"C:\Users\kryst\Documents\BlindCode Outputs",pyentry.get())
    shutil.move("requirements.txt",reqdir_path)
    shutil.move("main.py",reqdir_path)
def arblindit():
    pass



def BCOpaths():
    getpass = os.getlogin()
    current_path = os.path.join(r"C:\Users", getpass, "Documents","BlindCode", "BlindCode Outputs")     

    return current_path    

def BCPCpaths():
    getpass = os.getlogin()
    current_path = os.path.join(r"C:\Users", getpass, "Documents","BlindCode", "BlindCode_prepare_cache")     

    return current_path            
    




































#prebuid module entry tabs and add custom modules

def pycmodules():
    
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write(pycmentry.get() + '\n')
    addons.close

def arcomodules(name):
    aroutputs = r'C:\Users\kryst\Documents\BlindCode Outputs' + arcmentry.get()
    os.chdir(aroutputs)
    addons = open("requirements.txt", 'a')
    addons.write('arcomodules \n')
    addons.close
    def m5stack():
        os.chdir(r'C:\Users\kryst\Documents\BlindCode_prepare_cache')
        addons = open("requirements.txt", 'a')
        addons.write('m5stack \n')
        addons.close()
        pysetup  = open('main.py', 'a')
        pysetup.write('import m5stack\n')
        pysetup.close()
    
def gradio():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('gradio \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import gradio\n')
    pysetup.close()


def tkinter():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('tkinter \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import tkinter\n')
    pysetup.close()

def customtkinter():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('customtkinter \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import customtkinter as ctk\n')
    pysetup.close()

def pyinstaller():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('pyinstaller \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import pyinstaller\n')
    pysetup.close()

def openai():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('openai \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import openai\n')
    pysetup.close()
def espmdns():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('espmdns \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import espmdns\n')
    pysetup.close()

def m5stack():
    os.chdir(BCPCpaths());
    addons = open("requirements.txt", 'a')
    addons.write('m5stack \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import m5stack\n')
    pysetup.close()
def gradio():
    os.chdir(BCPCpaths());
    addons = open("requirements.txt", 'a')
    addons.write('gradio \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import gradio as gr\n')
    pysetup.close()

def tkinter():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('tkinter \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import tkinter as tk\n')
    pysetup.close()
def customtkinter():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('customtkinter \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import customtkinter\n')
    pysetup.close()

def pyinstaller():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('pyinstaller \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import pyinstaller\n')
    pysetup.close()

def openai():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('openai \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import openai\n')
    pysetup.close()
def espmdns():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('espmdns \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import espmdns\n')
    pysetup.close()
def requests():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('requests \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import requests\n')
    pysetup.close()
def beautifulsoup4():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('beautifulsoup4 \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import beautifulsoup4\n')
    pysetup.close()
def numpy():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('numpy \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import numpy\n')
    pysetup.close()

def matplotlib():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('matplotlib \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import matplotlib\n')
    pysetup.close()

def pandas():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('pandas \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import pandas\n')
    pysetup.close()
def scipy():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('scipy \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import scipy\n')
    pysetup.close()
def sqlalchemy():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('sqlalchemy \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import sqlalchemy\n')
    pysetup.close()
def webserver():
    os.chdir(BCPCpaths())
    addons = open("requirements.txt", 'a')
    addons.write('webserver \n')
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write('import webserver\n')
    pysetup.close()



def TtT():
    os.chdir(BCPCpaths())
    addons = open("gradiobasicTaT.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()

def TtI():
    os.chdir(BCPCpaths())
    addons = open("gradiobasicTaP.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()

def ItT():
    os.chdir(BCPCpaths())
    addons = open("gradiobasicPaT.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()

def ItI():
    os.chdir(BCPCpaths())
    addons = open("gradiobasicPaP.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()

def CTKLogin():
    os.chdir(BCPCpaths())
    addons = open("CustomTkinterLogin.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()

def CTKTabs():
    os.chdir(BCPCpaths())
    addons = open("CustomTkinterTabView.txt", 'r')
    code = addons.read()
    addons.close()
    pysetup  = open('main.py', 'a')
    pysetup.write(code)
    pysetup.close()




        




























#Enviroment tabs
frame = ctk.CTkFrame(app,fg_color="black",border_color="white",border_width=2,)
frame.place(x=0, y=0, relwidth=1, relheight=1,)

tabs = ctk.CTkTabview(frame,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
tabs.place(relx=0, rely=0, relwidth=1, relheight=1)

tab1 = tabs.add("Python")

tab2 = tabs.add("Arduino")

  #pytabs     
pytabs = ctk.CTkTabview(tab1,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
pytabs.place(relx=0, rely=0, relwidth=1, relheight=1)

pytab1 = pytabs.add("Name")
pytab2 = pytabs.add("Modules")
pytab3 = pytabs.add("Code")

#artabs
artabs = ctk.CTkTabview(tab2,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
artabs.place(relx=0, rely=0, relwidth=1, relheight=1)

artab1 = artabs.add("Name")
artab2 = artabs.add("Modules")
artab3 = artabs.add("Code")
#name entry tabs
pylabel = ctk.CTkLabel(pytab1, text="Python Blinder")
pylabel.pack()

arlabel = ctk.CTkLabel(artab1, text="Arduino Blinder")
arlabel.pack()

pyentry = ctk.CTkEntry(pytab1, placeholder_text="Enter Name", width=250, height=40,corner_radius=13,fg_color="white",text_color="black",border_color="white",border_width=1)
pyentry.pack()

arentry = ctk.CTkEntry(artab1, placeholder_text="Enter Name", width=250, height=40,corner_radius=13,fg_color="white",text_color="black",border_color="white",border_width=1)
arentry.pack()
#custom and prebuid module entry tabs
pymtab = ctk.CTkTabview(pytab2,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
pymtab.place(relx=0, rely=0, relwidth=1, relheight=1)
pymtab1 = pymtab.add("Python Modules Prebuilt")
pymtab2 = pymtab.add("Python Modules Custom")


armtab = ctk.CTkTabview(artab2,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
armtab.place(relx=0, rely=0, relwidth=1, relheight=1)
armtab1 = armtab.add("Arduino Modules Prebuilt")
armtab2 = armtab.add("Arduino Modules Custom")

#code tabs



pycodetabs = ctk.CTkTabview(pytab3,fg_color="black",border_color="white",border_width=2,segmented_button_fg_color="black",segmented_button_selected_color="#38B6FF",segmented_button_unselected_color="black")
pycodetabs.pack() # makes the tabview

pygradiocode = pycodetabs.add("Gradio Code")
pyTkintercode = pycodetabs.add("Tkinter Code")

pyGcodesframe = ctk.CTkScrollableFrame(pygradiocode,fg_color="black",border_color="white",border_width=2)
pyGcodesframe.pack()

pyTcodesframe = ctk.CTkScrollableFrame(pyTkintercode,fg_color="black",border_color="white",border_width=2)
pyTcodesframe.pack()
#code add buttons for Python and Arduino

#gradio code add buttons for Python and Arduino
pyTtT = ctk.CTkButton(pyGcodesframe, text="Text to Text", command=TtT)
pyTtT.pack(pady=10)

pyTtI = ctk.CTkButton(pyGcodesframe, text="Text to Image", command=TtI)
pyTtI.pack(pady=10)

pyItT = ctk.CTkButton(pyGcodesframe, text="Image to Text", command=ItT)
pyItT.pack(pady=10)

pyItI = ctk.CTkButton(pyGcodesframe, text="Image to Image", command=ItI)
pyItI.pack(pady=10)
#tkinter code add buttons for Python and Arduino)

pytklogin = ctk.CTkButton(pyTcodesframe, text="CTK Log In", command = CTKLogin)
pytklogin.pack(pady=10)

pytktabs = ctk.CTkButton(pyTcodesframe, text="CTK Tabs", command = CTKTabs)
pytktabs.pack(pady=10)





#module entry tabs
pymodscroll = ctk.CTkScrollableFrame(pymtab1,fg_color="black",border_color="white",border_width=2)
pymodscroll.pack()

artmodscroll = ctk.CTkScrollableFrame(armtab1,fg_color="black",border_color="white",border_width=2)
artmodscroll.pack()
#module entry tabs with custom modules
pycmentry = ctk.CTkEntry(pymtab2, placeholder_text="Enter Module Name", width=250, height=40,corner_radius=13,fg_color="white",text_color="black",border_color="white",border_width=1)
pycmentry.pack()
pycmsender = ctk.CTkButton(pymtab2, text="Add Module", command=pycmodules)
pycmsender.pack(pady=10)

arcmentry = ctk.CTkEntry(armtab2, placeholder_text="Enter Module Name", width=250, height=40,corner_radius=13,fg_color="white",text_color="black",border_color="white",border_width=1)
arcmentry.pack()
arcmsender = ctk.CTkButton(armtab2, text="Add Module",command=arcomodules)
arcmsender.pack(pady=10)
#code tabs


arlabel = ctk.CTkLabel(artab3, text="Arduino Code Setup")
arlabel.pack()

arlabel2 = ctk.CTkLabel(artab3, text="Comming Soon")
arlabel2.pack()

#module buttons for Arduino and Python

pyGRADIO = ctk.CTkButton(pymodscroll, text="gradio", command=gradio,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pyGRADIO.pack(pady=10)

arM5STACK = ctk.CTkButton(artmodscroll, text="m5stack", command=m5stack,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
arM5STACK.pack(pady=10)

pyTKINTER = ctk.CTkButton(pymodscroll, text="TKINTER", command=tkinter,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pyTKINTER.pack(pady=10)


arESPMDNS = ctk.CTkButton(artmodscroll, text="ESPMDNS", command=espmdns,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
arESPMDNS.pack(pady=10)

pyOPENAI = ctk.CTkButton(pymodscroll, text="openai", command=openai,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pyOPENAI.pack(pady=10)

arwebserver = ctk.CTkButton(artmodscroll, text="webserver", command=webserver,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
arwebserver.pack(pady=10)

pypyinstaller = ctk.CTkButton(pymodscroll, text="pyinstaller", command=pyinstaller,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pypyinstaller.pack(pady=10)

pycustmtkiner = ctk.CTkButton(pymodscroll, text="customtkinter", command=customtkinter,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pycustmtkiner.pack(pady=10)

pyrequests = ctk.CTkButton(pymodscroll, text="requests", command=requests,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pyrequests.pack(pady=10)

pybeautifulsoup4 = ctk.CTkButton(pymodscroll, text="beautifulsoup4", command=beautifulsoup4,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pybeautifulsoup4.pack(pady=10)

pynumpy = ctk.CTkButton(pymodscroll, text="numpy", command=numpy,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pynumpy.pack(pady=10)

pypandas = ctk.CTkButton(pymodscroll, text="pandas", command=pandas,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pypandas.pack(pady=10)

pymatplotlib = ctk.CTkButton(pymodscroll, text="matplotlib", command=matplotlib,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pymatplotlib.pack(pady=10)

pyscipy = ctk.CTkButton(pymodscroll, text="scipy", command=scipy,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pyscipy.pack(pady=10)
pysqlalchemy = ctk.CTkButton(pymodscroll, text="sqlalchemy", command=sqlalchemy,corner_radius=9,fg_color="#FF3131",border_color="white",border_width=3)
pysqlalchemy.pack(pady=10)





#Blind it button
button = ctk.CTkButton(tab1, text="Blind it!", command=pyblindit,fg_color="#FF3131",corner_radius=9,border_color="white",border_width=3)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

button = ctk.CTkButton(tab2, text="Blind it!", command=arblindit,fg_color="#FF3131",corner_radius=9,border_color="white",border_width=3)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)








#runbutton
app.mainloop()

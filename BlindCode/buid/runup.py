import os
import customtkinter as ctk
import tkinter as tk  
from buid.main import *

def pycmodules():
    pyoutputs = r'C:\Users\kryst\Documents\BlindCode Outputs' + pycmentry.get()
    os.chdir(pyoutputs)
    addons = open(requirements.txt, 'w')
    addons.write('pycmodules /n')
    addons.close

def arcomodules(name):
    aroutputs = r'C:\Users\kryst\Documents\BlindCode Outputs' + arcmentry.get()
    os.chdir(aroutputs)
    addons = open(requirements.txt, 'w')
    addons.write('arcomodules /n')
    addons.close
    
def gradio():
    os.chdir(r'C:\Users\kryst\Documents\BlindCode Outputs')
    addons = open(requirements.txt, 'w')
    addons.write('gradio /n')
    addons.closeq

def tkinter():
    os.chdir(r'C:\Users\kryst\Documents\BlindCode Outputs')
    addons = open(requirements.txt, 'w')
    addons.write('tkinter /n')
    addons.close

def customtkinter():
    os.chdir(r'C:\Users\kryst\Documents\BlindCode Outputs')
    addons = open(requirements.txt, 'w')
    addons.write('customtkinter /n')
    addons.close

def pyinstaller():
    os.chdir(r'C:\Users\kryst\Documents\BlindCode Outputs')
    addons = open(requirements.txt, 'w')
    addons.write('pyinstaller /n')
    addons.close

def openai():
    os.chdir(r'C:\Users\kryst\Documents\BlindCode Outputs')
    addons = open(requirements.txt, 'w')
    addons.write('openai /n')
    addons.close
    
    def m5stack():
        pass






        
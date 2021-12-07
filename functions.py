from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilenames, askopenfiles
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#place an image on the grid
def display_img(url, root, row, column):
    img = Image.open(url)
    #img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(root, image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=1, sticky=NE)

#place textbox on the page
def display_textbox(content, ro, col, root):
    text_box = Text(root, height=1, width= 20, font= (("shanti", 10)))
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=col, row=ro, sticky=E)

def display_Label(content, ro, col, root, stick):
    text_box = Label(root, text = content)
    text_box.grid(column=col, row=ro, sticky=stick)

def display_icon(url, root, row, column, stick):
    icon = Image.open(url)
    #resize image
    icon = icon.resize((25, 25))
    icon = ImageTk.PhotoImage(icon)
    icon_label = Button(root, image=icon, width=25, height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=stick)

def display_CheckButton(root, row, col, text, variable):
    CheckBtn = Checkbutton(root, text=text, variable=variable, font=(("shanti", 10)), bg="white", highlightcolor="red", padx=20, pady=10)
    CheckBtn.deselect()
    CheckBtn.grid(column=col, row=row, sticky=W)

def display_RadioButton(root, row, col, text, variable, value):
    RadioBtn = Radiobutton(root, text=text, font=(("shanti", 10)), bg="white",  padx=20, pady=10, variable=variable,  value=value)
    RadioBtn.grid(row=row, column=col, sticky=W)
    RadioBtn.deselect()

def value_changed():
    print('Klappt')


def ReadDataFiles(files):
    DataFiles = {}
    for fileDat in files:

        if fileDat.endswith('.dat') or fileDat.endswith('.csv'):
            key0 = fileDat.split('.')[0]    # key0 = 'Testnummer'
            if key0 not in DataFiles:
                DataFiles[key0] = {}
            #T_head = pd.read_csv(os.path.join(WorkDir,fileDat), sep=';', decimal=',')
            #T_num = pd.read_csv(os.path.join(WorkDir,fileDat), sep=';', decimal=',', header=3)

            #S_head = T_head.to_numpy()
            #S = T_num.to_numpy()

            #DataFiles[key0] = {}
            #DataFiles[key0]['Kraft'] = (S[:,2]*1000).astype(np.float)
            #DataFiles[key0]['Dehnung'] = S[:,1].astype(np.float)
            #DataFiles[key0]['Fläche'] = S[0,6].astype(np.float)
            #DataFiles[key0]['Spannung'] = DataFiles[key0]['Kraft']/DataFiles[key0]['Fläche']
    return DataFiles   

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
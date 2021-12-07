import tkinter as tk
from tkinter import Checkbutton, StringVar, font, IntVar
from tkinter.constants import BOTH, COMMAND, DISABLED, E, FALSE, TRUE, W, YES
from tkinter.ttk import LabelFrame
#from typing_extensions import IntVar
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)



def open_file(root):
    DataFiles={}
    filenames = askopenfilenames(parent=root, title="Choose a file", filetype=[("CSV file", "*.csv")])
    print(filenames)
    try:
        for i in range(len(filenames)):
            key0 = filenames[i].split('/')[-1].split('.')[0]
            if key0 not in DataFiles:
                DataFiles[key0] = {}
            T = pd.read_csv(filenames[i], encoding= 'unicode_escape', sep=';', decimal='.', header=2)
            S = T.to_numpy()
            DataFiles[key0]['Weg'] = S[:,0]
            DataFiles[key0]['Dehnung'] = S[:,1]
            DataFiles[key0]['Kraft'] = S[:,2]

            #fig = plt.subplots(figsize=(5,4), dpi=100)
            fig = plt.figure(figsize=(5, 4), dpi=100)
            fig.add_subplot(111).plot(DataFiles[key0]['Dehnung'], DataFiles[key0]['Kraft'])

            canvas = FigureCanvasTkAgg(fig, master=main_content)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2, row=1)
            
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {filenames}")

root = tk.Tk()

root.geometry('+%d+%d'%(100,50))

# Frames

main_content = tk.Frame(root, width=1600, height=700, bg="white")
main_content.grid(columnspan=3, rowspan=3, row=1)

Befehle = tk.Frame(main_content, width=375, height=520, bg="white")
Befehle.grid(columnspan=1, rowspan=1, column=2, row=1, padx=20, pady=20)

Spezifische_Eingaben = tk.LabelFrame(main_content, width=375, height=520, bg="#F2F2F2", text="Spezifische Eingaben", padx=10, pady=50)
Spezifische_Eingaben.grid(columnspan=1, rowspan=1, row=1, padx=20, pady=20, sticky=W)

CalculatedValues = tk.LabelFrame(main_content,  width=375, height=520, bg="white", text="Zu berechnende Werte:", padx=10, pady=50)
CalculatedValues.grid(columnspan=1, rowspan=1, row=2, padx=20, pady=20, sticky="sw")

Testtype = tk.LabelFrame(main_content,  width=375, height=520, bg="white", text="Art des Tests:", padx=10, pady=50)
Testtype.grid(columnspan=1, rowspan=1, row=2, column=1, padx=20, pady=20)

Auswertung = tk.LabelFrame(main_content,  width=375, height=520, bg="white", text="Auswertung:", padx=10, pady=50)
Auswertung.grid(columnspan=1, rowspan=1, row=2, column=2, padx=20, pady=20, sticky=W)

#Logo
display_img('LiA_Eng_logo.png', main_content,  0, 2)
# Textfeld
what_slide = tk.Label(main_content, text="Plot 1 of 10", font=("shanti", 10), bg="#1C6789", fg="white", width=40)
what_slide.grid(row=0, column=1)

# Pfeile
display_icon('Arrow_ri.png', main_content, 0, 1, E)
display_icon('Arrow_le.png', main_content, 0, 1, W)

## Befehle
#instructions
instructions = tk.Label(Befehle, text="Select raw data", font = "Raleway", bg="white")
instructions.grid(columnspan=2, column=2, row=1, sticky='n')

instruction_2 = tk.Label(Befehle, text="Auswertung exportieren", font = "Raleway", bg="white")
instruction_2.grid(columnspan=1, column=2, row=5, sticky='s')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(Befehle, textvariable=browse_text, command=lambda:open_file(root), font="Raleway", bg="#1C6789", fg="white", height=1, width=30)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2, pady=20, sticky=E)

#Export einzeln button
export_einzeln_text = tk.StringVar()
export_einzeln__btn = tk.Button(Befehle, textvariable=export_einzeln_text, font="Raleway", bg="#1C6789", fg="white", height=1, width=30)
export_einzeln_text.set("Export einzeln")
export_einzeln__btn.grid(columnspan=2, column=1, row=6, pady=20, sticky=E)

#Export alle button
export_alle_text = tk.StringVar()
export_alle_btn = tk.Button(Befehle, textvariable=export_alle_text, font="Raleway", bg="#1C6789", fg="white", height=1, width=30)
export_alle_text.set("Export alle")
export_alle_btn.grid(columnspan=2, column=1, row=7, sticky=E)

## Spezifische Eingaben
# Label "Probenbreite"
Probendurchmesser = display_Label('Probendurchmesser', 0, 0, Spezifische_Eingaben, W)
Probendurchmesser_Einheit = display_Label('[mm]', 0, 2, Spezifische_Eingaben, E)
Probenbreite = display_Label('Probenbreite', 1, 0, Spezifische_Eingaben, W)
Breite_Einheit = display_Label('[mm]', 1, 2, Spezifische_Eingaben, E)
Probendicke = display_Label('Probendicke', 2, 0, Spezifische_Eingaben, W)
Dicke_Einheit = display_Label('[mm]', 2, 2, Spezifische_Eingaben, E)
Untere_elastische_Grenze = display_Label('Untere elastische Grenze', 3, 0, Spezifische_Eingaben, W)
UnElGr_Einheit = display_Label('[%]', 3, 2, Spezifische_Eingaben, E)
Obere_elastische_Grenze = display_Label('Obere elastische Grenze', 4, 0, Spezifische_Eingaben, W)
ObElGr_Einheit = display_Label('[%]', 4, 2, Spezifische_Eingaben, E)
Bruch = display_Label('Bruch', 5, 0, Spezifische_Eingaben, W)
Bruch_Einheit = display_Label('[%]', 5, 2, Spezifische_Eingaben, E)
Probenname = display_Label('Probenname', 6, 0, Spezifische_Eingaben, W)
Pruefer = display_Label('Prüfer', 7, 0, Spezifische_Eingaben, W)
Frequenz = display_Label('Abtastfrequenz', 8, 0, Spezifische_Eingaben, W)
Pruefdatum = display_Label('Prüfdatum', 9, 0, Spezifische_Eingaben, W)
Pruefzeit = display_Label('Prüfzeit', 10, 0, Spezifische_Eingaben, W)

display_textbox("Probenname", 6, 1, Spezifische_Eingaben)
display_textbox("Prüfer", 7, 1, Spezifische_Eingaben)
display_textbox("Abtastfrequenz", 8, 1, Spezifische_Eingaben)
display_textbox("Prüfdatum", 9, 1, Spezifische_Eingaben)
display_textbox("Prüfzeit", 10, 1, Spezifische_Eingaben)

#Spinboxes in "Spezifische Eingaben"

sp_Durchmesser = tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Durchmesser.grid(column=1, row=0, sticky=E)

sp_Breite =tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Breite.grid(column=1, row=1, sticky=E)

sp_Dicke = tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Dicke.grid(column=1, row=2, sticky=E)

sp_Untere_elastische_Grenze = tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Untere_elastische_Grenze.grid(column=1, row=3, sticky=E)

sp_Obere_elastische_Grenze =tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Obere_elastische_Grenze.grid(column=1, row=4, sticky=E)

sp_Bruch = tk.Spinbox(Spezifische_Eingaben, from_=0.0, to=100.0, increment=0.01, width=10, command=value_changed)
sp_Bruch.grid(column=1, row=5, sticky=E)

def enableSpinbox():
    sp_Durchmesser.configure(state=DISABLED)
    sp_Durchmesser.update()
    sp_Breite.configure(state=NORMAL)
    sp_Breite.update()
    sp_Dicke.configure(state=NORMAL)
    sp_Dicke.update()
def disableSpinbox():
    sp_Durchmesser.configure(state=NORMAL)
    sp_Durchmesser.update()
    sp_Breite.configure(state=DISABLED)
    sp_Breite.update()
    sp_Dicke.configure(state=DISABLED)
    sp_Dicke.update()

## Zu berechnende Werte
# create Checkbuttons
mE_ChBtn_State = IntVar()
R_m_ChBtn_State = IntVar()
A_g_State = IntVar()
A_t_ChBtn_State = IntVar()
Rp02_ChBtn_State = IntVar()
ReH_ChBtn_State = IntVar()
Agt_ChBtn_State = IntVar()
A_L_ChBtn_State = IntVar()
ReL_ChBtn_State = IntVar()

mE_ChBtn = display_CheckButton(CalculatedValues, 1, 1, "mE", mE_ChBtn_State)
R_m_ChBtn = display_CheckButton(CalculatedValues, 1, 2, "R_m", R_m_ChBtn_State)
A_g = display_CheckButton(CalculatedValues, 1, 3, "A_g", A_g_State)
A_t_ChBtn = display_CheckButton(CalculatedValues, 1, 4, "A_t", A_t_ChBtn_State)
Rp02_ChBtn = display_CheckButton(CalculatedValues, 2, 1, "Rp02", Rp02_ChBtn_State)
ReH_ChBtn = display_CheckButton(CalculatedValues, 2, 2, "ReH", ReH_ChBtn_State)
Agt_ChBtn = display_CheckButton(CalculatedValues, 2, 3, "Agt", Agt_ChBtn_State)
A_L_ChBtn = display_CheckButton(CalculatedValues, 2, 4, "A_L", A_L_ChBtn_State)
ReL_ChBtn = display_CheckButton(CalculatedValues, 3, 2, "ReL", ReL_ChBtn_State)


## Art des Tests:

# Dropdown Menu
OptionList = [
    "DIN EN ISO haste nicht gesehn",
    "DIN EN ISO dings bums",
    "DIN EN ISO 0815"
]

variable = tk.StringVar(Testtype)
variable.set(OptionList[0])
opt = tk.OptionMenu(Testtype, variable, *OptionList)
opt.config(width=40, font=('shanti', 10))
opt.grid(column=1, columnspan=3, row=1, padx= 20, pady=10)



# Radiobuttons

Probengeometrie = IntVar()

Flachprobe_RaBtn = tk.Radiobutton(Testtype, text="Flache Probe", font=(("shanti", 10)), bg="white",  
                    padx=20, pady=10, variable=Probengeometrie, value=True, command=enableSpinbox)
Flachprobe_RaBtn.grid(row=2, column=3, sticky=W)

Rundprobe_RaBtn = tk.Radiobutton(Testtype, text="Runde Probe", font=(("shanti", 10)), bg="white",  
                    padx=20, pady=10, variable=Probengeometrie, value=False, command=disableSpinbox)
Rundprobe_RaBtn.grid(row=3, column=3, sticky=W)

# Auswertung

DisInOverview_State = IntVar()
DisInStatistics_State = IntVar()
SpecimenNotValid_State = IntVar()

DisInOverview = display_CheckButton(Auswertung, 1, 1, "In Übersicht abbilden", DisInOverview_State)
DisInStatistics = display_CheckButton(Auswertung, 2, 1, "Zu Statistik hinzufügen", DisInStatistics_State)
SpecimenNotValid = display_CheckButton(Auswertung, 3, 1, "Probe ungültig", SpecimenNotValid_State)



root.mainloop()
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Circle Area")
    frm_main.pack(padx=100, pady=40, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)
    
    root.mainloop()


def populate_main_window(frm_main):
    lbl_rad = Label(frm_main, text = "Circle Radius: ")
    ent_rad = IntEntry(frm_main, width = 4)

    lbl_area = Label(frm_main, text = "Area: ")

    lbl_answ = Label(frm_main, width=8)

    btn_calc = Button(frm_main, text="Calculate")
    btn_clear = Button(frm_main, text="Clear")

    lbl_rad.grid(      row=0, column=0, padx=3, pady=3)
    ent_rad.grid(      row=0, column=1, padx=3, pady=3)

    lbl_area.grid(       row=1, column=0, padx=(30,3), pady=5)
    lbl_answ.grid(      row=1, column=1, columnspan=2, padx=3, pady=5)

    btn_calc.grid(row=2, column=0, padx=3, pady=(30,3), columnspan=4, sticky="w")
    btn_clear.grid(row=2, column=1, padx=3, pady=(30,3), columnspan=4, sticky="e")


    def calculate():
        try:
            radius = ent_rad.get()
            area = math.pi * radius ** 2

            lbl_answ.config(text=f"{area:.2f}")
        
        except ValueError:
            lbl_answ.config(text="")

    def clear():
        btn_clear.focus()
        ent_rad.clear()
        lbl_answ.config(text="")
        ent_rad.focus()
    

    btn_calc.config(command=calculate)
    btn_clear.config(command=clear)

    ent_rad.focus()


if __name__ == "__main__":
    main()
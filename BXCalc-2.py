import tkinter
from tkinter import *


class BXCalc:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_text()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=0)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='white',
            text='Creative Displays BX Calculator',
            fg='black',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_text(self):
        text = Text(root)
        text.insert(INSERT, 'Testing')
        text.insert(END, 'End Test')
        text.pack(padx=10, pady=10)


    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.calc_button = tkinter.Button(
            buttons_frame,
            text='Calculate'
        )
        self.quit_button = tkinter.Button(
            buttons_frame,
            text='Quit'
        )

        self.calc_button.grid(row=0, column=0, sticky='ew')
        self.quit_button.grid(row=0, column=1, sticky='ew')

if __name__ == '__main__':
    root = tkinter.Tk()
    Text(root)
    BXCalc(root)
    root.mainloop()
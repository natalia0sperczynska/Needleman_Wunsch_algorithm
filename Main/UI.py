import tkinter
from tkinter import*
from tkinter.ttk import Label
from tkinter.ttk import *

class App(tkinter.Tk):
    """
    Main application class for creating and managing the tkinter GUI.
    """
    def __init__(self):

        """
        Function initializes the application window, layout and tabs.
        """
        super().__init__()
        self.geometry("400x400")
        icon = tkinter.PhotoImage(file="dna.png")
        self.iconphoto(True, icon)
        self.title("Needleman-Wunsch Algorithm")
        self.grid_columnconfigure((0, 1), weight=1)

        self.tabControl = tkinter.ttk.Notebook(self)
        self.tabControl.pack(expand=True, fill="both")

        self.choice_frame = MyFrame(self,tabControl=self.tabControl)
        self.choice_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.tabControl.add(self.choice_frame, text="Main Frame")

class MyFrame(tkinter.Frame):
    def __init__(self, parent, tabControl):
        super().__init__(parent)
        self.parent = parent
        self.generatedTabs = 0
        self.tabControl = tabControl

        self.configure(bg="#ad86e3")

        self.button_dna =tkinter.Button(self, text="Enter two DNA sequence", command=self.go_to_DNA_input,  fg="black", bg ="#5ba679")
        self.button_dna.pack(padx=10, pady=10)

        self.button_rna = tkinter.Button(self, text="Enter two RNA sequence", command=self.go_to_DNA_input,
                         fg="black", bg="#5ba679")
        self.button_rna.pack(padx=10, pady=10)

        self.button_protein =tkinter.Button(self, text="Enter two protein sequence", command=self.go_to_DNA_input,
                           fg="black", bg="#5ba679")
        self.button_protein.pack(padx=10, pady=10)

        self.button_fasta =tkinter.Button(self, text="Enter fasta files", command=self.go_to_DNA_input,
                               fg="black", bg="#5ba679")
        self.button_fasta.pack(padx=10, pady=10)

    def go_to_DNA_input(self):
        self.generatedTabs += 1
        user_input_frame = tkinter.Frame(self.tabControl)
        label1=tkinter.Label(user_input_frame, text="Enter first DNA sequence")
        label1.pack()
        first_seq = tkinter.Entry(user_input_frame)
        first_seq.pack(pady=10, padx=10)
        label2 = tkinter.Label(user_input_frame, text="Enter second DNA sequence")
        label2.pack()
        second_seq=tkinter.Entry(user_input_frame)
        second_seq.pack(padx=10, pady=10)
        user_input_frame.pack(expand=True, fill="both")
        self.tabControl.add(user_input_frame, text=f"Data input{self.generatedTabs}")

if __name__ == '__main__':
    app=App()
    app.mainloop()

import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import *
from Converters import *
from Alghorithm import *
from Sequences import *
from pandastable import Table, TableModel


class App(tkinter.Tk):
    """
    Main application class for creating and managing the tkinter GUI.
    """
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        icon = tkinter.PhotoImage(file="dna.png")
        self.iconphoto(True, icon)
        self.title("Needleman-Wunsch Algorithm")
        self.container = tkinter.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.table_container = tkinter.Frame(self)
        self.table_container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, DNAInputPage, RNAInputPage,ProteinInputPage,FastaInputPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class HomePage(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent

        self.configure(bg="#ad86e3")

        self.button_dna =tkinter.Button(self, text="Enter two DNA sequence", command=lambda:controller.show_frame(DNAInputPage),  fg="black", bg ="#5ba679")
        self.button_dna.pack(padx=10, pady=10)

        self.button_rna = tkinter.Button(self, text="Enter two RNA sequence", command=lambda:controller.show_frame(RNAInputPage),
                         fg="black", bg="#5ba679")
        self.button_rna.pack(padx=10, pady=10)

        self.button_protein =tkinter.Button(self, text="Enter two protein sequence", command=lambda:controller.show_frame(ProteinInputPage),
                           fg="black", bg="#5ba679")
        self.button_protein.pack(padx=10, pady=10)

        self.button_fasta =tkinter.Button(self, text="Enter fasta files", command=lambda:controller.show_frame(FastaInputPage),
                               fg="black", bg="#5ba679")
        self.button_fasta.pack(padx=10, pady=10)

class InputBaseFrame(tkinter.Frame):
    def __init__(self, parent, controller,convert_fun):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.convert_fun = convert_fun
        self.configure(bg="#ad86e3")
        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.pack(padx=10, pady=10)
        self.enter1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter1.pack(padx=10, pady=10)

        self.label2=tkinter.Label(self, text="Enter second sequence")
        self.label2.pack(padx=10, pady=10)
        self.enter2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter2.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Generate", command=self.get_data, fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)


    def get_data(self):
        input_seq1 = str(self.enter1.get())
        input_seq2 = str(self.enter2.get())
        seq1_labels="-"+input_seq1.upper()
        try:
            seq1 = self.convert_fun(input_seq1)
            seq2 = self.convert_fun(input_seq2)
            df = algorithm_implementation(seq1, seq2, gap=-1, mismatch=0, match=1)
            print("DF rows:", df.shape[0])
            print("Sequence length:", len(seq1.seq()) + 1)
            print(df)
            print(traceback(df, gap=-1, mismatch=0, match=1))
            print(int(get_score(df)))
            #table osobna klasa
            #layout landy
            #kolory
            df.insert(0,column="",value=[x for x in seq1_labels])
            self.table =Table(self.parent.master.table_container, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            self.table.show()
        except Exception as e:
                messagebox.showerror("Error", str(e))
                return


class DNAInputPage(InputBaseFrame):
    def __init__(self, parent, controller, convert_fun=convert_user_input_DNA):
        super().__init__(parent, controller,convert_fun)

class RNAInputPage(InputBaseFrame):
    def __init__(self, parent, controller, convert_fun=convert_user_input_RNA):
        super().__init__(parent, controller, convert_fun)

class ProteinInputPage(InputBaseFrame):
    def __init__(self, parent, controller,convert_fun=convert_user_input_Protein):
        super().__init__(parent, controller, convert_fun)

class FastaInputPage(InputBaseFrame):
    def __init__(self, parent, controller,convert_fun=convert_user_input_Protein):
        super().__init__(parent, controller, convert_fun)
if __name__ == '__main__':
    app=App()
    app.mainloop()

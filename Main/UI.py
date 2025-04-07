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

class DNAInputPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#ad86e3")

        self.label1=tkinter.Label(self, text="Enter first DNA sequence")
        self.label1.pack(padx=10, pady=10)
        self.enter_dna1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_dna1.pack(padx=10, pady=10)

        self.label2=tkinter.Label(self, text="Enter second DNA sequence")
        self.label2.pack(padx=10, pady=10)
        self.enter_dna2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_dna2.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Generate", command=self.get_data, fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)


    def get_data(self):
        input_se1 = str(self.enter_dna1.get())
        input_seq2 = str(self.enter_dna2.get())
        try:
            seq1 = convert_user_input_DNA(input_se1)
            seq2 = convert_user_input_DNA(input_seq2)
            df = algorithm_implementation(seq1, seq2, gap=-1, mismatch=0, match=1)
            # print(df)
            # print(traceback(df, gap=-1, mismatch=0, match=1))
            # print(int(get_score(df)))
            #table osobna klasa
            #layout landy
            #kolory
            df.insert(0,column="",value=[x for x in "-" + seq1.seq()])
            self.table =Table(self.parent.master.table_container, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            self.table.show()
        except Exception as e:
                messagebox.showerror("Error", str(e))
                return


class RNAInputPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#ad86e3")

        self.label1=tkinter.Label(self, text="Enter first RNA sequence")
        self.label1.pack(padx=10, pady=10)
        self.enter_rna1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_rna1.pack(padx=10, pady=10)

        self.label2=tkinter.Label(self, text="Enter second RNA sequence")
        self.label2.pack(padx=10, pady=10)
        self.enter_rna2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_rna2.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Generate", command=self.get_data, fg="black", bg="#5ba679")
        self.button_back.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

    def get_data(self):
        input_se1=str(self.enter_rna1.get())
        input_seq2=str(self.enter_rna2.get())
        seq1=convert_user_input_DNA(input_se1)
        seq2=convert_user_input_DNA(input_seq2)

        try:
            df = algorithm_implementation(seq1, seq2, gap=-1, mismatch=0, match=1)
            df.insert(0,column="",value=[x for x in "-" + seq1.seq()])
            self.table =Table(self.parent.master.table_container, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            self.table.show()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

class ProteinInputPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#ad86e3")

        self.label1=tkinter.Label(self, text="Enter first protein sequence")
        self.label1.pack(padx=10, pady=10)
        self.enter_protein1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_protein1.pack(padx=10, pady=10)

        self.label2=tkinter.Label(self, text="Enter second protein sequence")
        self.label2.pack(padx=10, pady=10)
        self.enter_protein2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter_protein2.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Generate", command=self.get_data, fg="black", bg="#5ba679")
        self.button_back.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

    def get_data(self):
        input_se1=str(self.enter_protein1.get())
        input_seq2=str(self.enter_protein2.get())
        seq1=convert_user_input_DNA(input_se1)
        seq2=convert_user_input_DNA(input_seq2)
        try:
            df = algorithm_implementation(seq1, seq2, gap=-1, mismatch=0, match=1)
            df.insert(0,column="",value=[x for x in "-" + seq1.seq()])
            self.table =Table(self.parent.master.table_container, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            self.table.show()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

class FastaInputPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#ad86e3")

        self.label1=tkinter.Label(self, text="Enter first fasta file")
        self.label1.pack(padx=10, pady=10)

        self.label2=tkinter.Label(self, text="Enter second fasta file")
        self.label2.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

if __name__ == '__main__':
    app=App()
    app.mainloop()

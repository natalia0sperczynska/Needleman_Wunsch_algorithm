import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Converters import *
from Alghorithm import *
from Plot import generate_graph
import pandas as pd
from pandas import *
#ukryc indexy

from pandastable import Table, TableModel
class App(tkinter.Tk):
    """
    Main application class for creating and managing the tkinter GUI.
    """
    def __init__(self):
        super().__init__()
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

        self.update_idletasks()
        self.minsize(400,400)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        self.update_idletasks()
        self.minsize(400,400)

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
        self.df : pd.DataFrame = None
        self.parent = parent
        self.controller = controller
        self.convert_fun = convert_fun
        self.file1=None
        self.file2=None
        self.seq1_str=""
        self.seq2_str=""
        self.configure(bg="#ad86e3")
        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.pack(padx=10, pady=10)
        self.enter1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter1.pack(padx=10, pady=10)
        self.enter1.bind('<FocusOut>', lambda event: update_entry(event, "seq1_str", self))

        self.label2=tkinter.Label(self, text="Enter second sequence")
        self.label2.pack(padx=10, pady=10)
        self.enter2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter2.pack(padx=10, pady=10)
        self.enter2.bind('<FocusOut>', lambda event: update_entry(event, "seq2_str", self))

        # self.button_save = tkinter.Button(self, text="Save", fg="black", bg="#5ba679")
        # self.button_save.pack(padx=10, pady=10)
        self.label3 = tkinter.Label(self, text="Match")
        self.label3.pack(padx=10, pady=10)
        self.enterMatch = tkinter.Entry(self, bg="#ad86e3")
        self.enterMatch.pack(padx=10, pady=10)

        self.label4 = tkinter.Label(self, text="Gap")
        self.label4.pack(padx=10, pady=10)
        self.enterGap = tkinter.Entry(self, bg="#ad86e3")
        self.enterGap.pack(padx=10, pady=10)

        self.label5 = tkinter.Label(self, text="Mismatch")
        self.label5.pack(padx=10, pady=10)
        self.enterMismatch = tkinter.Entry(self, bg="#ad86e3")
        self.enterMismatch.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Generate", command=lambda:get_data(self.seq1_str,self.seq2_str,self.convert_fun, self.parent,self), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

        self.button_graph = tkinter.Button(self, text="Show graph",
                                           command=lambda:show_graph_window(self.df,self.parent), fg="black", bg="#5ba679")
        self.button_graph.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda:controller.show_frame(HomePage), fg="black", bg ="#5ba679")
        self.button_back.pack(padx=10, pady=10)

class FastaInputPage(tkinter.Frame):
    def __init__(self, parent, controller, convert_fun=convert_user_input_Protein):
        super().__init__(parent)
        self.df: pd.DataFrame = None
        self.parent = parent
        self.controller = controller
        self.convert_fun = convert_fun
        self.file1 = None
        self.file2 = None
        self.seq1_str = ""
        self.seq2_str = ""
        self.configure(bg="#ad86e3")
        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.pack(padx=10, pady=10)

        self.button1 = tkinter.Button(self, text="Add file", command=lambda: open_file(self.file1,"seq1_str",self))
        self.button1.pack(padx=10, pady=10)

        self.label2 = tkinter.Label(self, text="Enter second sequence")
        self.label2.pack(padx=10, pady=10)
        self.button2 = tkinter.Button(self, text="Add file", command=lambda: open_file(self.file2,"seq2_str",self))
        self.button2.pack(padx=10, pady=10)


        self.button_generate = tkinter.Button(self, text="Generate", command=lambda:get_data(self.seq1_str, self.seq2_str, self.convert_fun, self.parent, self), fg="black", bg="#5ba679")
        self.button_generate.pack(padx=10, pady=10)

        self.button_graph = tkinter.Button(self, text="Show graph",
                                           command=lambda:show_graph_window(self.df,self.parent), fg="black", bg="#5ba679")
        self.button_graph.pack(padx=10, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda: controller.show_frame(HomePage),
                                              fg="black", bg="#5ba679")
        self.button_back.pack(padx=10, pady=10)


class DNAInputPage(InputBaseFrame):
    def __init__(self, parent, controller, convert_fun=convert_user_input_DNA):
        super().__init__(parent, controller,convert_fun)

class RNAInputPage(InputBaseFrame):
    def __init__(self, parent, controller, convert_fun=convert_user_input_RNA):
        super().__init__(parent, controller, convert_fun)

class ProteinInputPage(InputBaseFrame):
    def __init__(self, parent, controller,convert_fun=convert_user_input_Protein):
        super().__init__(parent, controller, convert_fun)

def update_entry(event,seq:str,frame):
    if seq=="seq1_str":
        frame.seq1_str = str(frame.enter1.get())
    elif seq=="seq2_str":
        frame.seq2_str = str(frame.enter2.get())


def open_file(file, seq:str,frame):
    path = filedialog.askopenfilename()
    file = open(path,'r')
    identifier = file.readline()
    content = ''.join(file.read().split())
    print(content)
    if seq=='seq1_str':
        frame.seq1_str = content
    elif seq=='seq2_str':
        frame.seq2_str = content
    file.close()

def get_data(seq1_str, seq2_str, convert_fun,parent,frame):
    input_seq1 = seq1_str
    input_seq2 = seq2_str
    seq1_labels="-"+input_seq1.upper()
    try:
        seq1 = convert_fun(input_seq1)
        seq2 = convert_fun(input_seq2)
        if seq1 is None or seq2 is None:
            return
        df = algorithm_implementation(seq1, seq2, gap=-1, mismatch=0, match=1)
        frame.df = df.copy()
        print(df)
        print(traceback(df, gap=-1, mismatch=0, match=1))
        print(int(get_score(df)))
        #layout landy
        #zapis do pliku tekstowego i zapis wykresu
        #zrobic kopie do tableki
        df_copy = df.copy()
        df_copy.insert(0,column="",value=[x for x in seq1_labels])

        table =Table(parent.master.table_container, dataframe=df_copy,
                                showtoolbar=True, showstatusbar=True)
        table.show()

    except Exception as e:
            messagebox.showerror("Error", str(e))
            return

def display_graph(df:DataFrame,root):
    new_window = tkinter.Toplevel(root)
    new_window.minsize(600,500)
    #zapisac do pliku
    new_window.title("Graph")
    #new_window.geometry("700x600")
    fig = generate_graph(df)
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, new_window)
    toolbar.update()
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

def show_graph_window(df:DataFrame,root):
    try:
        display_graph(df,root)
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    app=App()
    app.mainloop()

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

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_dna =tkinter.Button(self, text="Enter two DNA sequence", command=lambda:controller.show_frame(DNAInputPage),  fg="black", bg ="#5ba679")
        self.button_dna.grid(row=1, column=0, pady=10)

        self.button_rna = tkinter.Button(self, text="Enter two RNA sequence", command=lambda:controller.show_frame(RNAInputPage),
                         fg="black", bg="#5ba679")
        self.button_rna.grid(row=2, column=0, pady=10)

        self.button_protein =tkinter.Button(self, text="Enter two protein sequence", command=lambda:controller.show_frame(ProteinInputPage),
                           fg="black", bg="#5ba679")
        self.button_protein.grid(row=3, column=0, pady=10)

        self.button_fasta =tkinter.Button(self, text="Enter fasta files", command=lambda:controller.show_frame(FastaInputPage),
                               fg="black", bg="#5ba679")
        self.button_fasta.grid(row=4, column=0, pady=10)

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
        self.match = 1
        self.mismatch = 0
        self.gap = -1

        self.configure(bg="#ad86e3")
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.enter1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.enter1.bind('<FocusOut>', lambda event: update_entry(event, "seq1_str", self))

        self.label2=tkinter.Label(self, text="Enter second sequence")
        self.label2.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.enter2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter2.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.enter2.bind('<FocusOut>', lambda event: update_entry(event, "seq2_str", self))

        self._create_param_input("Match", "match", 1, 0)
        self._create_param_input("Gap", "gap", 1, 2)
        self._create_param_input("Mismatch", "mismatch", 2, 0)

        self._create_action_button("Generate",
                                   lambda: get_data(self.seq1_str, self.seq2_str, self.convert_fun, self.parent, self),
                                   3, 0)
        self._create_action_button("Show graph", lambda: show_graph_window(self.df, self.parent), 3, 1)
        self._create_action_button("Save as xlsx", lambda: save_to_xlsx(self.df), 3, 2)
        self._create_action_button("Save as text file", lambda: save_as_text_file(self.df), 3, 3)
        self._create_action_button("Back", lambda: controller.show_frame(HomePage), 4, 0, colspan=4)

    def _create_param_input(self, label_text, param_name, row, col):
        label = tkinter.Label(self, text=label_text, bg="#ad86e3")
        label.grid(row=row, column=col, padx=5, pady=5, sticky="e")
        entry = tkinter.Entry(self)
        entry.insert(0, str(getattr(self, param_name)))
        entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky="w")
        entry.bind('<FocusOut>', lambda event: update_parameters(event, param_name, self))
        setattr(self, f"enter{param_name.capitalize()}", entry)

    def _create_action_button(self, text, command, row, col, colspan=1):
        button = tkinter.Button(self, text=text, command=command, fg="black", bg="#5ba679")
        button.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)

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
        self.match=1
        self.mismatch=0
        self.gap=-1

        self.configure(bg="#ad86e3")
        for i in range (10):
            self.grid_rowconfigure(i,weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.button1 = tkinter.Button(self, text="Add file", command=lambda: open_file(self.file1,"seq1_str",self))
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label2 = tkinter.Label(self, text="Enter second sequence")
        self.label2.grid(row=1, column=0,padx=10,pady=10,sticky='e')
        self.button2 = tkinter.Button(self, text="Add file", command=lambda: open_file(self.file2,"seq2_str",self))
        self.button2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label3 = tkinter.Label(self, text="Match", bg="#ad86e3")
        self.label3.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.enterMatch = tkinter.Entry(self, bg="#ad86e3")
        self.enterMatch.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.enterMatch.bind('<FocusOut>', lambda event: update_parameters(event, "match", self))

        self.label4 = tkinter.Label(self, text="Gap", bg="#ad86e3")
        self.label4.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.enterGap = tkinter.Entry(self, bg="#ad86e3")
        self.enterGap.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.enterGap.bind('<FocusOut>', lambda event: update_parameters(event, "gap", self))

        self.label5 = tkinter.Label(self, text="Mismatch", bg="#ad86e3")
        self.label5.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.enterMismatch = tkinter.Entry(self, bg="#ad86e3")
        self.enterMismatch.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.enterMismatch.bind('<FocusOut>', lambda event: update_parameters(event, "mismatch", self))

        self.button_generate = tkinter.Button(self, text="Generate", command=lambda:get_data(self.seq1_str, self.seq2_str, self.convert_fun, self.parent, self), fg="black", bg="#5ba679")
        self.button_generate.grid(row=5,column=0,columnspan=2, pady=10)

        self.button_graph = tkinter.Button(self, text="Show graph",
                                           command=lambda:show_graph_window(self.df,self.parent), fg="black", bg="#5ba679")
        self.button_graph.grid(row=6,column=0,columnspan=2, pady=10)

        self.button_back = tkinter.Button(self, text="Back", command=lambda: controller.show_frame(HomePage),
                                              fg="black", bg="#5ba679")
        self.button_back.grid(row=7,column=0,columnspan=2, pady=10)

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

def update_parameters(event,param:str,frame):
    try:
        if param=="match":
            frame.match=int(frame.enterMatch.get())
        if param=="mismatch":
            frame.mismatch=int(frame.enterMismatch.get())
        if param=="gap":
            frame.gap=int(frame.enterGap.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Value needs to be an integer")
        return

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
        df = algorithm_implementation(seq1, seq2, gap=frame.gap, mismatch=frame.mismatch, match=frame.match)
        #gap=-1, mismatch=0, match=1
        frame.df = df.copy()
        print(df)
        print(traceback(df, gap=-1, mismatch=0, match=1))
        print(int(get_score(df)))
        df_copy = df.copy()
        df_copy.insert(0,column="",value=[x for x in seq1_labels])

        table =Table(parent.master.table_container, dataframe=df_copy,
                                showtoolbar=True, showstatusbar=True)
        table.showIndex=False
        table.show()
        #text result
        l=tkinter.Label(frame,text='Results:')
        l.grid(row=7,column=0, sticky="w",padx=5, pady=5, columnspan=4)

        T =tkinter.Text(frame, bg='white', bd=1, pady=5, padx=5, height=5, width=30)
        T.grid(row=8,column=0, columnspan=4,sticky="nsew",padx=10,pady=5)
        T.insert(tkinter.END, print_results(df,accumulator=traceback(df, gap=frame.gap, mismatch=frame.mismatch, match=frame.match)))

    except Exception as e:
            messagebox.showerror("Error", str(e))
            return
def print_results(df:DataFrame,accumulator)->str:
    match_percentage, gap_percentage= percentage_for_all_matches(accumulator)
    match_percentage*=100
    gap_percentage*=100
    return f"score: {get_score(df)} \nbest alignments: {accumulator} \nmatch percentage: {match_percentage} \ngap percentage: {gap_percentage}"
def save_to_xlsx(df:DataFrame):
    root = Tk()
    try:
        with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
            df.to_excel(file.name)
    except AttributeError:
        messagebox.showerror("Error", str(AttributeError))

    root.destroy()

def save_as_text_file(df:DataFrame):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(df.to_string(index=False))
        except Exception as e:
            messagebox.showerror("Error", str(e))


def display_graph(df:DataFrame,root):
    new_window = tkinter.Toplevel(root)
    new_window.minsize(600,500)
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

import tkinter
from tkinter import*
from tkinter import filedialog, messagebox
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Algorithm.Alghorithm import *
import pandas as pd
from pandas import *
from pandastable import Table
from Plot.Plot import generate_graph
from Sequences.Converters import convert_user_input_Protein, convert_user_input_RNA, convert_user_input_DNA
class App(tkinter.Tk):
    """Main application class for Needleman-Wunsch Algorithm visualizer.

       Attributes:
           container (Frame): Main container for all frames
           table_container (Frame): Container for displaying results tables
           frames (dict): Dictionary to hold all application frames
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
        """Raise the specified frame to the top of the display stack.

               Args:
                   page_class (Frame class): The frame class to display
        """
        frame = self.frames[page_class]
        frame.tkraise()
        self.update_idletasks()
        self.minsize(400,400)

class HomePage(tkinter.Frame):
    """Home page frame with navigation buttons to different input modes.

       Attributes:
           button_dna (Button): Button to navigate to DNA input page
           button_rna (Button): Button to navigate to RNA input page
           button_protein (Button): Button to navigate to Protein input page
           button_fasta (Button): Button to navigate to FASTA file input page
       """
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
    """Base class for all sequence input frames with common UI elements.

        Attributes:
            df (DataFrame): Stores alignment results
            seq1_str (str): First input sequence
            seq2_str (str): Second input sequence
            match (int): Match score parameter
            mismatch (int): Mismatch penalty parameter
            gap (int): Gap penalty parameter
        """
    def __init__(self, parent, controller, converter_function):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.convert_fun = converter_function
        self.df: pd.DataFrame = None
        self.initialize_variables()
        self.setup_ui()

    def initialize_variables(self):
        """Initialize all instance variables with default values."""
        self.file1 = None
        self.file2 = None
        self.seq1_str = ""
        self.seq2_str = ""
        self.match = 1
        self.mismatch = 0
        self.gap = -1

    def setup_ui(self):
        """Configure the frame's appearance and create all UI elements."""
        self.configure(bg="#ad86e3")
        self.setup_grid()
        self.create_input_fields()
        self.create_param_inputs()
        self.create_action_buttons()

    def setup_grid(self,row=8,column=4):
        """Create grid setup
                Args:
                    row (int): Number of rows (default = 8)
                    column (int): Number of columns (default = 4)
        """
        for i in range(row):
            self.grid_rowconfigure(i, weight=1)
        for i in range(column):
            self.grid_columnconfigure(i, weight=1)
    def create_input_fields(self):
        """Create sequence input fields and labels."""
        self.label1 = tkinter.Label(self, text="Enter first sequence")
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.enter1 = tkinter.Entry(self, bg="#ad86e3")
        self.enter1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.enter1.bind('<FocusOut>', lambda event: update_entry(event, "seq1_str", self))

        self.label2 = tkinter.Label(self, text="Enter second sequence")
        self.label2.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.enter2 = tkinter.Entry(self, bg="#ad86e3")
        self.enter2.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.enter2.bind('<FocusOut>', lambda event: update_entry(event, "seq2_str", self))
    def create_param_inputs(self):
        """Create parameter input fields (match, mismatch, gap)."""
        self._create_param_input("Match", "match", 1, 0)
        self._create_param_input("Gap", "gap", 1, 2)
        self._create_param_input("Mismatch", "mismatch", 2, 0)
    def create_action_buttons(self):
        """Method to create action buttons."""
        self._create_action_button("Generate",
                                   lambda: get_data(self.seq1_str, self.seq2_str, self.convert_fun, self.parent, self),
                                   3, 0)
        self._create_action_button("Show graph", lambda: show_graph_window(self.df, self.parent), 3, 1)
        self._create_action_button("Save as xlsx", lambda: save_to_xlsx(self.df), 3, 2)
        self._create_action_button("Save as text file", lambda: save_as_text_file(self.df,self), 3, 3)
        self._create_action_button("Back", lambda: self.controller.show_frame(HomePage), 4, 0, colspan=4)
    def _create_param_input(self, label_text, param_name, row, col):
        """Helper method to create a labeled parameter input field.

                Args:
                    label_text (str): Text for the parameter label
                    param_name (str): Name of the parameter variable
                    row (int): Grid row position
                    col (int): Grid column position
        """
        label = tkinter.Label(self, text=label_text, bg="#ad86e3")
        label.grid(row=row, column=col, padx=5, pady=5, sticky="e")
        entry = tkinter.Entry(self)
        entry.insert(0, str(getattr(self, param_name)))
        entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky="w")
        entry.bind('<FocusOut>', lambda event: update_parameters(event, param_name, self))
        setattr(self, f"enter{param_name.capitalize()}", entry)

    def _create_action_button(self, text, command, row, col, colspan=1):
        """Helper method to create an action button.

                Args:
                    text (str): Text for the button
                    command (function): Function to execute
                    row (int): Grid row position
                    col (int): Grid column position
                    colspan (int, optional): Grid column size in columns. Defaults to 1.
        """
        button = tkinter.Button(self, text=text, command=command, fg="black", bg="#5ba679")
        button.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)

class FastaInputPage(InputBaseFrame):
    """Frame for inputting sequences via FASTA files.

       Inherits from InputBaseFrame and modifies it for file input.
       """
    def __init__(self, parent, controller):
        super().__init__(parent,controller,converter_function=convert_user_input_Protein)
        self.modify_for_fasta()

    def modify_for_fasta(self):
        """Replace text entry fields with file loading buttons."""
        self.enter1.grid_remove()
        self.enter2.grid_remove()
        self._create_action_button("Add file 1", lambda: open_file(self.file1, "seq1_str", self), 0, 1)
        self._create_action_button("Add file 2", lambda: open_file(self.file2, "seq2_str", self), 0, 3)

class DNAInputPage(InputBaseFrame):
    """Frame for DNA sequence input. Inherits standard behavior from InputBaseFrame."""
    def __init__(self, parent, controller, converter_function=convert_user_input_DNA):
        super().__init__(parent, controller, converter_function)

class RNAInputPage(InputBaseFrame):
    """Frame for RNA sequence input. Inherits standard behavior from InputBaseFrame."""
    def __init__(self, parent, controller, converter_function=convert_user_input_RNA):
        super().__init__(parent, controller, converter_function)

class ProteinInputPage(InputBaseFrame):
    """Frame for protein sequence input. Inherits standard behavior from InputBaseFrame."""
    def __init__(self, parent, controller, converter_function=convert_user_input_Protein):
        super().__init__(parent, controller, converter_function)

def update_entry(event,seq:str,frame):
    """Update sequence variables when entry fields lose focus.

        Args:
            event: Tkinter event object
            seq (str): Which sequence to update ('seq1_str' or 'seq2_str')
            frame: Reference to the containing frame
        """
    if seq=="seq1_str":
        frame.seq1_str = str(frame.enter1.get())
    elif seq=="seq2_str":
        frame.seq2_str = str(frame.enter2.get())

def update_parameters(event,param:str,frame):
    """Update algorithm parameters when entry fields lose focus.

    Args:
        event: Tkinter event object
        param (str): Which parameter to update ('match', 'mismatch', or 'gap')
        frame: Reference to the containing frame
    """
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
    """Load sequence from FASTA file and update the frame.

       Args:
           file: File object
           seq (str): Which sequence to update ('seq1_str' or 'seq2_str')
           frame: Reference to the containing frame
       """
    path = filedialog.askopenfilename()
    try:
        file = open(path,'r')
        identifier = file.readline()
        content = ''.join(file.read().split())
        print(content)
        if seq == 'seq1_str':
            frame.seq1_str = content
        elif seq == 'seq2_str':
            frame.seq2_str = content
        file.close()
    except FileNotFoundError:
        messagebox.showerror("File not found", "File not found")
    except PermissionError:
        messagebox.showerror("Permission denied", "File not readable")

def get_data(seq1_str, seq2_str, converter_function, parent, frame):
    """Run alignment algorithm and display results.

        Args:
            seq1_str (str): First input sequence
            seq2_str (str): Second input sequence
            converter_function: Function to convert input sequences
            parent: Parent widget
            frame: Reference to the containing frame
        """
    input_seq1 = seq1_str
    input_seq2 = seq2_str
    seq1_labels="-"+input_seq1.upper()
    try:
        seq1 = converter_function(input_seq1)
        seq2 = converter_function(input_seq2)
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

        l=tkinter.Label(frame,text='Results:')
        l.grid(row=7,column=0, sticky="w",padx=5, pady=5, columnspan=4)

        T =tkinter.Text(frame, bg='white', bd=1, pady=5, padx=5, height=5, width=30)
        T.grid(row=8,column=0, columnspan=4,sticky="nsew",padx=10,pady=5)
        T.insert(tkinter.END, print_results(df,accumulator=traceback(df, gap=frame.gap, mismatch=frame.mismatch, match=frame.match)))

    except Exception as e:
            messagebox.showerror("Error", str(e))
            return
def print_results(df:DataFrame,accumulator)->str:
    """Format alignment results into a printable string.

        Args:
            df (DataFrame): Alignment results matrix
            accumulator: Traceback information

        Returns:
            str: Formatted results string
        """
    match_percentage, gap_percentage= percentage_for_all_matches(accumulator)
    match_percentage*=100
    gap_percentage*=100
    return f"score: {get_score(df)} \nbest alignments: {accumulator} \nmatch percentage: {match_percentage} \ngap percentage: {gap_percentage}"
def save_to_xlsx(df:DataFrame):
    """Save alignment results to Excel file."""
    root = Tk()
    try:
        with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
            df.to_excel(file.name)
    except AttributeError:
        messagebox.showerror("Error", str(AttributeError))

    root.destroy()

def save_as_text_file(df:DataFrame,frame):
    """Save alignment results to text file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                if frame:
                    file.write(f"Alignment Parameters:\n")
                    file.write(f"Match score: {frame.match}\n")
                    file.write(f"Mismatch penalty: {frame.mismatch}\n")
                    file.write(f"Gap penalty: {frame.gap}\n\n")

                file.write("Score Matrix:\n")
                file.write(df.to_string(index=True))
                file.write("\n\n")

                if hasattr(frame, 'df') and frame.df is not None:
                    alignments = traceback(frame.df, gap=frame.gap, mismatch=frame.mismatch, match=frame.match)
                    file.write(print_results(frame.df, alignments))
                    file.write("\n\nOptimal Alignments:\n")
                    for i, (seq1, seq2) in enumerate(alignments, 1):
                        file.write(f"\nAlignment {i}:\n")
                        file.write(f"Seq1: {seq1}\n")
                        file.write(f"Seq2: {seq2}\n")
                        match_pct, gap_pct = match_percentage(seq1, seq2)
                        file.write(f"Match: {match_pct * 100:.1f}%, Gaps: {gap_pct * 100:.1f}%\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def display_graph(df:DataFrame,root):
    """Display alignment results graph in a new window.

        Args:
            df (DataFrame): Alignment results to visualize
            root: Root window
        """
    new_window = tkinter.Toplevel(root)
    new_window.minsize(600,500)
    new_window.title("Graph")
    fig = generate_graph(df)
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, new_window)
    toolbar.update()
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

def show_graph_window(df:DataFrame,root):
    """Wrapper for display_graph with error handling.

        Args:
            df (DataFrame): Alignment results to visualize
            root: Root window
        """
    try:
        display_graph(df,root)
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    app=App()
    app.mainloop()

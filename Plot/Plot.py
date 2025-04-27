import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from Algorithm.Alghorithm import algorithm_implementation
from Sequences.Sequences import SequenceUser

sns.set_theme()
df = algorithm_implementation(SequenceUser("AAACCCGTT"), SequenceUser("AATCGCGTAT"), gap=-1, mismatch=0, match=1)

def generate_graph(df:DataFrame):
    """Generate a heatmap visualization of the alignment score matrix.

       Args:
           df (DataFrame): Pandas DataFrame containing alignment scores

       Returns:
           matplotlib.figure.Figure: The generated figure object

       Note:
           Only shows cell annotations for matrices smaller than 100 elements
           for readability. Uses a blue color palette.
       """
    fig, ax = plt.subplots(figsize=(6, 5))
    is_cell_text = True
    if df.size > 100:
        is_cell_text = False
    sns.heatmap(df, annot=is_cell_text, linewidths=.5, ax=ax, cmap="Blues", vmin=0)
    ax.xaxis.tick_top()
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')
    ax.set_title("Needleman-Wunsch score matrix", fontsize=12)
    return fig

if __name__ == "__main__":
    generate_graph(df)

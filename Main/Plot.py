import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

from Alghorithm import algorithm_implementation
from Sequences import SequenceUser

sns.set_theme()

def generate_graph(df:DataFrame):
    #df = algorithm_implementation(SequenceUser("AAACCCGTT"), SequenceUser("AATCGCGTAT"), gap=-1, mismatch=0, match=1)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(df, annot=True,  linewidths=.5, ax=ax,cmap="crest")
    ax.xaxis.tick_top()
    ax.set_title("Needleman-Wunsch score matrix", fontsize=12)
    return fig

if __name__ == "__main__":
    pass
    #generate_graph()

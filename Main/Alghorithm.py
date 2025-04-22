import numpy as np
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

from Sequences import *
#
# seq1="GGAATTCCA"
# seq2="GAAGTCCCA"

def algorithm_implementation(seq1 : SequenceUser, seq2 :SequenceUser, match=1, gap = -1, mismatch=0)->DataFrame:
    score = 0
    seq1 = "-" + seq1.seq()
    seq2 = "-" + seq2.seq()
    row_seq=[label for label in seq1]
    col_seq =[label for label in seq2]
    df = pd.DataFrame(np.zeros((len(seq1), len(seq2))), index=row_seq, columns=col_seq)
    for i in range(len(seq2)):
        df.iloc[0, i] = i * gap
    for j in range(len(seq1)):
        df.iloc[j, 0] = j * gap

    for i in range(1,len(seq1)):
        for j in range(1, len(seq2)):
            df.iloc[i,j]=max(
                df.iloc[i-1,j] + gap,
                df.iloc[i, j - 1] + gap,
                df.iloc[i - 1, j - 1] + match if df.index[i] == df.columns[j] else df.iloc[i - 1, j - 1] + mismatch)
    return df

def traceback(df : pd.DataFrame, match=1, gap=-1, mismatch=0):
    accumulator = []
    tracebackr(len(df.index)-1, len(df.columns) -1, '', '', df, accumulator, gap=gap, mismatch=mismatch, match=match)
    return accumulator

def tracebackr(i, j, align1, align2, df : pd.DataFrame,  accumulator : list, match=1, gap=-1, mismatch=0):
    if i == 0 and  j == 0:
        accumulator.append((align1, align2))
    if i > 0 and df.iloc[i,j] == df.iloc[i-1,j]+gap:
        tracebackr(i-1, j, '-' + align1, df.index[i]+align2, df, accumulator, match, gap, mismatch)
    if j>0 and df.iloc[i,j] == df.iloc[i,j-1]+gap:
        tracebackr(i,j-1, df.columns[j]+align1, "-"+align2, df, accumulator,match, gap, mismatch)
    if i>0 and j>0 and (df.iloc[i,j] == df.iloc[i-1,j-1]+mismatch or df.iloc[i,j] == df.iloc[i-1,j-1]+match):
        tracebackr(i-1,j-1, df.columns[j]+align1, df.index[i]+align2, df, accumulator, match, gap, mismatch)

def get_score(df:pd.DataFrame)->int:
    return df.iloc[-1,-1]

def percentage_for_all_matches(list:str):
    for alm in list:
        print(match_percentage(*alm))

def match_percentage(seq1:str,seq2:str):
    identical =  int(sum(np.array([ord(s) for s in seq1]) == np.array([ord(s) for s in seq2])))
    gaps = seq1.count("-")+seq2.count("-")
    return identical/len(seq1), gaps/len(seq1)

if __name__ == '__main__':

    # percentage_for_all_matches([('ACCT---', 'AAATTTG'), ('ACC-T--', 'AAATTTG'), ('AC-CT--', 'AAATTTG'), ('A-CCT--', 'AAATTTG'), ('-ACCT--', 'AAATTTG')])
    alms = [('ACCT---', 'AAATTTG'), ('ACC-T--', 'AAATTTG'), ('AC-CT--', 'AAATTTG'), ('A-CCT--', 'AAATTTG'), ('-ACCT--', 'AAATTTG')]
    al2s = [(seq1, seq2) for seq1, seq2 in alms]
    print(match_percentage(*alms[0]))
    # df = algorithm_implementation(seq1,seq2,gap=-1, mismatch=0,match=1)
    # print(df)
    # print(traceback(df, gap=-1, mismatch=0, match=1))
    # print(int(get_score(df)))

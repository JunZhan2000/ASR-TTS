import pandas as pd


data_file1 = "/Users/zhanjun/bishe/dataset/AISHELL-1/test/transcripts.tsv"
data_frame = pd.read_csv(data_file1, header=0)

for sample in data_frame:
    print(sample)
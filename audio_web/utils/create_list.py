import pandas as pd

mode_list = ['train', 'test', 'dev']

for mode in mode_list:
    print(mode)
    data_path = "/remote-home/jzhan/Datasets/AISHELL-1/" + mode + "/transcripts.tsv"
    save_path = "/remote-home/jzhan/Datasets/AISHELL-1/" + mode + "/transcripts.txt"

    data = pd.read_csv(data_path, sep='\t', header=0).values.tolist()
    # 以写的方式打开文件，如果文件不存在，就会自动创建
    file_write_obj = open(save_path, 'w')
    for sample in data:
        file_write_obj.writelines("/remote-home/jzhan/Datasets/AISHELL-1/" + mode + "/" + sample[0].split('/')[-2] + "/" +
                                  sample[0].split('/')[-1].strip(".wav")+".wav" + '\t' + sample[2])
        file_write_obj.write('\n')
    file_write_obj.close()

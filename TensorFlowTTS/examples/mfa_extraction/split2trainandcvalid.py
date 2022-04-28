import os
import shutil


def move_file(src_path, dst_path, file):
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print('move_file ERROR: ')

# train_files = []
# data_path = "/remote-home/jzhan/download/TensorFlowTTS/dump/train/ids"
# for filename in os.listdir(data_path):
#     train_files.append(filename.rstrip('-ids.npy'))
# train_path = "/remote-home/jzhan/download/TensorFlowTTS/dump/train/durations/"
# valid_path = "/remote-home/jzhan/download/TensorFlowTTS/dump/valid/durations/"
#
# for filename in os.listdir(train_path):
#     file_id = filename.rstrip('-durations.npy')
#     file_id = str(int(file_id))
#     if file_id in train_files:
#         os.rename(train_path+filename, train_path+file_id+'-durations.npy')
#     else:
#         move_file(train_path, valid_path, filename)
#         os.rename(valid_path + filename, valid_path + file_id + '-durations.npy')



val_files = []
data_path = "/remote-home/jzhan/download/TensorFlowTTS/dump/valid/ids"
for filename in os.listdir(data_path):
    val_files.append(filename.rstrip('-ids.npy'))
valid_path = "/remote-home/jzhan/download/TensorFlowTTS/dump/valid/durations/"

nums1 = 0
for filename in os.listdir(valid_path):
    file_id = filename.rstrip('-durations.npy')
    if file_id not in val_files:
        move_file(valid_path, "/remote-home/jzhan/download", filename)

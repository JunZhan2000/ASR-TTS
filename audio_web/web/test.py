from pydub import AudioSegment
def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")


file_name = "/Users/zhanjun/Downloads/80ab4fde-792e-4540-83d1-453090879719.ogg"
text = open(file_name,"rb").read()   # 读取二进制文件
f = open(file_name, "wb")
f.write(text)
f.close()
trans_any_audio_types(file_name, "ogg", "wav")

from flask import Flask, render_template, request, send_from_directory
from tts import load_model, tts_save_audios
import os
from asr.asr import load_asr_model
from pydub import AudioSegment

asr_model = load_asr_model()
text2mel_model, vocoder, processor = load_model()
root_path = os.getcwd()
app = Flask("Audio Studio")


@app.route('/')
def index():
   return render_template('index.html')


filename = "./static/audio/upload.ogg"


@app.route('/asr_result', methods=['GET'])
def asr_fc_result():
    # content = filename  # 识别
    content = asr_model.stt(filename)
    content = "拼音：" + content[0] + "\n文本：" + content[1].replace("</S>", "")
    return render_template('asr.html', content=content)


@app.route('/asr', methods=['GET', 'POST'])
def asr_fc():
    if request.method == 'POST':
        print(request.method)
        print(request.files)
        file = request.data
        if file:
            f = open(filename, "wb")
            f.write(file)
            f.close()
            return "ok"
    return render_template('asr.html')


@app.route('/tts', methods=['GET', 'POST'])
def tts_fc():
    if request.method == 'GET':  # 判断是否是 POST 请求
        return render_template('tts.html')
    # 获取表单数据
    input_text = request.form.get('content')
    print('文本：', input_text)
    audio_path = "/static/audio/test.wav"
    audio_path = "/static/audio/" + input_text + ".wav"
    tts_save_audios(input_text, text2mel_model, vocoder, processor, audio_path)
    return render_template('tts_result.html', audio_path=audio_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
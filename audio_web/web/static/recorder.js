const recordBtn = document.querySelector(".record-btn");
const player = document.querySelector(".audio-player");


if (navigator.mediaDevices.getUserMedia) {
    var chunks = [];
    const constraints = {audio: true};
    navigator.mediaDevices.getUserMedia(constraints).then(
        stream => {
            console.log("授权成功！");

            const mediaRecorder = new MediaRecorder(stream);

            recordBtn.onclick = () => {
                if (mediaRecorder.state === "recording") {
                    mediaRecorder.stop();
                    recordBtn.textContent = "开始录制";
                    console.log("录音结束");
                } else {
                    mediaRecorder.start();
                    console.log("录音中...");
                    recordBtn.textContent = "停止录制";
                }
                console.log("录音器状态：", mediaRecorder.state);
            };

            mediaRecorder.ondataavailable = e => {
                chunks.push(e.data);
            };

            mediaRecorder.onstop = e => {
                var blob = new Blob(chunks, {type: "audio/ogg; codecs=opus"});
                chunks = [];
                var audioURL = window.URL.createObjectURL(blob);
                player.src = audioURL;
                // var fd = new FormData();
                // fd.append('audio_file', blob);
                // fd.append('filename', "test123.wav")
                //
                // var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                // httpRequest.open('POST', 'http://localhost:9000/asr', true); //第二步：打开连接
                // httpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                // httpRequest.send(fd);//发送请求 将情头体写在send中
                var xhr = new XMLHttpRequest();//第一步：创建需要的对象
                xhr.open('POST', 'http://localhost:9000/asr', true); //第二步：打开连接
                xhr.setRequestHeader('X-File-Name', blob.name);
                xhr.setRequestHeader('X-File-Size', blob.size);
                xhr.setRequestHeader('Content-Type', blob.type);
                xhr.send(blob);

            };
        },

        () => {
            console.error("授权失败！");
        }
    );
} else {
    console.error("浏览器不支持 getUserMedia");
}
function render({ model, el }) {
    el.classList.add("volume-meter-widget");
    function textChanged() {
        el.textContent = model.get("text");
        el.style.backgroundColor = model.get("color")
    }
    textChanged();
    model.on("change:text", textChanged);
    model.on("change:color", textChanged);
    navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false
    })
        .then(function (stream) {
            const audioContext = new AudioContext();
            const microphone = audioContext.createMediaStreamSource(stream);
            const analyser = audioContext.createAnalyser();
            analyser.smoothingTimeConstant = 0.8;
            analyser.fftSize = 1024;

            microphone.connect(analyser);
            const array = new Uint8Array(analyser.fftSize);
            const timer = setInterval(() => {
                analyser.getByteTimeDomainData(array);
                const volume = array.reduce((max, current) => Math.max(max, Math.abs(current - 127)), 0) / 128;
                model.set("volume", volume);
                model.save_changes();
                if (!document.body.contains(el)) {
                    stream.getTracks().forEach((track) => {
                        if (track.readyState == 'live') {
                            track.stop();
                        }
                    });
                    clearInterval(timer)
                }
            }, 1000)
        })
        .catch(function (err) {
            /* handle the error */
            console.error(err);
        })
}

export default { render }
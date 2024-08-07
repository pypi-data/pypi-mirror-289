function render({ model, el }) {
    el.classList.add("photo-widget");
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        const capture = document.createElement('button');
        capture.textContent = 'Capture';
        el.appendChild(capture);
        const video = document.createElement('video');
        video.style.display = 'block';
        el.appendChild(video)
        video.srcObject = stream;
        video.play().then(() => {
            function onclick() {
                const canvas = document.createElement('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                stream.getVideoTracks()[0].stop();
                el.remove()
                model.set("dataURL", canvas.toDataURL('image/jpeg', 0.8));
                model.save_changes();
            }
            capture.onclick = onclick
        })
    })
}

export default { render }
function render({ model, el }) {
    el.classList.add("timer-widget");
    let target = Date.now() / 1000
    function targetChanged() {
        target = model.get("target");
    }
    targetChanged();
    model.on("change:target", targetChanged);
    const timer = setInterval(() => {
        let current = Date.now() / 1000
        let seconds = target - current
        if (seconds < 0) {
            el.textContent = "Timer completed!"
        } else {
            let minutes = Math.floor(seconds / 60)
            seconds -= minutes * 60
            seconds = Math.round(seconds)
            el.textContent = `${minutes} minutes, ${seconds} seconds remaining`
        }
        if (!document.body.contains(el)) {
            clearInterval(timer)
        }
    }, 1000)
}

export default { render }
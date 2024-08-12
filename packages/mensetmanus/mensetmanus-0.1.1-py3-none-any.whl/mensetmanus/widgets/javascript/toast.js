function render({ model, el }) {
    el.classList.add("toast-widget");
    let delay = 1.
    function delayChanged() {
        delay = model.get("delay");
    }
    function textChanged() {
        let text = model.get("text")
        if (text !== "") {
            el.textContent = text
            setTimeout(() => {
                el.textContent = ""
            }, delay * 1000)
        }
    }
    delayChanged();
    textChanged()
    model.on("change:delay", delayChanged);
    model.on("change:text", textChanged);
}

export default { render }
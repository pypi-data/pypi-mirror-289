import typing
import pathlib
import ipywidgets
import anywidget
import traitlets

DEFAULT_LEVELS = [
    {"volume": 0.005, "text": "Great", "color": "green"},
    {"volume": 0.03, "text": "Good", "color": "orange"},
    {"volume": 0.05, "text": "Needs Improvement", "color": "red"},
]


class PhotoWidget(anywidget.AnyWidget):
    _esm = (pathlib.Path(__file__).parent / "javascript" / "photo.js").read_text()
    _css = """
    .photo-widget {
        padding: 10px;
        text-align: center;
        font-size: 20px;
    }
    """

    dataURL = traitlets.Unicode("").tag(sync=True)


class ToastWidget(anywidget.AnyWidget):
    _esm = (pathlib.Path(__file__).parent / "javascript" / "toast.js").read_text()
    _css = """
    .toast-widget {
        padding: 10px;
        text-align: center;
        font-size: 20px;
    }
    """

    delay = traitlets.Float(0.0).tag(sync=True)
    text = traitlets.Unicode("").tag(sync=True)

    def __init__(self, delay: float = 1.0):
        super().__init__()
        self.delay = delay


class TimerWidget(anywidget.AnyWidget):
    _esm = (pathlib.Path(__file__).parent / "javascript" / "timer.js").read_text()
    _css = """
    .timer-widget {
        padding: 10px;
        text-align: center;
        font-size: 20px;
    }
    """

    target = traitlets.Float(0.0).tag(sync=True)

    def __init__(self, target: float):
        super().__init__()
        self.target = target


class VolumeMeterWidget(anywidget.AnyWidget):
    _esm = (pathlib.Path(__file__).parent / "javascript" / "volume.js").read_text()
    _css = """
    .volume-meter-widget {
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 20px;
    }
    """
    text = traitlets.Unicode("Volume Not Yet Measured").tag(sync=True)
    color = traitlets.Unicode("green").tag(sync=True)
    volume = traitlets.Float(0.0).tag(sync=True)

    def __init__(self, levels: typing.Optional[typing.List[typing.Dict]] = None):
        super().__init__()
        self.levels = levels or DEFAULT_LEVELS
        self.observe(self.on_change, names=["volume"])

    def on_change(self, change):
        if change["type"] == "change" and change["name"] == "volume":
            volume = change["new"]
            selected = None
            for level in self.levels:
                if volume > level["volume"]:
                    selected = level
            selected = selected or self.levels[0]
            self.text = f"{volume}: {selected['text']}"
            self.color = selected["color"]


def build_seating_chart(students, configs):
    """Build a seating chart visual.

    Args:
        students: A list of dicts containing a "name" parameter.
        configs: A list of table configs indicating "color" (for background), "text_color" (for foreground),
            and "name" for the title for the table.
    """
    tables = [[] for _ in configs]
    for student in students:
        min(tables, key=len).append(student)
    display = []
    for config, table in zip(configs, tables):
        display.append(
            ipywidgets.HTML(
                value=f"""
            <div style='color: {config['text_color']}; background-color: {config['color'].lower()}; padding: 15px; font-style: bold'>
                <p>{config['name']}</p>
                <ul>
                {"".join(["<li>" + s["name"] + "</li>" for s in table])}
                </ul>
            </div>
            """,
            )
        )
    return ipywidgets.HBox(display)

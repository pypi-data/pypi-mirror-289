# Standard libraries:
from typing import TypeAlias, Optional, Tuple, Dict, Any
from tkinter import Widget, Event, Misc


class TransparentMisc(Misc):
    is_transparent: bool = False

    def __init__(self, master: Optional[Misc] = None, *, background: Optional[str] = "transparent", **standard_options: Any) -> None:
        assert isinstance(self, Widget), "This instance must be a Widget."
        super().__init__(master, **standard_options)
        self.configure(background=background)
        self.bind(sequence="<<ParentConfigure>>", func=self.on_parent_configure, add=True)

    def configure(self, **standard_options: Any) -> Any:
        background_color: Optional[str] = standard_options.pop("background", None)
        background_color = standard_options.pop("bg", background_color)
        if background_color is not None:
            self.is_transparent = isinstance(background_color, str) and background_color == "transparent"
            if not self.is_transparent:
                standard_options["background"] = background_color
            self.on_parent_configure()
        return super().configure(**standard_options)
    config = configure

    def on_parent_configure(self, event: Optional[Event] = None) -> None:
        if not self.is_transparent:
            return None
        parent_background_color: Optional[str] = Misc.cget(self.master, key="background") or None
        if parent_background_color is None:
            return None
        Misc.configure(self.master, background=parent_background_color)
        for child_widget in self.winfo_children():
            child_widget.event_generate(sequence="<<ParentConfigure>>")

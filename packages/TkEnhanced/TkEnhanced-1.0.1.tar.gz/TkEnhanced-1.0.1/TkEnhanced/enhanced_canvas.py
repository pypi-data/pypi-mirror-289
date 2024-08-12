# Local imports:
from ._transparent_misc import TransparentMisc

# Standard libraries:
from typing import Optional, Any
from tkinter import Canvas, Misc


class EnhCanvas(TransparentMisc, Canvas):
    def __init__(self, master: Optional[Misc] = None, *, background: Optional[str] = "transparent", **standard_options: Any) -> None:
        super().__init__(master, background=background, **standard_options)

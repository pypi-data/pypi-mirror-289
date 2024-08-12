# Local imports:
from . import EnhFrame

# Standard libraries:
from typing import Optional, Any
from tkinter import Misc


class EnhScrollableFrame(EnhFrame):
    def __init__(self, master: Optional[Misc] = None, *, background: Optional[str] = "transparent", **standard_options: Any) -> None:
        super().__init__(master, background=background, **standard_options)

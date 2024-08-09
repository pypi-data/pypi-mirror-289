from zenlite.core.globs import *
from .__init__ import zenprocess

class zenrenderer(zenprocess):
    def __init__(self) -> None:
        super().__init__()

    def process(self, *args, **kwargs) -> None:
        print("zen-rendering\n")
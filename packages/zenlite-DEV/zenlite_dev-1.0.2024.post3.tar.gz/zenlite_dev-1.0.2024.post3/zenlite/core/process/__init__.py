from zenlite.core.globs import *

class zenprocess:
    def __init__(self, prio:int=1) -> None:
        self.prio:int=prio

    def process(self, *args, **kwargs) -> None:
        raise NotImplementedError

from .core.globs import pg, gl, glm, glfw
from .zplatform import *
from .zapplication import *
from .core.process.render import zenrenderer

class zenlite:
    def __init__(self) -> None: pass

    def process(self, *args, **kwargs) -> None: pass

def init() -> zenlite:
    z:zenlite=zenlite()
    # parse config
    # configure engine
    # run local tests
    return z

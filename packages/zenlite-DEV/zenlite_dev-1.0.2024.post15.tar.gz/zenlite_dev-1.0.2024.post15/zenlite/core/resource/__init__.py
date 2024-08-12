from zenlite.core.globs import pg, glm, np

class zenresource:
    def __init__(self, id:int=-1) -> None:
        self.id=id

class zenbank2:
    def __init__(self, max:int, *args, **kwargs):
        self.max:int=max
        self.count:int=0

class zenbank:
    def __init__(self, max:int, *args, **kwargs):
        self.nresource:int=0
        self.resources:dict={}

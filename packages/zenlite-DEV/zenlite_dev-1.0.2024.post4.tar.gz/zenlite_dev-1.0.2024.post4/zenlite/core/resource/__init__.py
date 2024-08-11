from core.globs import pg, glm, np

class zenbank:
    def __init__(self, max:int, *args, **kwargs):
        self.nresource:int=0
        self.resources:dict={}

from .zvxchunk import zvxchunk
from ..globs import pg, glm, np, bytec
from ..resource.zenmesh import zenmesh

class zvxrealm:
    def __init__(self, ) -> None: ...

class zvxchunkbed:
    def __init__(self, ) -> None:
        self.chunksize:float=32.0
        self.dimensions:glm.vec3=glm.vec3(2, 2, 2)
        self.area:float=self.dimensions.x*self.dimensions.z
        self.volume:float=self.area*self.dimensions.y
        self.centery:float=self.dimensions.y*self.chunksize
        self.centerxz:float=self.dimensions.x*self.chunksize
        self.chunk_ids:list[int]=[-1 for _ in range(self.volume)]

    def fill_chunks(self) -> None:...
    def build_chunks(self) -> None:...
    
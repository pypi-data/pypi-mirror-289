import moderngl as GL
from .__init__ import zenbank, zenresource
from zenlite.core.globs import pg, np, glm
from zenlite.core.zenvx.zvxchunk import build_zvxmesh

class zvxchunk(zenresource):
    def __init__(self, id:int) -> None:
        super().__init__(id=id)
        self.voxels=None
        self.size:int=None
        self.area:int=None
        self.hsize:int=None
        self.volume:int=None
        self.nvoxels:int=None
        self.mesh_id:int=None
        self.vxsize:float=None

ZVX_CHUNK_MAX:int=10_000
class zvxchunkbank(zenbank):
    def __init__(self, zenresources, *args, **kwargs):
        super().__init__(max=ZVX_CHUNK_MAX, *args, **kwargs)
        self.zenresources=zenresources
        self.size:list[int]=[-1 for _ in range(self.max)]
        self.area:list[int]=[-1 for _ in range(self.max)]
        self.hsize:list[int]=[-1 for _ in range(self.max)]
        self.volume:list[int]=[-1 for _ in range(self.max)]
        self.nvoxels:list[int]=[-1 for _ in range(self.max)]
        self.mesh_id:list[int]=[-1 for _ in range(self.max)]
        self.vxsize:list[float]=[float for _ in range(self.max)]
        self.voxels:list[np.ndarray]=[ [] for _ in range(self.max) ]

    def get_chunk(self, chunk_id:int) -> zvxchunk|zenresource|None:
        if chunk_id <= self.max and chunk_id != -1:
            c:zvxchunk=zvxchunk(chunk_id)
            c.size=self.size[chunk_id]
            c.area=self.area[chunk_id]
            c.hsize=self.hsize[chunk_id]
            c.volume=self.volume[chunk_id]
            c.nvoxels=self.nvoxels[chunk_id]
            c.mesh_id=self.mesh_id[chunk_id]
            c.vxsize=self.vxsize[chunk_id]
            c.voxels=self.voxels[chunk_id]
            return c
        else: return None

    def make_chunk(self, size:int, vxsize:float) -> int:
        if self.count+1 <= self.max:
            chunk_id:int=self.count
            self.nvoxels[chunk_id]=0
            self.size[chunk_id]=size
            self.area[chunk_id]=size*size
            self.hsize[chunk_id]=size/2
            self.vxsize[chunk_id]=vxsize
            self.volume[chunk_id]=self.area[chunk_id]*size
            self.voxels[chunk_id]=np.zeros(self.volume[chunk_id], dtype="uint8")

            self.count+=1; self.voxelize(chunk_id); return chunk_id

    def voxelize(self, chunk_id:int) -> None:
        """
            voxels exist as a number from 0-255 where 0 is empty space
            rather than storing them in 3D arrays (glm.vec3(vx_x, vx_y, vx_z))
            they are stored in a 1D array which will be indexed using the following formula
            from 3D space to 1D array:  AREA=SIZE*SIZE
                                        INDEX=X+SIZE*Z+AREA*Y
        """
        if chunk_id <= self.max and chunk_id != -1:
            for x in range(self.size[chunk_id]):
                for z in range(self.size[chunk_id]):
                    for y in range(self.size[chunk_id]):
                        # set the zvx_id
                        self.voxels[chunk_id][x+self.size[chunk_id]*z+self.area[chunk_id]*y]= (
                            x + y + z if int(glm.simplex(glm.vec3(x, y, z) * 0.1) + 1) else 0
                        )
                        # self.voxels[x+self.size*z+self.area*y]=x+y+z
            self.nvoxels[chunk_id]=len(self.voxels[chunk_id])

    def build(self, chunk_id:int) -> None:
        if chunk_id <= self.max and chunk_id != -1:
            self.mesh_id[chunk_id]=self.zenresources.meshbank.make_mesh(
                vertices=build_zvxmesh(
                    self.area[chunk_id],
                    self.size[chunk_id],
                    self.volume[chunk_id],
                    self.voxels[chunk_id],
                    sum(int(fmt[:1]) for fmt in '3u1 1u1 1u1'.split()),
                    self.vxsize[chunk_id],
                ),
                vformat='3u1 1u1 1u1',
                vattribs=('position', 'zvx_id', 'face_id'),
                # TODO: either make a chunk specific shader, or introduce shader conditionals
                shader_id=self.zenresources.shaders["default002"],
            )


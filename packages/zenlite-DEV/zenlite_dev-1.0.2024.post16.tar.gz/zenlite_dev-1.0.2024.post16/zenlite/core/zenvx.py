from .globs import pg, glm, np, bytec
from .resource.zenmesh import zenmesh

# this function inspects a voxel to determine if it lay outside of the chunk, or has a vzx_id of 0
def zvx_void(location, zvxarr, zvxchunksize, zvxchunkarea) -> bool:
    x,y,z=location
    if 0 <= x < zvxchunksize and 0 <= y < zvxchunksize and 0 <= z < zvxchunksize:
        if zvxarr[x+zvxchunksize*z+zvxchunkarea*y]:
            return False
    return True

# this function interleaves attributes from calculated vertices into the final vertex_buffer, while increasing a stride counter
def zvx_interleave(stride, vbuffer, *vertices) -> int:
    for vertex in vertices:
        for attrib in vertex:
            vbuffer[stride]=attrib;stride+=1
    return stride

def build_zvxmesh(zvxchunkarea, zvxchunksize, zvxchunkvol, zvxarr, vformatsize, voxel_size):
    # the size of the vertex data array is determined by this formula:
    # size = chunk_volume * vx_vertices * vertex_atrributes
    # each voxel is made of a cube which can only ever have a max of 3 faces visible upon construction
    # these 3 faces are made of 2 triangles, which each consist of 3 vertices ( 3faces * 2triangles * 3vertices ) = 18 possible vertices
    # each voxel will then have 5 vertex attributes that need to be interleaved into the chunk-mesh's vertex buffer:
    # (x, y, z) each, a zvx_id and a face_id
    # the zvx_id will range between 0-255 to determine the type of voxel it is allowing for specific configuration/behaviors
    # the face_id will simply tell us which face each vertex belongs to (assuming a right handed coordinate system (-z is forward))

    stride:int = 0
    vbuffer:np.ndarray = np.empty(zvxchunkvol * 18 * vformatsize, dtype="uint8")

    for x in range(zvxchunksize):
        for y in range(zvxchunksize):
            for z in range(zvxchunksize):
                zvx_id = zvxarr[x + zvxchunksize * z + zvxchunkarea * y]
                if not zvx_id: continue
                
                # Calculate positions with voxel size
                x0, y0, z0 = x * voxel_size, y * voxel_size, z * voxel_size
                x1, y1, z1 = x0 + voxel_size, y0 + voxel_size, z0 + voxel_size

                # check each face of the voxel to determine if vertices should be constructed if the face is not obstructed
                # Top face
                #           world space
                #        relative to the chunk
                if zvx_void((x, y + 1, z), zvxarr, zvxchunksize, zvxchunkarea):
                    # vertex data format: x, y, z, zvx_id, face_id
                    v0 = (x0, y1, z0, zvx_id, 0)
                    v1 = (x1, y1, z0, zvx_id, 0)
                    v2 = (x1, y1, z1, zvx_id, 0)
                    v3 = (x0, y1, z1, zvx_id, 0)
                    stride = zvx_interleave(stride, vbuffer, v0, v3, v2, v0, v2, v1)
                    #                                  indexing vertices by hand

                # Bottom face
                if zvx_void((x, y - 1, z), zvxarr, zvxchunksize, zvxchunkarea):
                    v0 = (x0, y0, z0, zvx_id, 1)
                    v1 = (x1, y0, z0, zvx_id, 1)
                    v2 = (x1, y0, z1, zvx_id, 1)
                    v3 = (x0, y0, z1, zvx_id, 1)
                    stride = zvx_interleave(stride, vbuffer, v0, v2, v3, v0, v1, v2)

                # Right face
                if zvx_void((x + 1, y, z), zvxarr, zvxchunksize, zvxchunkarea):
                    v0 = (x1, y0, z0, zvx_id, 2)
                    v1 = (x1, y1, z0, zvx_id, 2)
                    v2 = (x1, y1, z1, zvx_id, 2)
                    v3 = (x1, y0, z1, zvx_id, 2)
                    stride = zvx_interleave(stride, vbuffer, v0, v1, v2, v0, v2, v3)

                # Left face
                if zvx_void((x - 1, y, z), zvxarr, zvxchunksize, zvxchunkarea):
                    v0 = (x0, y0, z0, zvx_id, 3)
                    v1 = (x0, y1, z0, zvx_id, 3)
                    v2 = (x0, y1, z1, zvx_id, 3)
                    v3 = (x0, y0, z1, zvx_id, 3)
                    stride = zvx_interleave(stride, vbuffer, v0, v2, v1, v0, v3, v2)

                # Back face
                if zvx_void((x, y, z - 1), zvxarr, zvxchunksize, zvxchunkarea):
                    v0 = (x0, y0, z0, zvx_id, 4)
                    v1 = (x0, y1, z0, zvx_id, 4)
                    v2 = (x1, y1, z0, zvx_id, 4)
                    v3 = (x1, y0, z0, zvx_id, 4)
                    stride = zvx_interleave(stride, vbuffer, v0, v1, v2, v0, v2, v3)

                # Front face
                if zvx_void((x, y, z + 1), zvxarr, zvxchunksize, zvxchunkarea):
                    v0 = (x0, y0, z1, zvx_id, 5)
                    v1 = (x0, y1, z1, zvx_id, 5)
                    v2 = (x1, y1, z1, zvx_id, 5)
                    v3 = (x1, y0, z1, zvx_id, 5)
                    stride = zvx_interleave(stride, vbuffer, v0, v2, v1, v0, v3, v2)

    return vbuffer[:stride + 1]


class zvxchunkmesh(zenmesh):
    def __init__(self, chunk):
        super().__init__()
        self.m_model=glm.identity(glm.mat4)
        self.chunk:zvxchunk=chunk
        self.vformat='3u1 1u1 1u1'
        self.vformatsize=sum(int(fmt[:1]) for fmt in self.vformat.split())
        self.vattribs=('position', 'zvx_id', 'face_id')

    def construct(self, resources, context) -> None:
        self.vertices=build_zvxmesh(
            self.chunk.area,
            self.chunk.size,
            self.chunk.volume,
            self.chunk.voxels,
            self.vformatsize,
            self.chunk.vxsize,
        )
        self.shader=resources.zenshaders["zenshader002"]
        self.vbo=context.GL.buffer(self.vertices)
        self.vao=context.GL.vertex_array(
            self.shader.program,
            [(self.vbo, self.vformat, *self.vattribs)], skip_errors=True
        )
        resources.meshbank._insert(self)

class zvxchunk:
    def __init__(self, vxsize:float=1.0) -> None:
        self.size:int=32
        self.nvoxels:int=0
        self.vxsize:float=vxsize
        self.hsize:int=self.size//2
        self.area:int=self.size*self.size
        self.volume:int=self.area*self.size
        self.mesh:zvxchunkmesh=zvxchunkmesh(self)
        self.voxels=np.zeros(self.volume, dtype="uint8")

    def build(self, resources, context) -> None:
        # empty chunk
        """
            voxels exist as a number from 0-255 where 0 is empty space
            rather than storing them in 3D arrays (glm.vec3(vx_x, vx_y, vx_z))
            they are stored in a 1D array which will be indexed using the following formula
            from 3D space to 1D array:  AREA=SIZE*SIZE
                                        INDEX=X+SIZE*Z+AREA*Y
        """
        self.voxels=np.zeros(self.volume, dtype="uint8")

        # fill the chunk
        for x in range(self.size):
            for z in range(self.size):
                for y in range(self.size):
                    # set the zvx_id
                    self.voxels[x+self.size*z+self.area*y]= (
                        x + y + z if int(glm.simplex(glm.vec3(x, y, z) * 0.1) + 1) else 0
                    )
                    # self.voxels[x+self.size*z+self.area*y]=x+y+z

        self.nvoxels=len(self.voxels)
        # construct mesh
        self.mesh.construct(resources, context)




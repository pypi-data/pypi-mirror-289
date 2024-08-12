from .__init__ import zenresource, zenbank, zenbank2, glm, np

class zenmesh(zenresource):
    def __init__(self, id:int=-1):
        super().__init__(id=id)
        self.vbo:int=None
        self.vao:int=None
        self.shader:int=None
        """ zenresource id """
        self.texture:int=None
        """ zenresource id """
        self.vformat:str=None
        self.vertices:list[float]=None
        self.vattribs:tuple[str, ...]=None
        self.m_model:glm.mat4=glm.identity(glm.mat4)

    def set_shader(self, shader) -> None: self.shader=shader
    def set_texture(self, texture) -> None: self.texture=texture

ZEN_MESH_MAX:int=100
class zenmeshbank2(zenbank2):
    def __init__(self, zencontext, *args, **kwargs):
        super().__init__(max=ZEN_MESH_MAX)
        self.context=zencontext
        self.zenresources = args[0]
        self.vbo:list[int]=[-1 for _ in range(self.max)]
        self.vao:list[int]=[-1 for _ in range(self.max)]
        
        self.shader:list[int]=[-1 for _ in range(self.max)]
        """ zenresource id -> get a mesh shader interface = zen.resource.sbank.get_shader(mesh.shader) """
        
        self.texture:list[int]=[-1 for _ in range(self.max)]
        """ zenresource id -> get a mesh texture interface = zen.resource.tbank.get_texture(mesh.texture) """
        
        self.vformat:list[str]=["None" for _ in range(self.max)]
        self.vertices:list[list[float]]=[[] for _ in range(self.max)]
        self.vattribs:list[tuple[str]]=[tuple() for _ in range(self.max)]
        self.m_model:list[glm.mat4]=[glm.identity(glm.mat4) for _ in range(self.max)]

    def make_mesh(self, vertices: list[tuple[float]], vattribs: tuple[str] = ('position',), vformat: str = "3f", indices: list[tuple[int]] = None, colors: list[tuple[float]] = None) -> zenmesh:
        mesh_id:int=self.count
        mesh:zenmesh = zenmesh(id=mesh_id)

        mesh.vformat = vformat
        self.vformat[mesh_id] = mesh.vformat

        mesh.vattribs = vattribs
        self.vattribs[mesh_id] = mesh.vattribs
        
        vertices_np = np.array(vertices, dtype="float32")
        colors_np = np.array(colors, dtype="float32") if colors is not None else None
        
        if colors is not None: vertex_data = np.hstack([vertices_np, colors_np], dtype="float32")
        else: vertex_data = vertices_np
            
        if indices is not None: vertex_data = np.array([vertex_data[ind] for triangle in indices for ind in triangle], dtype="float32")

        mesh.vertices = vertex_data
        self.vertices[mesh_id] = mesh.vertices

        mesh.vbo = self.context.GL.buffer(mesh.vertices)
        self.vbo[mesh_id] = mesh.vbo

        mesh.shader = self.zenresources.zenshaders["zenshader001"]
        self.shader[mesh_id] = mesh.shader.id

        mesh.vao = self.context.GL.vertex_array(
            self.zenresources.zenshaders["zenshader001"].program,
            [(mesh.vbo, mesh.vformat, *mesh.vattribs)], skip_errors=True
        )
        self.vao[mesh_id] = mesh.vao

        self.count += 1
        return mesh

class zenmeshbank(zenbank):
    def __init__(self, zencontext, *args, **kwargs):
        super().__init__(max=ZEN_MESH_MAX)
        self.context=zencontext
        self.zenresources = args[0]

    # private method, SHOULD NOT BE CALLED BY AN END USER!!!
    def _insert(self, mesh:zenmesh) -> None:
        mesh.id = self.nresource
        self.resources[mesh.id] = mesh
        self.nresource += 1

    def make_mesh(self, vertices: list[tuple[float]], vattribs: tuple[str] = ('position',), vformat: str = "3f", indices: list[tuple[int]] = None, colors: list[tuple[float]] = None) -> zenmesh:
        mesh:zenmesh = zenmesh()
        mesh.vformat = vformat
        mesh.vattribs = vattribs
        
        vertices_np = np.array(vertices, dtype="float32")
        colors_np = np.array(colors, dtype="float32") if colors is not None else None
        
        if colors is not None: vertex_data = np.hstack([vertices_np, colors_np], dtype="float32")
        else: vertex_data = vertices_np
            
        if indices is not None: vertex_data = np.array([vertex_data[ind] for triangle in indices for ind in triangle], dtype="float32")

        mesh.vertices = vertex_data
        mesh.vbo = self.context.GL.buffer(mesh.vertices)
        mesh.shader = self.zenresources.zenshaders["zenshader001"]
        mesh.vao = self.context.GL.vertex_array(
            self.zenresources.zenshaders["zenshader001"].program,
            [(mesh.vbo, mesh.vformat, *mesh.vattribs)], skip_errors=True
        )
        mesh.id = self.nresource
        self.resources[mesh.id] = mesh
        self.nresource += 1
        return mesh

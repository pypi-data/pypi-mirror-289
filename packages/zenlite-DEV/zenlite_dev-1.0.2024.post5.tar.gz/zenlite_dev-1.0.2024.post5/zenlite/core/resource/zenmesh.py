from .__init__ import zenbank, glm, np

class zenmesh:
    def __init__(self):
        self.id:int=None
        self.vbo:int=None
        self.vao:int=None
        self.shader:int=None
        self.texture:int=None
        self.vformat:str=None
        self.vertices:list[float]=None
        self.vattribs:tuple[str, ...]=None
        self.m_model:glm.mat4=glm.identity(glm.mat4)

    def set_shader(self, shader) -> None: self.shader=shader
    def set_texture(self, texture) -> None: self.texture=texture

ZEN_MESH_MAX:int=100
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

    def _make_vertex_data(self, vertices:list[float], colors:list[float]=None, indices:list[int]=None, dtype:str="float32") -> np.ndarray:
        return np.hstack([vertices, colors], dtype=dtype)

    def make_mesh(self, vertices: list[tuple[float]], vattribs: tuple[str] = ('position',), vformat: str = "3f", indices: list[tuple[int]] = None, colors: list[tuple[float]] = None) -> zenmesh:
        mesh:zenmesh = zenmesh()
        mesh.vformat = vformat
        mesh.vattribs = vattribs
        
        vertices_np = np.array(vertices, dtype="float32")
        colors_np = np.array(colors, dtype="float32") if colors is not None else None
        
        if colors is not None: vertex_data = self._make_vertex_data(vertices_np, colors_np)
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

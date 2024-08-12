import glm
from .__init__ import zenbank, zenresource, zenbank2

class zenshader(zenresource):
    def __init__(self, id:int, vsrc:str, fsrc:str, tag:str=None):
        super().__init__(id=id)
        self.tag:str=tag
        self.vsrc:str=vsrc
        self.fsrc:str=fsrc
        self.program:int=None
        self.nuniforms:int=0
        self.uniforms:dict={
            "m_proj":glm.identity(glm.mat4),
            "m_view":glm.identity(glm.mat4),
            "m_model":glm.identity(glm.mat4)
        }

    def new_uniform(self, name:str, data=None) -> None:
        uni=self.uniforms.get(name, None)
        if uni is None and self.nuniforms+1 < 16:
            self.uniforms[name] = data
            self.nuniforms+=1
        return None
    
    def set_uniform(self, name:str, data) -> None:
        uni=self.uniforms.get(name, None)
        if uni is None: return None
        try:
            self.program[name].write(data)
        except () as err: print(err); return None
        self.uniforms[name]=data

ZEN_SHADER_MAX:int=100
class zenshaderbank2(zenbank2):
    def __init__(self, zencontext, *args, **kwargs):
        super().__init__(max=ZEN_SHADER_MAX, *args, **kwargs)
        self.context=zencontext
        self.tag:list[str]=["NULL" for _ in range(self.max)]
        self.program:list[int]=[-1 for _ in range(self.max)]
        self.vsrc:list[str]=["NULL" for _ in range(self.max)]
        self.fsrc:list[str]=["NULL" for _ in range(self.max)]
        self.nuniforms:list[int]=[-1 for _ in range(self.max)]
        self.uniforms:list[dict]=[{} for _ in range(self.max)]

    def get_shader(self, shader_id:int) -> None|zenshader|zenresource:
        if isinstance(shader_id, int) and shader_id <= self.max:
            s:zenshader=zenshader()
            s.tag=self.tag[shader_id]
            s.vsrc=self.vsrc[shader_id]
            s.fsrc=self.fsrc[shader_id]
            s.program=self.program[shader_id]
            s.uniforms=self.uniforms[shader_id]
            s.nuniforms=self.nuniforms[shader_id]
            return s
        else: return None

    def make_shader(self, vsrc:str, fsrc:str, tag:str=None) -> int:
        if self.count+1 <= self.max:
            shader_id:int=self.count
            self.tag[shader_id]=tag
            self.vsrc[shader_id]=vsrc
            self.fsrc[shader_id]=fsrc
            self.nuniforms[shader_id]=0
            self.uniforms[shader_id]={
                "m_proj":glm.identity(glm.mat4),
                "m_view":glm.identity(glm.mat4),
                "m_model":glm.identity(glm.mat4)
            }

            with open(vsrc, 'r') as vertex: vertex_shader = vertex.read(); vertex.close()
            with open(fsrc, 'r') as fragment: fragment_shader = fragment.read(); fragment.close()

            self.program[shader_id]=self.context.GL.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

            self.count+=1; return shader_id


class zenshaderbank(zenbank):
    def __init__(self, zencontext, *args, **kwargs):
        super().__init__(max=ZEN_SHADER_MAX, *args, **kwargs)
        self.context=zencontext

    def make_shader(self, vsrc:str, fsrc:str, tag:str=None):
        zshader:zenshader=zenshader(vsrc, fsrc, tag)
        zshader.id=self.nresource
        with open(vsrc, 'r') as vertex: vertex_shader = vertex.read(); vertex.close()
        with open(fsrc, 'r') as fragment: fragment_shader = fragment.read(); fragment.close()

        zshader.program = self.context.GL.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        self.resources[ tag if tag is not None else f"shader_{self.nresource}" ]=zshader
        self.nresource+=1

    def get_shader(self, tag:str):
        shader = self.resources.get(tag, None)
        if shader is None:
            print("ERROR GETTING SHADER: ",tag,end="")
            return None
        else: return shader

    def set_uniforms(self, shader:str, uniform:str, data) -> None:
        try:
            shader = self.get_shader(shader)
            if shader is None: raise KeyError
            else: 
                try: 
                    shader.program[uniform].write(data)
                except () as err: print(err); return
            shader.uniforms[uniform] = data
        except(KeyError) as err: return

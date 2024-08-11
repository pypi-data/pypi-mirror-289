from .__init__ import zenbank
import glm

class zenshader:
    def __init__(self, vsrc:str, fsrc:str, tag:str=None):
        self.id:int=0
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

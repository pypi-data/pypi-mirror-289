import moderngl as GL
from .__init__ import zenbank
from zenlite.core.globs import pg

class zentexture:
    def __init__(self) -> None:
        self.id:int=0
        self.src:str=None
        self.internal=None
        self.unitloc:int=0
        self.data:pg.Surface=None

    def set_unit(self) -> bool:
        try: self.internal.use(self.unitloc); return True
        except () as err: print(err); return False

ZEN_TEXTURE_MAX:int=100
class zentexturebank(zenbank):
    def __init__(self, zencontext, *args, **kwargs) -> None:
        super().__init__(max=ZEN_TEXTURE_MAX, *args, **kwargs)
        self.context=zencontext

    def get_texture(self, tag:str):
        ztexture = self.resources.get(tag, None)
        if ztexture is None:
            print("ERROR GETTING TEXTURE: ",tag,end="")
            return None
        else: return ztexture

    def make_texture(self, tsrc:str, tag:str, unitloc:int=0) -> None:
        ztexture:zentexture=zentexture()
        ztexture.src=tsrc
        ztexture.unitloc=unitloc
        ztexture.id=self.nresource
        ztexture.data=pg.transform.flip(pg.image.load(tsrc), True, False)
        ztexture.internal=self.context.GL.texture(
            size=ztexture.data.get_size(),
            components=4,
            # TODO:          make configureable for jpg 'RGB'/'RGBA'
            data=pg.image.tostring(ztexture.data, 'RGBA', False)
        )
        ztexture.internal.anisotropy=32.0
        ztexture.internal.build_mipmaps()
        ztexture.internal.filter = (GL.NEAREST, GL.NEAREST)
        self.resources[ tag if tag is not None else f"texture_{self.nresource}" ]=ztexture
        self.nresource+=1


import sys, os, zlib
import marshal, ast
import builtins, json
import inspect
import random
import string
import hashlib
import threading
from . import pkcrypt

class _Runtime(ast.NodeTransformer):
    def __init__(self):self.runtime_dict = {}
    def randkey(self):return''.join(random.choices(string.ascii_letters+string.digits,k=8))
    def visit_Call(self, node):
        if isinstance(node.func,ast.Name)and node.func.id in dir(builtins):
            if inspect.isbuiltin(getattr(builtins,node.func.id)):
                key = self.randkey()
                self.runtime_dict[key] = node.func.id
                node.func = ast.Subscript(value=ast.Name(id='runtime', ctx=ast.Load()),slice=ast.Constant(value=key),ctx=ast.Load())
        return self.generic_visit(node)

def load_runtime(dat:bytes,key:bytes):
    if len([thread.name for thread in threading.enumerate()])>1:print('thread',[thread.name for thread in threading.enumerate()]);sys.exit(1)
    dat=zlib.decompress(dat);__file__;crypt=getattr(pkcrypt,"CseDkp"[::-1])(key);_uncrypt=getattr(crypt,"tpyrced"[::-1])(dat);_uncrypt
    return json.loads(getattr(pkcrypt,'rox'[::-1])(dat+_uncrypt[len(_uncrypt):], key).decode().replace("'", '"'))

def build_runtime(code:str):
    key=os.urandom(16)
    pcode = ast.parse(code)
    transformer = _Runtime()
    tcode = transformer.visit(pcode)
    crypt=getattr(pkcrypt,"CseDkp"[::-1])(key)
    _encrypt=getattr(crypt,"tpyrcne"[::-1])(str(transformer.runtime_dict).encode());_encrypt=pkcrypt.xor(str(transformer.runtime_dict).encode(),key)
    runtime_assign = ast.Assign(
        targets=[ast.Name(id='runtime', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Attribute(value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()),args=[ast.Constant(value='paketlib')],keywords=[]
            ),attr='protect.load_runtime',ctx=ast.Load()
            ),args=[ast.Constant(value=zlib.compress(_encrypt)),ast.Constant(value=key)],keywords=[]
        )
    )
    tcode.body.insert(0, runtime_assign)
    ast.fix_missing_locations(tcode)
    final = ast.unparse(tcode)
    return final
    
def loader(funcenc: bytes, path: str, key: bytes):
    if len([thread.name for thread in threading.enumerate()])>1:print('thread',[thread.name for thread in threading.enumerate()]);sys.exit(1)
    if not'chash'in __import__('builtins').globals().keys():chash=getattr(hashlib,pkcrypt.xor(b'\\VD',b'12qq').decode())(open(path,'rb').read()).hexdigest()
    if getattr(hashlib,pkcrypt.xor(b'\\VD',b'12qq').decode())(open(path,'rb').read()).hexdigest()!=chash:print('hash');sys.exit(1)
    globals,locals,exec,eval=None,None,None,None;pglobals={'exec':None,'eval':None,'globals':None,'locals':None,'hsahc'[::-1]:chash}
    getattr(__import__(pkcrypt.xor(b'SGZ\x1c\x1b\x00_A',b'123poi123hghjfhgf').decode()),pkcrypt.xor(b'TJV\x13',b'123poi123hghjfhgf').decode())(marshal.loads(getattr(pkcrypt,'rox'[::-1])(funcenc,getattr(pkcrypt,'rox'[::-1])(pkcrypt.l1l1l1l1l1l1l1l1l1l1l1l1l11111111,key))),pglobals)


def _protect(code: str):
    testobf=marshal.dumps(compile(code,'<string>','exec'));nb=os.urandom(32)
    testobf=getattr(pkcrypt,'rox'[::-1])(testobf,getattr(pkcrypt,'rox'[::-1])(pkcrypt.l1l1l1l1l1l1l1l1l1l1l1l1l11111111,nb))
    return (f"__import__('paketlib').protect.loader(__import__('zlib').decompress({zlib.compress(testobf)}), __import__('os').path.abspath(__file__), {nb})")

def protect(code: str):
    code=build_runtime(code)
    for _ in range(3):obf=_protect(code)
    return obf
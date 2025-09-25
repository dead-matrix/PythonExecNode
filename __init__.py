import sys
import subprocess

class PythonExecNode:
    CATEGORY = "Custom/Development"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run"
   
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"code": ("STRING", {"multiline": True})}}

    def run(self, code):
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        out = (r.stdout or "") + (r.stderr or "")
        return (out.strip(),)
    
NODE_CLASS_MAPPINGS = {"PythonExecNode": PythonExecNode}
NODE_DISPLAY_NAME_MAPPINGS = {"PythonExecNode": "Python Exec"}
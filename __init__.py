import sys
import io

class PythonExecNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "code": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "Custom/Development"

    def run(self, code):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # ограничим пространство имён
        safe_globals = {"__builtins__": __builtins__}
        local_vars = {}
        try:
            exec(code, safe_globals, local_vars)
            output = sys.stdout.getvalue()
            if local_vars:
                vars_repr = ", ".join(f"{k}={v!r}" for k, v in local_vars.items())
                output += f"\nLocals: {vars_repr}"
        except Exception as e:
            output = f"Error: {e}"
        finally:
            sys.stdout = old_stdout

        return (output.strip(),)


NODE_CLASS_MAPPINGS = {
    "PythonExecNode": PythonExecNode
}

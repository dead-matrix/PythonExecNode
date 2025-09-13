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
    CATEGORY = "Custom"

    def run(self, code):
        # перехватываем stdout
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        local_vars = {}
        try:
            exec(code, globals(), local_vars)
            output = sys.stdout.getvalue()
            # добавим вывод переменных, если нужно
            if local_vars:
                output += "\nLocals: " + str(local_vars)
        except Exception as e:
            output = f"Error: {e}"
        finally:
            sys.stdout = old_stdout

        return (output.strip(),)


NODE_CLASS_MAPPINGS = {
    "PythonExecNode": PythonExecNode
}

import io
import sys

def run_snippet(code: str) -> dict:
    """
    Execute a code snippet and capture stdout.
    Returns a dictionary with stdout as string.
    """
    buffer = io.StringIO()
    try:
        sys_stdout = sys.stdout
        sys.stdout = buffer
        exec(code, {})
        return {"stdout": buffer.getvalue()}
    finally:
        sys.stdout = sys_stdout

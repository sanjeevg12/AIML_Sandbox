from sandbox.lessons import get_lessons
from sandbox.runner import run_snippet

def test_imports():
    lessons = get_lessons()
    assert isinstance(lessons, list) and len(lessons) >= 2

    out = run_snippet("print('ok')")
    assert "ok" in out["stdout"]

import runpy
import io
from contextlib import redirect_stdout

def test_demo_output():
    f = io.StringIO()
    with redirect_stdout(f):
        runpy.run_path('demo_1.py')
    assert f.getvalue().strip() == '9'
import os
import tempfile
import shutil
from contextlib import contextmanager
import pytest

"""
Comparison
Aspect	@contextmanager	Pytest Fixtures
Scope	Limited to the block within the with statement	Can be function, class, module, or session
Usage	General Python code, including tests	Specifically for pytest tests
Integration	Used with the with statement	Declared as parameters in test functions
Reusability	Can be reused across any Python code	Can be reused across multiple test functions
Setup/Teardown	Handled around the yield statement	Handled around the yield statement
Configuration	More manual, requires explicit with statements	Automatically applied to test functions
"""
import os
import tempfile
import shutil
from contextlib import contextmanager

@contextmanager
def temporary_directory():
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

def test_temporary_directory():
    with temporary_directory() as temp_dir:
        assert os.path.isdir(temp_dir)
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, 'w') as f:
            f.write("Hello, pytest!")
        assert os.path.exists(file_path)
        with open(file_path, 'r') as f:
            assert f.read() == "Hello, pytest!"

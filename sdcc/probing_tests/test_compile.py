import re
import subprocess

import pytest

from .compilation import diagnoser, executor, gdict


@pytest.fixture(scope="session")
def clang_version():
    clang_version_string = subprocess.check_output(
        ["clang", "--version"], universal_newlines=True
    )
    print("clang version:", clang_version_string)
    # assume little about how version is printed, e.g. because macOS mangles it
    m = re.search(r"((\d+)\.(\d+)\.\d+)", clang_version_string, flags=re.I)
    return m


@pytest.mark.dependency(
    name="test_clang",
    depends=['test_exist'],
    scope="session",
)
def test_clang_version_exists(clang_version):
    """Test if clang exists."""
    assert clang_version, \
        "can not parse clang version '{clang_version_string}'"


@pytest.mark.dependency(
    name='test_compile',
    depends=['test_exist'],
    scope="session",
)
def test_it(clang_version, stu_answer_content, stu_answer, artifacts):
    """Test compilation."""
    process = executor.run(
        clang_version, stu_answer_content, stu_answer, artifacts
    )
    gdict['process'] = process
    assert \
        not process.stdout and process.returncode == 0


@pytest.mark.dependency(
    name="test_compile_flipped",
    depends=['test_exist'],
    scope="session",
)
def test_flipped(artifacts):
    process = gdict['process']
    assert not \
        (not process.stdout and process.returncode == 0)
    (artifacts / 'compilation_error.txt').write_text(process.stdout)


@pytest.mark.parametrize("label, regex", diagnoser.params)
def test_reason(label, regex):
    process = gdict['process']
    assert re.search(regex, process.stdout, flags=re.I | re.DOTALL) is not None

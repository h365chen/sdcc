import subprocess

import pytest

gdict = {}


@pytest.mark.order(0)
def test_compile_wrapper():
    """Compile wrapper code to .o file to be linked later."""
    wrapper = 'probing_tests/dcc_runtime/dcc_main.c'
    obj = 'probing_tests/dcc_runtime/dcc_c_wrapper_source.o'
    cmd = f"clang -c {wrapper} -o {obj} -gdwarf-4 -g -O3".split()
    subprocess.run(
        cmd,
        input="",
        text=True,
        check=False,
    )


@pytest.mark.order(1)
def test_link(stu_answer):
    """Compile and link student's answer."""
    # temporary overwrite
    stu_answer = 'probing_tests/dcc_runtime/student.c'
    obj = 'probing_tests/dcc_runtime/dcc_c_wrapper_source.o'
    exe = 'probing_tests/dcc_runtime/a.out'

    # -fsanitize=address -fsanitize=undefined
    # ^ they cause issues; move them out for now
    cmd = f"""
    clang
    -Wall -Wno-unused -Wunused-variable -Wunused-value -Wno-unused-result -Wshadow
    -Og
    -fcolor-diagnostics -fdiagnostics-color
    -gdwarf-4 -Wunused-comparison -fno-omit-frame-pointer -fno-common -funwind-tables -fno-optimize-sibling-calls -Qunused-arguments -Wno-unused-parameter -Wno-return-type
    -D_exit=__renamed__exit
    -Dclose=__renamed_close
    -Dexecvp=__renamed_execvp
    -Dgetpid=__renamed_getpid
    -Dmain=__real_main
    -Dfileno=__wrap_fileno
    {obj}
    {stu_answer}
    -lm
    -o {exe}
    """.split()  # noqa
    print(' '.join(cmd))
    subprocess.run(
        cmd,
        input="",
        text=True,
        check=False,
    )


@pytest.mark.order(2)
def test_segfault():
    """Check if there is a segment fault."""
    # Start the subprocess
    exe = 'probing_tests/dcc_runtime/a.out'
    cmd = f"./{exe}".split()
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        text=True,
    )
    gdict["pid"] = process.pid
    # Stream the output line by line
    for line in process.stdout:
        if "received signal" in line:
            assert True
            return
    assert False


@pytest.mark.order(3)
def test_lldb():
    """Attach LLDB and do inspection."""
    pid = gdict["pid"]
    cmd = f"lldb -p {pid}".split()
    lldb_cmds = """
thread backtrace
kill
    """.strip()
    subprocess.run(
        cmd,
        input=lldb_cmds,
        text=True,
        check=False,
    )
    assert False

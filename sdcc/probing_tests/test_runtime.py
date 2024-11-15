import subprocess
import time

import pytest

gdict = {}


@pytest.mark.skip(reason="It seems we don't need a wrapper code. We can just launch with `lldb ./a.out`")  # noqa
def test_compile_wrapper():
    """Compile wrapper code to .o file to be linked later."""
    wrapper = 'probing_tests/dcc_runtime/dcc_main.c'
    obj = 'probing_tests/dcc_runtime/dcc_c_wrapper_source.o'
    cmd = f"""
    clang
    -g
    -O0
    -gdwarf-4
    -c {wrapper}
    -o {obj}
    """.split()
    process = subprocess.run(
        cmd,
        input="",
        text=True,
        check=False,
    )
    print(process.stdout)
    # assert 0


@pytest.mark.order(1)
def test_link(stu_answer):
    """Compile and link student's answer."""
    # temporary overwrite
    stu_answer = 'probing_tests/dcc_runtime/student.c'
    # obj = 'probing_tests/dcc_runtime/dcc_c_wrapper_source.o'
    exe = 'probing_tests/dcc_runtime/a.out'

    # -fsanitize=address -fsanitize=undefined
    # ^ they cause issues; move them out for now
    cmd = f"""
    clang
    -O0
    -g
    -gdwarf-4
    -Wall
    -Wno-unused -Wunused-variable -Wunused-value
    -Wno-unused-result -Wshadow -Wunused-comparison
    -Wno-unused-parameter -Wno-return-type
    -fno-omit-frame-pointer -fno-common
    -funwind-tables -fno-optimize-sibling-calls
    -fcolor-diagnostics -fdiagnostics-color
    -Qunused-arguments
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
    cmd = f"""
    lldb
    --
    ./{exe}
    """.split()
    # TODO: what about using pytest's captures?
    with subprocess.Popen(cmd,
                          stdin=subprocess.PIPE,
                          # stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          text=True,
                          bufsize=1,
                          universal_newlines=True
                          ) as proc:

        # LLDB commands with a precoded waiting time
        # TODO: better specify the waiting time
        lldb_cmds = [
            ('run', 1),
            ('frame variable', 0.2),
            ('kill', 0.1),
            ('quit', 0.1),
        ]
        for command, t in lldb_cmds:
            proc.stdin.write(command + '\n')
            proc.stdin.flush()
            time.sleep(t)
            # ^ note that proc.stdout.readline() is blocking
            # so it cannot be used here

        # capture stdout in pytest, so following code is not needed
        # close stdin and fetch stdout
        # stdout, _ = proc.communicate()
        # print(stdout)
    assert False

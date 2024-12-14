import subprocess
import time

import pytest


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


@pytest.mark.dependency(
    name="test_runtime",
    depends=['test_compile'],
    scope="session",
)
def test_it(artifacts, capfd):
    """Check if there is a segment fault."""
    # Start the subprocess
    exe = artifacts / 'dcc' / 'a.out'
    cmd = f"""
    lldb
    --
    {exe}
    """.split()
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

    out, _ = capfd.readouterr()
    if "exited with status = 0" not in out:
        (artifacts / 'lldb_out.txt').write_text(out)
        print(out)
        assert False

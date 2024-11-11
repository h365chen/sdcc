"""Contain code to compile student's code."""

import os
import subprocess
import sys


def run(clang_version, stu_answer_content, stu_answer, artifacts):
    """Contain code to compile student's submission."""
    os.environ["PATH"] = (
        os.path.dirname(os.path.realpath(sys.argv[0]))
        + ":/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:"
        + os.environ.get("PATH", "")
    )

    temp_dir = artifacts / 'dcc'
    (temp_dir / "a.out").unlink(missing_ok=True)  # rm a.out
    for f in temp_dir.glob("*.o"):  # rm *.o
        f.unlink(missing_ok=True)
    temp_dir.mkdir(exist_ok=True)

    COMMON_COMPILER_ARGS = """
        -Wall
        -Wno-unused
        -Wunused-variable
        -Wunused-value
        -Wno-unused-result
        -Wshadow
        """.split()

    command = (
        ["clang"]
        + COMMON_COMPILER_ARGS
        # + ["-fsanitize=address"]
        + ["-o", str(temp_dir / "a.out")]
        + [str(stu_answer)]
        + ["-lm"]
    )
    print("compile command: ", " ".join(command))
    process = subprocess.run(
        command,
        input="",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        errors="replace",
        check=False,
    )
    return process

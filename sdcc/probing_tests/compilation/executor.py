"""Contain code to compile student's code."""

import subprocess


def run(clang_version, stu_answer_content, stu_answer, artifacts):
    """Contain code to compile student's submission."""
    temp_dir = artifacts / 'dcc'
    target = temp_dir / 'a.out'
    target.unlink(missing_ok=True)  # rm a.out
    for f in temp_dir.glob("*.o"):  # rm *.o
        f.unlink(missing_ok=True)
    temp_dir.mkdir(exist_ok=True)

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
    -o {target}
    {stu_answer}
    -lm
    """.split()  # noqa
    print("compile command: ", " ".join(cmd))
    process = subprocess.run(
        cmd,
        input="",
        text=True,
        check=False,
    )
    return process

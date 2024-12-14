"""Extract pytest context."""

import math
import re

import pytest
from socassess import userargs

from . import gdict


@pytest.mark.dependency(
    depends=["test_reason_warning[double_int_literal_conversion]"],
    scope="session",
)
def test_double_int_literal_conversion():
    process = gdict['compilation']['process']
    content = process.stderr
    lines = content.splitlines()
    for prev_line, next_line in zip(lines[:-1], lines[1:]):
        if re.match(r"^[ ~\d|]*\^[ ~]*$", next_line):
            m = re.match(r"^(.*)\^~+", next_line)
            if m:
                highlighted_word = prev_line[len(m.group(1)):len(m.group(0))]
            else:
                caret_index = next_line.index("^")
                m = re.match(r"^\w*", prev_line[caret_index:])
                highlighted_word = m.group(0)

            underlined_word = ""
            m = re.match(r"^(.*?)~+", next_line)
            if m:
                underlined_word = prev_line[len(m.group(1)):len(m.group(0))]
    userargs.pytest_context['double_int_literal_conversion'] = {
        "highlighted_word": highlighted_word,
        "underlined_word": underlined_word,
        "highlighted_word_truncated": str(math.trunc(float(highlighted_word)))
    }


@pytest.mark.dependency(
    depends=["test_reason_error[missing_semicolon_line_before_assert]"],
    scope="session",
)
def test_missing_semicolon_line_before_assert():
    process = gdict['compilation']['process']
    content = process.stderr
    lines = content.splitlines()
    m = re.match(r"^(\S.*?):(\d+):", lines[0])
    if m:
        stufile, line_number = m.groups()
    userargs.pytest_context['missing_semicolon_line_before_assert'] = {
        'stufile': stufile if stufile else None,
        'line_number': int(line_number)-1 if line_number else None,  # the previous line is the cause  # noqa
    }

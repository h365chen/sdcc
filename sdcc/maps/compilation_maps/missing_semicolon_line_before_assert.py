"""Feedback on compilation ERROR."""

# flake8: noqa
from socassess import userargs


def fetch_fields() -> dict:
    """Extract fields from the compilation message for this feedback."""
    content = (userargs.artifacts / 'compilation_error.txt').read_text()
    return {
        "content": '\n'.join(['> ' + line for line in content.splitlines()]),
        "stufile": userargs.pytest_context['missing_semicolon_line_before_assert']['stufile'],
        "line_number": userargs.pytest_context['missing_semicolon_line_before_assert']['line_number'],
    }


mappings = {
    frozenset([
        'test_compile::test_compile::failed',
        'test_compile::test_compile_flipped::passed',
        'test_compile::test_reason_error[missing_semicolon_line_before_assert]::passed',
        'compilation.test_extract_context::test_missing_semicolon_line_before_assert::passed',
    ]): {
        'feedback': """

Oops! There's a compilation error.

{content}

There is probably a syntax error such as missing semi-colon on line
{line_number} of {stufile} or an earlier line

Reproduce:

```
#include <assert.h>

int main(void) {
    int i = 10
    assert(i == 10);
}
```

        """
        .strip(),
        'function': fetch_fields,
    },
}

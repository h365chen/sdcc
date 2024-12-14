"""Feedback on compilation WARNING."""

# flake8: noqa
from socassess import userargs


def fetch_fields() -> dict:
    """Extract fields from the compilation message for this feedback."""
    content = (userargs.artifacts / 'compilation_warning.txt').read_text()
    lines = content.splitlines()
    return {
        "content": '\n'.join(['> ' + line for line in lines]),
    }


mappings = {
    frozenset([
        'test_compile::test_no_warning::failed',
        'test_compile::test_no_warning_flipped::passed',
        'test_compile::test_reason_warning[indexing_one_too_far]::passed',
    ]): {
        'feedback': """

Oops! There's a compilation warning.

{content}

Remember arrays indices start at zero.
The valid array indices for an array of size n are 0..n-1.
For example, for an array of size 10 you can use 0..9 as indices.

Reproduce:

```
int main(void) {
    int a[42] = { 0 };
    return a[42];
}
```

        """
        .strip(),
        'function': fetch_fields,
    },
}

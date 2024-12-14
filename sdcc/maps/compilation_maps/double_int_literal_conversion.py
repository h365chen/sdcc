"""Feedback on compilation WARNING."""

# flake8: noqa
from socassess import userargs


def fetch_fields() -> dict:
    """Extract fields from the compilation message for this feedback."""
    content = (userargs.artifacts / 'compilation_warning.txt').read_text()
    lines = content.splitlines()
    return {
        "content": '\n'.join(['> ' + line for line in lines]),
        "highlighted_word": userargs.pytest_context['double_int_literal_conversion']['highlighted_word'],
        "underlined_word": userargs.pytest_context['double_int_literal_conversion']['underlined_word'],
        "highlighted_word_truncated": userargs.pytest_context['double_int_literal_conversion']['highlighted_word_truncated'],
    }


mappings = {
    frozenset([
        'test_compile::test_no_warning::failed',
        'test_compile::test_no_warning_flipped::passed',
        'test_compile::test_reason_warning[double_int_literal_conversion]::passed',
        'compilation.test_extract_context::test_double_int_literal_conversion::passed',
    ]): {
        'feedback': """

Oops! There's a compilation warning.

{content}

You are assigning the floating point number {highlighted_word} to the int
variable {underlined_word}, if this is what you want, change {highlighted_word} to {highlighted_word_truncated}.

Reproduce:

```
int main(int argc, char *argv[]) {
    int i = 6.7;
    return i;
}
```

        """
        .strip(),
        'function': fetch_fields,
    },
}

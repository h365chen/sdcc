from socassess import userargs


def fetch_fields() -> dict:
    """Extract fields from the compilation message for this feedback."""
    content = (userargs.artifacts / 'lldb_out.txt').read_text()
    return {
        "content": content,
    }


mappings = {
    frozenset([
        'test_runtime::test_it::failed',
    ]): {
        'feedback': """

Oops! There's a runtime error.

{content}

        """
        .strip(),
        'function': fetch_fields,
    },
}

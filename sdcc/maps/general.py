mappings = {
    frozenset([
        # Since this is an one-line binary test so we assume the only cause of
        # its failure is the file was not found.
        'test_it::test_exist::failed',
    ]): {
        'feedback': 'Oops! Did you forget to submit the file or did name your file correctly?',  # noqa: E501
    },
    frozenset([
        'test_it::test_exist::passed',
    ]): {
        'feedback': 'Nice! I found your solution!',
    },
}

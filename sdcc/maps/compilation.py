# TODO: use wildcard instead of naming each module

from .compilation_maps import (double_int_literal_conversion,
                               indexing_one_too_far,
                               missing_semicolon_line_before_assert)

passed = {
    frozenset([
        'test_compile::test_compile::passed',
        'test_compile::test_compile_flipped::failed',
    ]): {
        'feedback': """

Nice! Your code compiles.

        """
        .strip(),
    },
}

mappings = passed \
    | double_int_literal_conversion.mappings \
    | missing_semicolon_line_before_assert.mappings \
    | indexing_one_too_far.mappings

# Representative answer

`missing_semicolon_line_before_assert.c`

# Feedback

```
# Feedback

## general

Nice! I found your solution!

## compilation

Oops! There's a compilation issue.

> /private/var/folders/__/mwshqy7j2zx96dpf5b1k9cn80000gn/T/pytest-of-huanyi/pytest-2/test_match_missing_semicolon_l0/stu/student.c:5:5: error: called object type 'int' is not a function or function pointer
>     4 |     int i = 10
>       |             ~~
>     5 |     assert(i == 10);
>       |     ^
> /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/assert.h:75:5: note: expanded from macro 'assert'
>    75 |     (__builtin_expect(!(e), 0) ? __assert_rtn(__func__, __ASSERT_FILE_NAME, __LINE__, #e) : (void)0)
>       |     ^
> 1 error generated.

There is probably a syntax error such as missing semi-colon on line
4 of /private/var/folders/__/mwshqy7j2zx96dpf5b1k9cn80000gn/T/pytest-of-huanyi/pytest-2/test_match_missing_semicolon_l0/stu/student.c or an earlier line

Reproduce:

\```
#include <assert.h>

int main(void) {
    int i = 10
    assert(i == 10);
}
\```


```

# Error message if any
# Representative answer

`double_int_literal_conversion.c`

# Feedback

```
# Feedback

## general

Nice! I found your solution!

## compilation

Oops! There's a compilation issue.

> /private/var/folders/__/mwshqy7j2zx96dpf5b1k9cn80000gn/T/pytest-of-huanyi/pytest-2/test_match_double_int_literal_0/stu/student.c:2:11: warning: implicit conversion from 'double' to 'int' changes value from 6.7 to 6 [-Wliteral-conversion]
>     2 |   int i = 6.7;
>       |       ~   ^~~
> 1 warning generated.

You are assigning the floating point number 6.7 to the int
variable i, if this is what you want, change 6.7
to 6

Reproduce:

\```
int main(int argc, char *argv[]) {
    int i = 6.7;
    return i;
}
\```


```

# Error message if any
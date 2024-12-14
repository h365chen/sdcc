# Representative answer

`double_int_literal_conversion.c`

# Feedback

```
# Feedback

## general

Nice! I found your solution!

## compilation

Nice! Your code compiles.
Oops! There's a compilation warning.

> /private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_double_int_literal_0/stu/student.c:2:11: warning: implicit conversion from 'double' to 'int' changes value from 6.7 to 6 [-Wliteral-conversion]
>     2 |   int i = 6.7;
>       |       ~   ^~~
> 1 warning generated.

You are assigning the floating point number 6.7 to the int
variable i, if this is what you want, change 6.7 to 6.

Reproduce:

\```
int main(int argc, char *argv[]) {
    int i = 6.7;
    return i;
}
\```

## runtime

Oops! There's a runtime error.

(lldb) target create "/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_double_int_literal_0/artifacts/dcc/a.out"
Current executable set to '/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_double_int_literal_0/artifacts/dcc/a.out' (arm64).
(lldb) run
Process 34667 launched: '/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_double_int_literal_0/artifacts/dcc/a.out' (arm64)
Process 34667 exited with status = 6 (0x00000006) 
(lldb) frame variable
error: Command requires a process which is currently stopped.
(lldb) kill
error: Process must be launched.
(lldb) quit



```

# Error message if any
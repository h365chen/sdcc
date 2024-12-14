# Representative answer

`indexing_one_too_far.c`

# Feedback

```
# Feedback

## general

Nice! I found your solution!

## compilation

Nice! Your code compiles.
Oops! There's a compilation warning.

> /private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_indexing_one_too_fa0/stu/student.c:3:5: warning: array index 5 is past the end of the array (that has type 'int[5]') [-Warray-bounds]
>     3 |     a[5] = 0;
>       |     ^ ~
> /private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_indexing_one_too_fa0/stu/student.c:2:5: note: array 'a' declared here
>     2 |     int a[5];
>       |     ^
> 1 warning generated.

Remember arrays indices start at zero.
The valid array indices for an array of size n are 0..n-1.
For example, for an array of size 10 you can use 0..9 as indices.

Reproduce:

\```
int main(void) {
    int a[42] = { 0 };
    return a[42];
}
\```

## runtime

Oops! There's a runtime error.

(lldb) target create "/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_indexing_one_too_fa0/artifacts/dcc/a.out"
Current executable set to '/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_indexing_one_too_fa0/artifacts/dcc/a.out' (arm64).
(lldb) run
Process 34656 launched: '/private/var/folders/wk/dq6crxqs62338j1lkx160z980000gn/T/pytest-of-huanyi/pytest-6/test_match_indexing_one_too_fa0/artifacts/dcc/a.out' (arm64)
Process 34656 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = signal SIGABRT
    frame #0: 0x0000000183c66600 libsystem_kernel.dylib`__pthread_kill + 8
libsystem_kernel.dylib`__pthread_kill:
->  0x183c66600 <+8>:  b.lo   0x183c66620               ; <+40>
    0x183c66604 <+12>: pacibsp 
    0x183c66608 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x183c6660c <+20>: mov    x29, sp
Target 0: (a.out) stopped.
(lldb) frame variable
(lldb) kill
Process 34656 exited with status = 9 (0x00000009) killed
(lldb) quit



```

# Error message if any
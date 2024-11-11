# Representative answer

`indexing_one_too_far.c`

# Feedback

```
# Feedback

## general

Nice! I found your solution!

## compilation

Oops! There's a compilation issue.

> /private/var/folders/__/mwshqy7j2zx96dpf5b1k9cn80000gn/T/pytest-of-huanyi/pytest-2/test_match_indexing_one_too_fa0/stu/student.c:3:5: warning: array index 5 is past the end of the array (that has type 'int[5]') [-Warray-bounds]
>     3 |     a[5] = 0;
>       |     ^ ~
> /private/var/folders/__/mwshqy7j2zx96dpf5b1k9cn80000gn/T/pytest-of-huanyi/pytest-2/test_match_indexing_one_too_fa0/stu/student.c:2:5: note: array 'a' declared here
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


```

# Error message if any
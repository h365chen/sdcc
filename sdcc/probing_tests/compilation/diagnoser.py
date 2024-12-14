"""Contain code to explain some of the compilation errors."""

# flake8: noqa

import pytest

params_warning = [
    pytest.param(
        label, regex,
        marks=pytest.mark.dependency(
            name=f"test_reason_warning[{label}]",
            depends=["test_no_warning_flipped"],
            scope='session',
        ),
        id=label,
    ) for label, regex in [
        ("double_int_literal_conversion", r"implicit conversion from 'double' to 'int'"),
        ("indexing_one_too_far", r"array index (\d+) is past the end of the array.*(which contains \1 element|\[\1\])"),
    ]
]

params_error = [
    pytest.param(
        label, regex,
        marks=pytest.mark.dependency(
            name=f"test_reason_error[{label}]",
            depends=["test_compile_flipped"],
            scope='session',
        ),
        id=label,
    ) for label, regex in [
        ("two_main_functions", r"multiple definition of \W*main\b"),
        ("no_main_function", r"undefined reference to \W*main\b"),
        ("scanf_missing_ampersand", r"format specifies type '(?P<type>int|double) \*' but the argument has type '(?P=type)'"),
        ("format_type_mismatch", r"format specifies type '[^:]+' but the argument has type '[^:]+'"),
        ("missing_semicolon_line_before_assert", r"called object type 'int' is not a function or function pointer"),
        ("assert_without_closing_parenthesis", r"unterminated function-like macro invocation"),
        ("assign_to_multidimensional_array", r"array type .*?\]\[.* is not assignable"),
        ("assign_to_array", r"array type .*?[^\]]\[(\d+)\]' is not assignable"),
        ("stack_use_after_return", r"address of stack memory associated with local variable '(.*?)' returned"),
        ("assign_function_to_int", r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'.*\("),
        ("assign_array_to_int", r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'.*]'"),
        ("assign_pointer_to_int", r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'"),
        ("missing_library_include", r"(implicitly declaring library function|call to undeclared library function) '(\w+)'"),
        ("misspelt_printf", r"(implicit declaration of|call to undeclared) function '(print.?.?)'"),
        ("implicit_function_declaration", r"(implicit declaration of function|call to undeclared function) '(\w+)'"),
        ("expression_is_not_assignable", r"expression is not assignable"),
        ("uninitialized-local-variable", r"'(.*)' is used uninitialized in this function"),
        ("function-variable-clash", r"called object type .* is not a function or function pointer"),
        ("function_definition_not_allowed_here", r"function definition is not allowed here"),
        ("indirection_requires_pointer_operand", r"indirection requires pointer operand \('(.*)' invalid\)"),
        ("duplicated_cond", r"duplicated .*\bif\b.* condition"),
        ("condition_has_identical_branches", r"condition has identical branches"),
        ("logical_or_always_true", r"logical .?\bor\b.* is always true|logical.*or.*of collectively exhaustive tests is always true|overlapping comparisons always evaluate to true"),
        ("logical_and_always_false", r"logical .?\band\b.* is always false|overlapping comparisons always evaluate to false"),
        ("logical_equal_expressions", r"logical .?((and|or)).? of equal expressions"),
        ("declaration_shadows_a_local_variable", r"declaration shadows a local variable"),
        ("nonnull", r"argument (\d+) null where non-null expected"),
        ("array_subscript_is_not_an_integer", r"array subscript is not an integer"),
        ("continue_statement_not_in_loop", r"continue.* statement not in loop"),
        ("break_statement_not_in_loop", r"break.* statement not in loop"),
        ("non_void_function_does_not_return_a_value_in_all_control_paths", r"non-void function does not return a value in all control paths"),
        ("non_void_function_does_not_return_a_value", r"non-void function does not return a value \["),
        ("data_argument_not_used_by_format_string", r"data argument not used by format string"),
        ("more_percent_conversions_than_data_arguments", r"more '%' conversions than data arguments"),
        ("expected_semicolon_in_for_statement_specifier", r"expected ';' in 'for' statement specifier"),
        ("expression_result_unused", r"expression result unused"),
        ("extra_tokens_at_end_of_include_directive", r"extra tokens at end of #include directive"),
        ("h_file_not_found", r"s.*o.h' file not found"),
        ("has_empty_body", r"has empty body"),
        ("ignoring_return_value_of_function", r"ignoring return value of function"),
        ("invalid_equal_equal_at_end_of_declaration", r"invalid '==' at end of declaration; did you mean '='"),
        ("invalid_preprocessing_directive", r"invalid preprocessing directive"),
        ("return_type_of_main_is_not_int", r"return type of 'main' is not 'int'"),
        ("multiple_unsequenced_modifications", r"multiple unsequenced modifications"),
        ("parameter_of_main", r" parameter o. 'main'"),
        ("relational_comparison_result_unused", r"relational comparison result unused"),
        ("result_of_comparison_against_a_string_literal_is_unspecified", r"result of comparison against a string literal is unspecified"),
        ("subscripted_value_is_not_an_array", r"subscripted value is not an array"),
        ("missing_function_return_type", r"type specifier missing, defaults to 'int'"),
        ("missing_parameter_type", r"type specifier missing, defaults to 'int'"),
        ("unknown_escape_sequence", r"warning: unknown escape sequence '\\ '"),
        ("using_the_result_of_an_assignment_as_a_condition_without_parentheses", r"using the result of an assignment as a condition without parenthese"),
        ("use_of_undeclared_identifier", r"use of undeclared identifier"),
        ("unknown_type_name_define", r"unknown type name 'define'"),
        ("unknown_type_name_include", r"unknown type name 'include'"),
        ("is_uninitialized_when_used_here", r"is uninitialized when used here"),
        ("is_uninitialized_when_used_within_its_own_initialization", r"is uninitialized when used within its own initialization"),
        ("void_function_should_not_return_a_value", r"void function '(.*)' should not return a value"),
        ("too_many_arguments_to_function_call", r"too many arguments to function call, expected (\d+), have (\d+)"),
        ("fgets_comparison_between_pointer_and_integer", r"comparison between pointer and integer \('char \*' and 'int'\)"),
        ("unknown_escape_sequence_specific", r"unknown escape sequence '\\(.)'")
    ]
]


# Explanation(
#     label="two_main_functions",
#     regex=r"multiple definition of \W*main\b",
#     explanation="Your program contains more than one main function - a C program can only contain one main function.",
#     reproduce="""\
# // hack to get 2 main functions compiled in separate files
# //dcc_flags=$src_file
# int main(void) {
# }
# """,
# ),
# Explanation(
#     label="no_main_function",
#     regex=r"undefined reference to \W*main\b",
#     explanation="Your program does not contain a main function - a C program must contain a main function.",
#     no_following_explanations=True,
#     reproduce="""\
# """,
# ),
# Explanation(
#     label="scanf_missing_ampersand",
#     regex=r"format specifies type '(?P<type>int|double) \*' but the argument has type '(?P=type)'",
#     explanation="Perhaps you have forgotten an '&' before '**{highlighted_word}**' on line {line_number} of {file}.",
#     reproduce="""\
# #include <stdio.h>

# int main(void) {
# int i = 0;
# scanf("%d", i);
# }
# """,
# ),
# Explanation(
#     label="format_type_mismatch",
#     regex=r"format specifies type '[^:]+' but the argument has type '[^:]+'",
#     explanation="make sure you are using the correct format code (e.g., `%d` for integers, `%lf` for floating-point values) in your format string on line {line_number} of {file}.",
#     reproduce="""\
# #include <stdio.h>

# int main(void) {
# printf("%d", "hello!");
# }
# """,
# ),
# Explanation(
#     label="missing_semicolon_line_before_assert",
#     regex=r"called object type 'int' is not a function or function pointer",
#     explanation="there is probably a syntax error such as missing semi-colon on line {int(line_number) - 1} of {file} or an earlier line",
#     precondition=lambda message, match: message.highlighted_word == "assert",
#     reproduce="""\
# #include <assert.h>

# int main(void) {
# int i = 10
# assert(i == 10);
# }
# """,
# ),
# Explanation(
#     label="assert_without_closing_parenthesis",
#     regex=r"unterminated function-like macro invocation",
#     explanation="it looks like there is a missing closing bracket on the assert on line {line_number} of {file}.",
#     precondition=lambda message, match: message.highlighted_word == "assert",
#     no_following_explanations=True,
#     show_note=False,
#     reproduce="""\
# #include <assert.h>

# int main(int argc, char *argv[]) {
# assert(argc == 1;
# }
# """,
# ),
# Explanation(
#     label="double_int_literal_conversion",
#     regex=r"implicit conversion from 'double' to 'int'",
#     explanation="you are assigning the floating point number **{highlighted_word}** to the int variable **{underlined_word}** , if this is what you want, change **{highlighted_word}** to **{truncate_number(highlighted_word)}**",
#     reproduce="""\
# int main(int argc, char *argv[]) {
# int i = 6.7;
# return i;
# }
# """,
# ),
# Explanation(
#     label="assign_to_multidimensional_array",
#     regex=r"array type .*?\]\[.* is not assignable",
#     explanation="""\
# you are trying to assign to '**{underlined_word}**' which is an array.
# You can not assign to a whole array.
# You can use a nested loop to assign to each array element individually.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# int a[3][1], b[3][1] = {0};
# a = b;
# }
# """,
# ),
# Explanation(
#     label="assign_to_array",
#     regex=r"array type .*?[^\]]\[(\d+)\]' is not assignable",
#     explanation="""\
# you are trying to assign to '**{underlined_word}**' which is an array with {match.group(1)} element{'s' if match.group(1) != '1' else ''}.
# You can not assign to a whole array.
# You can use a loop to assign to each array element individually.
# """,
#     long_explanation=True,
#     reproduce="""\
# int main(void) {
# int a[1], b[1] = {0};
# a = b;
# }
# """,
# ),
# Explanation(
#     label="stack_use_after_return",
#     regex=r"address of stack memory associated with local variable '(.*?)' returned",
#     explanation="""\
# you are trying to return a pointer to the local variable '**{highlighted_word}**'.
# You can not do this because **{highlighted_word}** will not exist after the function returns.
# """,
#     long_explanation=True,
#     reproduce="""\
# int *f(void) {
# int i;
# return &i;
# }
# int main(void){}
# """,
# ),
# Explanation(
#     label="assign_function_to_int",
#     regex=r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'.*\(",
#     explanation="""\
# you are attempting to assign **{underlined_word}** which is a function to an **{match.group(2)}** variable.
# Perhaps you are trying to call the function and have forgotten the round brackets and any parameter values.
# """,
#     long_explanation=True,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# int a = main;
# return a;
# }
# """,
# ),
# Explanation(
#     label="assign_array_to_int",
#     regex=r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'.*]'",
#     explanation="""\
# you are attempting to assign **{underlined_word}** which is an array to an **{match.group(2)}** variable.""",
#     reproduce="""
# int main(void) {
# int a[3][3] = {0};
# a[0][0] = a[1];
# }
# """,
# ),
# Explanation(
#     label="assign_pointer_to_int",
#     regex=r"incompatible pointer to integer conversion (assigning to|initializing) '(\w+)'",
#     explanation="""you are attempting to assign **{underlined_word}** which is not an **{match.group(2)}** to an **{match.group(2)}** variable.""",
#     reproduce="""
# int main(int argc, char *argv[]) {
# int a;
# a = &a;
# }
# """,
# ),
# Explanation(
#     label="missing_library_include",
#     regex=r"(implicitly declaring library function|call to undeclared library function) '(\w+)'",
#     explanation="""\
# you are calling **{match.group(2)}** on line {line_number} of {file} but
# dcc does not recognize **{match.group(2)}** as a function.
# Do you have {emphasize('#include <' + extract_system_include_file(note) + '>')} at the top of your file?
# """,
#     show_note=False,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# printf("hello");
# }
# """,
# ),
# Explanation(
#     label="misspelt_printf",
#     regex=r"(implicit declaration of|call to undeclared) function '(print.?.?)'",
#     explanation="""\
# you are calling a function named **{match.group(2)}** on line {line_number} of {file} but dcc does not recognize **{match.group(2)}** as a function.
# Maybe you meant **printf**?
# """,
#     no_following_explanations=True,
#     reproduce="""\
# #include <stdio.h>
# int main(int argc, char *argv[]) {
# print("hello");
# }
# """,
# ),
# Explanation(
#     label="implicit_function_declaration",
#     regex=r"(implicit declaration of function|call to undeclared function) '(\w+)'",
#     explanation="""\
# you are calling a function named **{match.group(2)}** line {line_number} of {file} but dcc does not recognize **{match.group(2)}** as a function.
# There are several possible causes:
# a) You might have misspelt the function name.
# b) You might need to add a #include line at the top of {file}.
# c) You might need to add a prototype for **{match.group(2)}**.
# """,
#     no_following_explanations=True,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# f();
# }
# """,
# ),
# Explanation(
#     regex=r"expression is not assignable",
#     explanation="""\
# you are using **=** incorrectly perhaps you meant **==**.
# Reminder: you use **=** to assign to a variable.
# You use **==** to compare values.
#     """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc = 1 || argc = 2) {
#     return 1;
# }
# }
# """,
# ),
# Explanation(
#     label="uninitialized-local-variable",
#     regex=r"'(.*)' is used uninitialized in this function",
#     explanation="""you are using the value of the variable **{match.group(1)}** before assigning a value to **{match.group(1)}**.""",
#     reproduce="""\
# int main(void) {
# int a[1];
# return a[0];
# }
# """,
# ),
# Explanation(
#     label="function-variable-clash",
#     regex=r"called object type .* is not a function or function pointer",
#     precondition=lambda message, match: re.match(r"^\w+$", message.underlined_word),
#     long_explanation=True,
#     explanation="""\
# '**{underlined_word}**' is the name of a variable but you are trying to call it as a function.
# If '**{underlined_word}**' is also the name of a function, you can avoid the clash,
# by changing the name of the variable '**{underlined_word}**' to something else.""",
#     reproduce="""\
# int main(void) {
# int main;
# return main();
# }
# """,
# ),
# Explanation(
#     regex=r"function definition is not allowed here",
#     precondition=lambda message, match: message.line_number
#     and int(message.line_number) > 1,
#     long_explanation=True,
#     explanation="""\
# there is likely a closing brace (curly bracket) missing before line {line_number} of {file}.
# Is a **} missing** in the previous function?""",
#     no_following_explanations=True,
#     reproduce="""\
# int f(int a) {
# return a;

# int main(void) {
# return f(0);
# }
# """,
# ),
# Explanation(
#     label="indirection-requires-pointer-operand",
#     regex=r"indirection requires pointer operand \('(.*)' invalid\)",
#     explanation="""\
# you are trying to use '**{underlined_word}**' as a pointer.
# You can not do this because '**{underlined_word}**' is of type **{match.group(1)}**.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# return *argc;
# }
# """,
# ),
# Explanation(
#     label="duplicated-cond",
#     regex=r"duplicated .*\bif\b.* condition",
#     explanation="""\
# you have repeated the same condition in a chain of if statements.
# Only the first if statement using the condition can be executed.
# The others can never be executed.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc == 1)
#     return 42;
# else if (argc == 1)
#     return 43;
# else
#     return 44;
# }
# """,
# ),
# Explanation(
#     regex=r"condition has identical branches",
#     explanation="""\
# your if statement has identical then and else parts.
# It is pointless to have an if statement which executes the same code
# when its condition is true and also when its condition is false.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc == 1)
#     return 42;
# else
#     return 42;
# }
# """,
# ),
# Explanation(
#     label="logical-or-always-true",
#     regex=r"logical .?\bor\b.* is always true|logical.*or.*of collectively exhaustive tests is always true|overlapping comparisons always evaluate to true",
#     explanation="""Your '**||**' expression is always true, no matter what value variables have.
# Perhaps you meant to use '**&&**' ?
# """,
#     reproduce="""
# int main(int argc, char *argv[]) {
# if (argc > 1 || argc < 3)
#     return 42;
# else
#     return 43;
# }
# """,
# ),
# Explanation(
#     label="logical-and-always-false",
#     regex=r"logical .?\band\b.* is always false|overlapping comparisons always evaluate to false",
#     explanation="""Your '**&&**' expression is always false, no matter what value variables have.
# Perhaps you meant to use '**||**' ?
# """,
#     reproduce="""
# int main(int argc, char *argv[]) {
# if (argc > 1 && argc < 1)
#     return 42;
# else
#     return 43;
# }
# """,
# ),
# Explanation(
#     label="logical-equal-expressions",
#     regex=r"logical .?((and|or)).? of equal expressions",
#     explanation="""you have used '**{highlighted_word}**' with same lefthand and righthand operands.
# If this what you meant, it can be simplified: **{'x ' + highlighted_word + ' x'}** can be replaced with just **x**.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc > 1 ||argc > 1)
#     return 42;
# else
#     return 43;
# }
# """,
# ),
# Explanation(
#     regex=r"declaration shadows a local variable",
#     explanation="""you already have a variable named '**{highlighted_word}**'.
# It is confusing to have a second overlapping declaration of the same variable name.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# {
#     int argc = 42;
#     return argc;
# }
# }
# """,
# ),
# Explanation(
#     label="nonnull",
#     regex=r"argument (\d+) null where non-null expected",
#     explanation="""\
# you are passing {extract_argument_variable(highlighted_word, match.group(1), emphasize)} as {emphasize('argument ' + match.group(1))} to '**{extract_function_name(highlighted_word)}**'.
# {emphasize('Argument ' + match.group(1))} to '**{extract_function_name(highlighted_word)}**' should never be NULL.
# """,
#     reproduce="""\
# #include <unistd.h>

# int main(void) {
# char *pathname = NULL;
# faccessat(0, pathname, 0, 0);
# }
# """,
# ),
# Explanation(
#     label="indexing_one_too_far",
#     regex=r"array index (\d+) is past the end of the array.*(which contains \1 element|\[\1\])",
#     explanation="""\
# remember arrays indices start at zero.
# The valid array indices for an array of size n are 0..n-1.
# For example, for an array of size 10 you can use 0..9 as indices.
# """,
#     reproduce="""\
# int main(void) {
# int a[42] = { 0 };
# return a[42];
# }
# """,
# ),
# Explanation(
#     regex=r"array subscript is not an integer",
#     precondition=lambda message, match: '"' in message.highlighted_word,
#     explanation="""\
# you are using a string as an array index. An array index has to be an integer.
# """,
#     reproduce="""\
# int main(void) {
# int a[1] = { 0 };
# return a["0"];
# }
# """,
# ),
# Explanation(
#     regex=r"continue.* statement not in loop",
#     explanation="""\
# **continue** statements can only be used inside a while or for loop.
# Check the braces {{}} are correct on nearby statements.
# """,
#     reproduce="""\
# int main(void) {
# continue;
# }
# """,
# ),
# Explanation(
#     regex=r"break.* statement not in loop",
#     explanation="""\
# **break** statements can only be used inside a while loop, for loop or switch.
# Check the braces **{{}}** are correct on nearby statements.
# """,
#     reproduce="""\
# int main(void) {
# break;
# }
# """,
# ),
# Explanation(
#     label="non_void_function_does_not_return_a_value_in_all_control_paths",
#     regex=r"non-void function does not return a value in all control paths",
#     explanation="""\
# Your function contains a **return** but it is possible for execution
# to reach the end of the function without a **return** statment being executed.
# """,
#     reproduce="""\
# int f(int a) {
# if (a) {
#     return 1;
# }
# }
# int main(int argc, char *argv[]) {
# f(argc);
# }
# """,
# ),
# Explanation(
#     label="non_void_function_does_not_return_a_value",
#     regex=r"non-void function does not return a value \[",
#     explanation="""\
# your function has no **return** statement.
# Unless a function is of type void, it must return a value using a **return** statement.
# """,
#     reproduce="""\
# int f(int a) {
# }
# int main(int argc, char *argv[]) {
# f(argc);
# }
# """,
# ),
# Explanation(
#     regex=r"data argument not used by format string",
#     explanation="""\
# you have more argument values than % codes in the format string.
# You need to change the format string or change the number of arguments.
# """,
#     reproduce="""\
# #include <stdio.h>

# int main(void) {
# printf("%d %d", 27, 28, 29);
# }
# """,
# ),
# Explanation(
#     regex=r"more '%' conversions than data arguments",
#     explanation="""\
# you have less argument values than % codes in the format string.
# You need to change the format string or change the number of arguments.
# """,
#     reproduce="""\
# #include <stdio.h>

# int main(void) {
# printf("%d %d %d %d", 27, 28, 29);
# }
# """,
# ),
# Explanation(
#     regex=r"expected ';' in 'for' statement specifier",
#     explanation="""\
# the three parts of a '**;**' statment should be separated with '**;**'
# """,
#     reproduce="""\
# int main(void) {
# for (int i = 0; i < 10 i++) {
# }
# }
# """,
# ),
# Explanation(
#     regex=r"expression result unused",
#     explanation="""\
# you are doing nothing with a value on line {line_number} of {file}.
# Did you mean to assign it to a varable?
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# argc;
# }
# """,
# ),
# Explanation(
#     regex=r"extra tokens at end of #include directive",
#     precondition=lambda message, match: ";"
#     in "".join(message.text_without_ansi_codes),
#     explanation="""\
# you have unnecessary characters on your #include statement.
# Remember #include statements don't need a '**;**'.
# """,
#     reproduce="""\
# #include <stdio.h>;
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"extra tokens at end of #include directive",
#     explanation="""\
# you have unnecessary characters on your #include statement.
# """,
#     reproduce="""\
# #include <stdio.h>@
# int main(void) {
# }
# """,
# ),
# Explanation(
#     label="h_file_not_found",
#     regex=r"s.*o.h' file not found",
#     explanation="""\
# you are attempting to #include a file which does not exist.
# Did you mean: '**#include <stdio.h>**'
# """,
#     reproduce="""\
# #include <studio.h>
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"has empty body",
#     precondition=lambda message, match: ";"
#     in "".join(message.text_without_ansi_codes),
#     explanation="""\
# you may have an extra '**;**' that you should remove.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc); {
# }
# }
# """,
# ),
# Explanation(
#     regex=r"ignoring return value of function",
#     explanation="""\
# you are not using the value returned by function **{highlighted_word}** .
# Did you mean to assign it to a variable?
# """,
#     reproduce="""\
# #include <stdlib.h>
# int main(int argc, char *argv[]) {
# atoi(argv[0]);
# }
# """,
# ),
# Explanation(
#     label="ignoring_return_value_of_function",
#     regex=r"ignoring return value of function",
#     explanation="""\
# you are not using the value returned by function **{highlighted_word}** .
# Did you mean to assign it to a variable?
# """,
#     reproduce="""\
# #include <stdlib.h>
# int main(int argc, char *argv[]) {
# atoi(argv[0]);
# }
# """,
# ),
# Explanation(
#     label="invalid_equal_equal_at_end_of_declaration",
#     regex=r"invalid '==' at end of declaration; did you mean '='",
#     explanation="""\
# remember '**=**' is used to assign a value to a variable, '**==**' is used to compare values, 
# """,
#     reproduce="""\
# int main(void) {
# int i == 0;
# }
# """,
# ),
# Explanation(
#     regex=r"invalid preprocessing directive",
#     explanation="""\
# you have an invalid line begining with '**#**'.
# Did you mean **#include** or **#define ** ? 
# """,
#     reproduce="""\
# #inclde <stdio.h>
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"return type of 'main' is not 'int'",
#     explanation="""\
# '**main**' must always have return type **int**.
# """,
#     reproduce="""\
# void main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"multiple unsequenced modifications",
#     explanation="""\
# you are changing a variable multiple times in the one statement. 
# **`++`** and **`--`** change the variable, there is no need to also assign the result to the variable.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# argc = argc--;
# }
# """,
# ),
# Explanation(
#     regex=r" parameter o. 'main'",
#     explanation="""\
# your declaration of '**main**' is incorrect.
# Try either '**int main(void)**' or '**int main(int argc, char *argv[])**'
# """,
#     reproduce="""\
# int main(int argc) {
# }
# """,
# ),
# Explanation(
#     regex=r"relational comparison result unused",
#     precondition=lambda message, match: ","
#     in "".join(message.text_without_ansi_codes),
#     explanation="""\
# you appear to be combining combining comparison incorrectly. 
# Perhaps you are using '**,**' instead of '**&&**' or '**||**'.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# return argc < 0, argc < 23;
# }
# """,
# ),
# Explanation(
#     regex=r"result of comparison against a string literal is unspecified",
#     explanation="""\
# you can not compare strings with '<', '>' etc.
# 'string.h' has functions which can compare strings, e.g. '**strcmp**'
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# return argv[0] < "";
# }
# """,
# ),
# Explanation(
#     regex=r"subscripted value is not an array",
#     explanation="""\
# you appear to be incorrectly trying to use **{underlined_word}** as an array .
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# return argc[0];
# }
# """,
# ),
# Explanation(
#     label="missing_function_return_type",
#     regex=r"type specifier missing, defaults to 'int'",
#     precondition=lambda message, _: re.search(
#         rf"\b{message.highlighted_word}\s*\(", "".join(message.text_without_ansi_codes)
#     ),
#     explanation="""\
# have you given a return type for **{highlighted_word}**?
# You must specify the return type of a function just before its name.
# """,
#     reproduce="""\
# square (int x) {
# return 1;
# }
# int main(void) {
# return square(0);
# }
# """,
# ),
# Explanation(
#     label="missing_parameter_type",
#     regex=r"type specifier missing, defaults to 'int'",
#     precondition=lambda message, _: not re.search(
#         rf"\b{message.highlighted_word}\s*\(", "".join(message.text_without_ansi_codes)
#     ),
#     explanation="""\
# have you given a type for **{highlighted_word}**?
# You must specify the type of each function parameter.
# """,
#     reproduce="""\
# int add(int b, c) {
# return 1;
# }
# int main(void) {
# return add(1, 2);
# }
# """,
# ),
# Explanation(
#     regex=r" warning: unknown escape sequence '\\ '",
#     precondition=lambda message, match: "\\ n"
#     in "".join(message.text_without_ansi_codes),
#     explanation="""\
# you have a space after a backslash which is not permitted. 
# Did you mean '\\\\n'?
# """,
#     reproduce="""\
# int main(void) {
# return "\\ n"[0];
# }
# """,
# ),
# Explanation(
#     regex=r" warning: unknown escape sequence '\\ '",
#     explanation="""\
# you have a space after a backslash which is not permitted. 
# """,
#     reproduce="""\
# int main(void) {
# return "\\ "[0];
# }
# """,
# ),
# Explanation(
#     regex=r"using the result of an assignment as a condition without parenthese",
#     explanation="""\
# you use '**=**' to assign to a variable, you use '**==**' to compare values.
# """,
#     reproduce="""\
# int main(int argc, char *argv[]) {
# if (argc = 4) {
#     return 1;
# }
# }
# """,
# ),
# Explanation(
#     regex=r"use of undeclared identifier",
#     explanation="""\
# you have used the name '**{highlighted_word}**' on line {line_number} of {file} without previously declaring it.
# If you meant to use '**{highlighted_word}**' as a variable, check you have declared it by specifying its type
# Also  check you have spelled '**{highlighted_word}**' correctly everywhere.
# """,
#     reproduce="""\
# int main(void) {
# return x;
# }
# """,
# ),
# Explanation(
#     regex=r"unknown type name 'define'",
#     explanation="""\
# you appear to have left out a '#'.
# Use #**define** to define a constant, for example: #define PI 3.14159
# """,
#     reproduce="""\
# define X 42
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"unknown type name 'include'",
#     explanation="""\
# you appear to have left out a '#'.
# Use #**include** to include a file, for example: #include <stdio.h>
# """,
#     reproduce="""\
# define X 42
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"is uninitialized when used here",
#     explanation="""\
# you are using variable '**{highlighted_word}**' before it has been assigned a value.
# Be sure to assign a value to '**{highlighted_word}**' before trying to use its value.
# """,
#     reproduce="""\
# int main(void) {
# int x;
# }
# """,
# ),
# Explanation(
#     regex=r"is uninitialized when used within its own initialization",
#     explanation="""\
# you are using variable '**{highlighted_word}**' as part of its own initialization.
# You can not use a variable to initialize itself.
# """,
#     reproduce="""\
# int main(void) {
# int x;
# }
# """,
# ),
# Explanation(
#     regex=r"void function '(.*)' should not return a value",
#     explanation="""\
# you are trying to **return** a value from function **{match.group(1)}** which is of type **void**.
# You need to change the return type of **{match.group(1)}** or change the **return** statement.
# """,
#     reproduce="""\
# void f(void) {
# return 1;
# }
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"void function '(.*)' should not return a value",
#     explanation="""\
# you are trying to **return** a value from function **{match.group(1)}** which is of type **void**.
# You need to change the return type of **{match.group(1)}** or change the **return** statement.
# """,
#     reproduce="""\
# void f(void) {
# return 1;
# }
# int main(void) {
# }
# """,
# ),
# Explanation(
#     regex=r"too many arguments to function call, expected (\d+), have (\d+)",
#     explanation="""\
# function **{underlined_word+"()"}** takes **{match.group(1)}** arguments but you have given it **{match.group(2)}** arguments.
# """,
#     reproduce="""\
# #include <stdio.h>
# int main(void) {
# return getchar(0, 0, 0);
# }
# """,
# ),
# Explanation(
#     precondition=lambda message, match: message.underlined_word.startswith(
#         "fgets("
#     ),
#     regex=r"comparison between pointer and integer \('char \*' and 'int'\)",
#     explanation="""\
# **fgets** returns a pointer. Compare it to **NULL** to detect **fgets** being unable to read a line.
# """,
#     reproduce="""\
# #include <stdio.h>
# int main(void) {
# char a[16];
# return fgets(a, sizeof a, stdin) == EOF;
# }
# """,
# ),
# Explanation(
#     regex=r"unknown escape sequence '\\(.)'",
#     explanation="""\
# if you want an actual backslash in your string use **{BACKSLASH * 2}**
# """,
#     reproduce="""\
# int main(void) {
# return (int)"\\_/";
# }
# """,
# ),

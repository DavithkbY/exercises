# Assignment

You are given a file `input.txt`. You can imagine this is Python source code.
Your task is to find all strings in this file and print them out in order, one string per line.

* A string is delimited by `"`.
* A string always starts and ends on the same line.
* One line can contain multiple strings.
* A string can contain escaped quotes: for example `"He said \"Hello\"."` represents `He said "Hello"`.
  These escaped quotes must appear as regular quotes in the output, e.g., `\"x\"` must become `"x"`.
* Escaped quotes only appear within strings.

Write your output to `output.txt`.

## Example

See `example-input.txt` and `example-output.txt`.

# Assignment

You are given a text file `input.txt`.
Each line of the form

```text
== Some text
```

should be transformed to

```text
Some text
=========
```

The results must be written in a file `output.txt`.

Exact rules:

* The line must start with exactly two equal signs followed by a space for the transformation rule to apply.
* The number of generated `=` must be exactly as long as the text it's under.
* Lines not starting with `"== "` must be preserved.

## Examples

See `example-input.txt` and `example-output.txt`.

## Hints

* Using the Python shell, find out what `"a" * 5` does.

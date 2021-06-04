# Assignment

`previous.txt` and `current.txt` both contain the same names but in a different order and represent a ranking.
Write a script that produces a file `output.txt` with the same ranking as `current.txt`, but where each name is suffixed with the change in rank.

## Rules

* When someone moves up, add `(+N)` after the name, where `N` is the number of places (s)he moved up.
* If someone's rank remained the same, add `(=)`.
* When someone moves down, add `(-N)` with `N` the number of places (s)he dropped.

## Example 1

Say that `previous.txt` contains

```text
Darren Aronofsky
Sergio Leone
Rian Johnson
Paul Thomas Anderson
Denis Villeneuve
```

and `current.txt` contains

```text
Paul Thomas Anderson
Sergio Leone
Denis Villeneuve
Rian Johnson
Darren Aronofsky
```

Your script should then generate a file `output.txt` with as contents

```text
Paul Thomas Anderson (+3)
Sergio Leone (=)
Denis Villeneuve (+2)
Rian Johnson (-1)
Darren Aronofsky (-4)
```

Paul was ranked 4th in `previous.txt` and moved up to #1 in `current.txt`, hence the `+3` in `output.txt`.
Sergio remained in second place, so he gets a `=`, and so on.

## Example 2

See `example-previous.txt`, `example-current.txt` and `example-output.txt`.

## Hints

* Focus first on ranking the names in `previous.txt`. Build a dictionary that associates name with ranking.
  Next, while going through `current.txt`, you can consult this dictionary to quickly determine the old ranking.
* If you're having trouble solving this problem, you can trivially make your own small input set and check manually.
  Once your script works on your small input set, it should also work on the given one.

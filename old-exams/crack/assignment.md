# Assignment

## Hash Functions

For this problem, we will make use of *hash functions*,
more specifically the hash function named SHA256.
It is included in Python's standard library,
so a good first step would be to look up how to hash strings
using SHA256 in Python 3.

**Note:** you'll probably encounter the error
`TypeError: Unicode-objects must be encoded before hashing`
if you try to hash a string directly.
Strings must first be converted to raw bytes:
use `string.encode('UTF-8')` to achieve this.

## Task

There are 100,000 students, each having a unique id of the form `rXXXXXXX` with each `X` a decimal digit.
Each student has a password.

For security reasons, passwords are never stored directly in a database.
Instead, we have stored their SHA256 hash, written in hexadecimal.

You are given two files:

* `hashed.txt` contains the password hashes for each student.
  * The first column contains the student id.
  * The second column contains the SHA256-hash (hexadecimal) of the student's password.
* `dictionary.txt` contains all the (unhashed) passwords.

Write a script that, for each student, finds his/her password.
In other words, you need to find a password from `dictionary.txt` whose
SHA256 hash equals the value in `hashed.txt`.

Write your results to `output.txt`.

* Each line must be formatted `rXXXXXXX PASSWORD`.
* The student ids must appear in the same order as in `hashed.txt`.

## Example

Say there are three students.

<center>

|Id|Password|Hash|
|-|:-:|:-:|
|`r0000001`|`qwerty`|`65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5`|
|`r0000002`|`PASSWORD`|`0be64ae89ddd24e225434de95d501711339baeee18f009ba9b4369af27d30d60`|
|`r0000003`|`12345678`|`ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f`|

</center>

In this case, `hashed.txt` would contain

```text
r0000001 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
r0000002 0be64ae89ddd24e225434de95d501711339baeee18f009ba9b4369af27d30d60
r0000003 ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f
```

and `dictionary.txt` would contain

```text
`12345678`
`PASSWORD`
`qwerty`
```

Your script should produce, based on these two files, the following `output.txt`:

```text
r0000001 qwerty
r0000002 PASSWORD
r0000003 12345678
```

== Advice

Make sure you're using SHA256 correctly.
Start with looking up online how to use SHA256 and check that
you get the same hash values as shown in the above examples.

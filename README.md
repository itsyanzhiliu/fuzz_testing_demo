# Demo for Fuzz Testing
**High level algorithm**: 

1. Use one or multiple valid URL strings as seed inputs
2. Randomly mutate the seed inputs to obtain various mutated input strings
3. Evaluate those input strings and obtain their line coverage
4. Select input strings with many new, uncovered lines as seed inputs.
5. Repeat until cannot obtain new coverage for some number of consecutive iterations.


**The Fuzzer**: The fuzzer will take as input an executable program (given as a string indicating the full path of the file) and output 2 lines: the first is a nonnegative number indicating the number of explored statements and the second is a sorted, comma-separated list of unique id's of statements that were covered.

```
$ ./fuzzer.exe /path/to/test.exe
1000
test.c:1, test.c:2,  ...  test.c:1000
```

The fuzzer also takes as input an argument `-show`, and outputs (e.g., at iteration X, the fuzzer generated Y inputs and covered Z unique lines).

```
$./fuzzer.exe /path/to/test.exe -show
....  # some progress
1000
test.c:1, test.c:2,  ...  test.c:1000
```

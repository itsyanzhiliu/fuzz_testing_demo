# Demo for Fuzz Testing
**High level algorithm**: 

1. Use one or multiple valid URL strings as seed inputs
2. Randomly mutate the seed inputs to obtain various mutated input strings
3. Evaluate those input strings and obtain their line coverage
4. Select input strings with many new, uncovered lines as seed inputs.
5. Repeat until cannot obtain new coverage for some number of consecutive iterations.

## Instruction
### Install GCC
If you don't have GCC installed, you'll need to install it. The installation steps depend on your operating system.

Linux: On most Linux distributions, you can use your package manager to install GCC. For example, on Ubuntu or Debian, you can run:
```
sudo apt-get update
sudo apt-get install gcc
```
Windows: If you're using Windows, you can install GCC by installing a package like MinGW or Cygwin.

### Update PATH

- Linux: You typically don't need to do anything, as the package manager handles adding paths to the system environment.

- Windows: If you're on Windows, you'll need to manually add the directory containing the gcc executable to the PATH. 


### Conpile and Run
```
$ gcc --coverage -o test.exe test.c
$ ./test.exe 'Send+mail+to+me%40unl.edu'
```

### Test Program

The input executable test program (e.g., test.exe) is a CGI decoder (discussed in class), which takes as input a string CGI encoded string (e.g., a URL, web address) and convert it to the original string before the encoding.

```
$ ./test.exe "Hello+World"
Hello World
```

### Coverage Information

```
$ gcov test.exe.c   # generate the .gcov file
$ less test.exe.c.gcov    # your fuzzer will parse in this file and analyze its contents
```


### Output
The fuzzer will take as input an executable program (given as a string indicating the full path of the file) and output 2 lines: the first is a nonnegative number indicating the number of explored statements and the second is a sorted, comma-separated list of unique id's of statements that were covered.

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


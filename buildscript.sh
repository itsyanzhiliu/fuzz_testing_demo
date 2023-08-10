#!/bin/bash

# Copy and rename fuzzer.py
cp fuzzer.py fuzzer.exe

# Copy and rename test.py
cp test.py test.exe

# Make the executables executable
chmod +x fuzzer.exe
chmod +x test.exe

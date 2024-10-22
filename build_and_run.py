#! /usr/bin/env python3
import os, sys
filename = "main.cpp"
filetype = "cpp"

# Handling Command-line Arguments
if len(sys.argv) > 1:
    if len(sys.argv) == 2: # One argument
        filename = sys.argv[1]
    elif len(sys.argv) == 3: # Two arguments
        filename = sys.argv[1]
        if sys.argv[2] == "c" or sys.argv[2] == "cpp":
            filetype = sys.argv[2]
        else:
            print(f"Invalid filetype \"{sys.argv[2]}\"!")
            sys.exit(1)
    else: # More than two arguments
        print("Too many arguments!")
        sys.exit(1)

if "/" in filename: # Path as filename.
    print("Please run the script at the directory of the source code instead of providing the path.")
    sys.exit(1)

if not os.path.isfile(filename): # File doesn't exist.
    print(f"File \"{filename}\" does not exist here!")
    sys.exit(1)

if not filename.endswith(f".{filetype}"):
    print(f"WARN: Filename \"{filename}\" does not match the filetype \"{filetype}\"!")

if os.path.isfile("bar.out"): # Remove previous build.
    os.remove("bar.out")

if filetype == "cpp":
    os.system(f"g++ {filename} -o bar.out")
else:
    os.system(f"gcc {filename} -o bar.out")

if not os.path.isfile("bar.out"): # Didn't compile successfully
    print("Compilation failed.")
    sys.exit(1)

os.system("./bar.out")

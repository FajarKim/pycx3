"""
pycx3 Compiler CLI Tool

This tool provides a command-line interface for compiling and
running Python version 3 source files using Cython.

Copyright (c) 2024 Rangga Fajar Oktariansyah.
All rights reserved.

Note:
  This tool is designed to work with Python 3.8 and above.

Usage:
  pycx3 source_file.py  # Compile the specified Python source file.

For more information and updates, visit: https://github.com/FajarKim/pycx3
"""

import subprocess
import sys
from typing import Tuple
from .compile import compile as compile_

def parse_args() -> Tuple[str, list]:
    """
    Parse command-line arguments.

    Returns:
        Tuple[str, list]: A tuple containing the source file path and remaining command-line arguments.
    """
    if len(sys.argv) < 2:
        RED = "\033[91m"
        ENDC = "\033[0m"
        # Print error message and exit if no input files are provided.
        print(f"pycx3: {RED}fatal error:{ENDC} no input files")
        print("compilation terminated.")
        sys.exit(-1)
    sys.argv.pop(0)
    source_file = sys.argv.pop(0)
    return source_file, sys.argv

def compile() -> None:
    """
    Command-line interface for compilation.

    Exits with the return code from the compilation process.
    """
    source_file, _ = parse_args()
    return_code, _ = compile_(source_file)
    sys.exit(return_code)

def compile_and_run() -> int:
    """
    Compile and run the specified source file.

    Returns:
        int: The return code from the compilation and execution process.
    """
    source_file, argv = parse_args()
    return_code, executable = compile_(source_file)
    if return_code == 0:
        # Construct the command to execute the compiled file.
        command = ["./" + executable] + argv
        return_code = subprocess.check_call(command)
    return return_code

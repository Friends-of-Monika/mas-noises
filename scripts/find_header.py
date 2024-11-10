#!/usr/bin/env python3
#pylint: skip-file

# This script performs simple submod header detection in RenPy scripts
# which is expected to change in the upcoming Submod Framework overhaul.
#
# Usage:
#   $ python find_header.py find <path to directory with .rpy scripts>
#     - looks for header structures in the directory and prints them out
#
#   OR
#
#   $ python find_header.py header <path to .rpy file>
#     - looks for header structure in just one file and prints it out
#
# Output format:
#   Errors are printed in human-readable format to stderr, outputs are printed
#   to stdout in JSON format.
#
# Error codes:
#   1 - invalid arguments
#   2 - error has occured
#
# Author:
#   dreamscached <dreamscache.d@gmail.com>


import tokenize
import argparse
import pathlib
import json
import sys
import re
import os


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    find = commands.add_parser("find")
    find.add_argument("path", type=pathlib.Path)
    header = commands.add_parser("header")
    header.add_argument("path", type=pathlib.Path)
    args = parser.parse_args()

    if args.command == "find":
        find_headers(args)
    elif args.command == "header":
        print_header(args)


def find_headers(args):
    if not args.path.is_dir():
        print("error: expected path to be a directory", file=sys.stderr)
        exit(1)

    rpy_files = (
        os.path.join(cd, path)
        for cd, _, files in os.walk(args.path)
        for path in files
        if path.endswith(".rpy")
    )

    headers = dict(map(lambda p: (p, get_header(p)), rpy_files))
    headers = dict(((k, v) for k, v in headers.items() if v))

    json.dump(headers, sys.stdout)
    exit(0)


def print_header(args):
    if not args.path.is_file():
        print("error: expected path to be a file", file=sys.stderr)
        exit(1)

    header = get_header(args.path)
    if not header:
        print("error: script file contains no header", file=sys.stderr)
        exit(2)

    json.dump(header, sys.stdout)
    exit(0)


def get_header(path):
    with open(path, "r") as f:
        # Load tokens from the token stream into list
        tokens = list(tokenize.generate_tokens(f.readline))

    must_have = ("name", "version")
    header = dict()
    curr_key = None

    # Here's a VERY basic FSM that scans the entire list of tokens
    # and locates the must_have identifiers and assigned strings
    # (other types are ignored, format/byte/unicode string prefixes
    # are supported and work too.)

    state = 0
    for t, s, *_ in tokens:

        if state == 0: # initial state
            if t == tokenize.NAME and s == "Submod":
                state = 1
            # else: state = 0

        elif state == 1: # found Submod token
            if t == tokenize.OP and s == "(":
                state = 2
            else:
                state = 1

        elif state == 2: # found opening bracket
            if t == tokenize.NAME and s in must_have:
                curr_key = s
                state = 3

            elif t == tokenize.OP and s == "(":
                state = 5

            elif t == tokenize.OP and s == ")":
                state = 1
            # else: state = 2

        elif state == 5: # found opening bracket inside Submod(...)
            # Added this as a quickfix because otherwise state = 2
            # would break upon hitting a bracket inside
            if t == tokenize.OP and s == ")":
                state = 2

        elif state == 3: # found an identifier
            if t == tokenize.OP and s == "=":
                state = 4
            else:
                state = 2

        elif state == 4: # found the equals sign
            if t == tokenize.STRING:
                if re.search('^[fbu]', s, re.I):
                    s = s[1:]
                header[curr_key] = s[1:-1]
            state = 2

    if all((k in header for k in must_have)):
        return header
    return None


if __name__ == "__main__":
    main()
#!python3
import sys
import argparse


def create_parser():
    """
    Arguments parser helper
    """
    parse = argparse.ArgumentParser()

    parse.add_argument("-s", "--size", type=int, required=True, help="size in megabytes (if -g, then gigabytes)")
    parse.add_argument("-f", "--file", required=True, help="file name")
    parse.add_argument("-g", "--gigabytes", action='store_const', const=True, default=False)

    return parse

parser = create_parser()
ns = parser.parse_args()

if (ns.size < 1) or (ns.size > 9999999):
    print("Invalid parameter! Allowed only the numbers 1 to 9999999")
    sys.exit(1)

size = ns.size
if ns.gigabytes:
    size *= 1024

f=open(ns.file, "w")
f.seek(1024 * 1024 * size)
f.write("\0")

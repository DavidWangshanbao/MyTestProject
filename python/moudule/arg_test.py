#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  argparse

parser = argparse.ArgumentParser(description="this is my  test argparse module")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--version", help="input your version")
args = parser.parse_args()
if args.version:
        print "version is {}".format(args.version)



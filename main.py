#!/usr/bin/env python3.9

from Matching.Parser import Parser

import pathlib

pars = Parser(pathlib.Path("/tmp/example.json"))

print(pars.parse())

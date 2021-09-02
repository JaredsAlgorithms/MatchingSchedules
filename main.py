#!/usr/bin/env python3.9

from Matching.Parser import Parser
from Matching.Scheduler import Scheduler

import pathlib

pars = Parser(pathlib.Path("inputs/example.json"))
_schedule = Scheduler()

# person1, person2 = pars.parse()

duration, [person1, person2] = pars.parse()

_schedule.mergeSchedules(duration, person1, person2)

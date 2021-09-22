#!/usr/bin/env python3.9

from Matching.Parser import Parser
from Matching.Scheduler import Scheduler
from Matching.TimeSlot import TimeSlot

import pathlib


def main(path: str):
    pars = Parser(pathlib.Path(path))
    _schedule = Scheduler()

    duration, [person1, person2] = pars.parse()

    resultant = _schedule.mergeSchedules(person1, person2)
    intervals = _schedule.dispenseTimes(resultant)

    for interval in intervals:
        begin, end = interval
        obj = TimeSlot.from_datetime(begin, end)
        interval_duration = abs(begin - end).total_seconds()
        if(duration > interval_duration):
            continue
        print(
            f'{obj.begin.strftime("%H:%M")} -> {obj.end.strftime("%H:%M")}')


main("inputs/01.json")
# print()
# main("inputs/02.json")

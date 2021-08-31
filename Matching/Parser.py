import json
import pathlib

from Matching.Entity import Entity
from Matching.TimeSlot import TimeSlot


class Parser:
    def __init__(self, path: pathlib.Path):
        if not(path.is_file()):
            raise FileNotFoundError
        self.path = path

    def parse(self) -> list[Entity]:
        with open(self.path, "r") as fp:
            contents = json.load(fp)

        person_container = []
        for candidate, information in contents["people"][0].items():
            container = []
            working_schedule = information['workingSchedule']
            # start of day, end of day
            SOD, EOD = information['dailyActivities']

            for begin, end in working_schedule:
                container.append(TimeSlot(begin, end))

            # add fringe cases
            container.append(TimeSlot(EOD, '23:59'))
            container.insert(0, TimeSlot('00:00', SOD))

            person_container.append(Entity(candidate, container, [
                container[0], container[-1]]))

        return person_container

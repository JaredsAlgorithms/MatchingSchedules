import json
import pathlib

from Matching.Entity import Entity
from Matching.TimeSlot import TimeSlot


class Parser:
    def __init__(self, path: pathlib.Path):
        if not(path.is_file()):
            raise FileNotFoundError
        self.path = path

    def parse(self) -> tuple[int, list[Entity]]:
        with open(self.path, "r") as fp:
            contents = json.load(fp)

        person_container = []
        duration = contents["meetingDuration"]

        for candidate, information in contents["people"][0].items():
            container = []
            working_schedule = information['workingSchedule']
            # start of day, end of day
            SOD, EOD = information['dailyActivities']

            for begin, end in working_schedule:
                availability = (
                    False if(begin < SOD) else True,
                    False if(end > EOD) else True
                )
                container.append(
                    TimeSlot(begin, end, availability))

            # add fringe cases
            container.append(TimeSlot(EOD, '23:59', (False, False)))
            container.insert(0, TimeSlot('00:00', SOD, (False, False)))

            person_container.append(Entity(candidate, container, [
                container[0], container[-1]]))

        return (duration, person_container)

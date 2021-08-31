from Matching.TimeSlot import TimeSlot


class Entity:
    def __init__(self, name: str, schedule: list[TimeSlot], unavailable: list[TimeSlot]):
        self.name = name
        self.schedule = schedule
        self.unavailable = unavailable

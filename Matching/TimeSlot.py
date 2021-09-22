import datetime


class TimeSlot:
    def __init__(self, begin: str, end: str, available: bool):
        if not(isinstance(begin, str) and
               isinstance(end, str) and
               isinstance(available, tuple)):
            raise ValueError

        self.begin = datetime.datetime.strptime(begin, '%H:%M')
        self.end = datetime.datetime.strptime(end, '%H:%M')
        self.available = available

    @classmethod
    def from_datetime(cls, begin: datetime.datetime, end: datetime.datetime):
        cls.begin = begin
        cls.end = end
        cls.available = True
        return cls

    def __repr__(self):
        return f"""
{self.begin.strftime('%H:%M')} -> {self.end.strftime('%H:%M')} [ {self.time_elapsed()} hr(s) ]
        """

    def time_elapsed(self):
        """ Return length of time from beginning to end """

        return (self.end - self.begin)

    def __eq__(self, other):
        return (
            (self.begin == other.begin) and
            (self.end == other.end)
        )

    def __hash__(self):
        return hash(self.begin) + hash(self.end)

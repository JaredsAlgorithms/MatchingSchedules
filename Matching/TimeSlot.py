import datetime


class TimeSlot:
    def __init__(self, begin: str, end: str):
        if not(isinstance(begin, str) and
               isinstance(end, str)):
            raise ValueError

        self.begin = datetime.datetime.strptime(begin, '%H:%M')
        self.end = datetime.datetime.strptime(end, '%H:%M')

    def __repr__(self):
        return f"""
{self.begin.strftime('%H:%M')} -> {self.end.strftime('%H:%M')} [ {self.time_elapsed()} hr(s) ]
        """

    def time_elapsed(self):
        """ Return length of time from beginning to end """

        return (self.end - self.begin)

    def as_seconds(self):
        return self.time_elapsed().total_seconds()

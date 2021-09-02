class Scheduler:
    def __init__(self):
        pass

    def mergeSchedules(self, duration, person1, person2):
        """
        Given the duration of the meeting and both parties schedules:
        Return a list of times that DO NOT work for either party
        """
        [min1, max1], [min2, max2] = person1.unavailable, person2.unavailable

        for schedule1, schedule2 in zip(person1.schedule, person2.schedule):
            if not(schedule1.available or schedule2.available):
                # these are fringe cases, do not add to list of times to consider
                continue
            # interested in the ending of the first schedule and beginning of the second one
            s1, e1 = schedule1.begin, schedule1.end
            s2, e2 = schedule2.begin, schedule2.end

            lhs = abs(s1 - s2).total_seconds()

            print(f"time remaining before the meeting: {lhs // 60}")

            rhs = abs(e1 - e2).total_seconds()

            print(f"time remaining after the meeting: {rhs}")

            # if((end <= begin) and (duration <= time_between)):
            # print("something")
            # else:
            # print("this time slot will not work:")
            # print(end, begin)

    # def mergedSchedules(self, duration, person1, person2):
        # i, j = 0, 0
        # schedule1Amount, schedule2Amount = len(
            # person1.schedule), len(person2.schedule)

        # while((i < schedule1Amount) and (j < schedule2Amount)):
            # meeting1, meeting2 = person1.schedule[i], person2.schedule[j]
            # if

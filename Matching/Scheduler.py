from Matching.TimeSlot import TimeSlot
from Matching.Stack import Stack


class Scheduler:
    def combineSchedules(self, person1, person2) -> list:
        """
        Remove duplicate time intervals
        """

        a, b = len(person1.schedule), len(person2.schedule)

        # True: person1
        # False: person2

        _info = (
            False if a < b else True,
            abs(a - b)
        )
        container = []
        for schedule1, schedule2 in zip(person1.schedule, person2.schedule):
            if(schedule1 not in container):
                container.append(schedule1)
            if(schedule2 not in container):
                container.append(schedule2)

        # make sure you add the contents of the larger schedule into the container
        if(a != b):
            __which_container, index = _info
            person = person1 if(__which_container) else person2
            for value in person.schedule[index:]:
                if(value not in container):
                    container.append(value)

        container.sort(key=lambda x: x.begin)  # O(n * log(n)) time complexity
        return container

    def mergeSchedules(self, person1, person2):
        """
        Input: pre-sorted container
        Return a range of times that possibly work for each party
        """

        # NOTE: this project pulls from this solution from LeetCode:
        # https://leetcode.com/problems/merge-intervals/solution/
        # smaller time intervals will be combined into one contiguous interval
        # I wanted to be creative and use a stack instead of a pure list

        # assumes result is not a n empty list
        result = self.combineSchedules(person1, person2)
        if not(result):
            return []

        _Stack = Stack()
        _Stack.push(result[0])

        for slot in result[1:]:
            top = _Stack.peek()
            if(top.end < slot.begin):
                _Stack.push(slot)
            else:
                top.end = max(top.end, slot.end)
        return _Stack.container

    def dispenseTimes(self, merged):

        # strip edge cases
        edge_one, edge_two = merged[0].end, merged[-1].begin  # 2
        new_container = []

        # iterate over the range not including fringe cases
        for element in merged[1:-1]:
            begin, end = element.begin, element.end
            new_container.append(begin)
            new_container.append(end)

        new_container.insert(0, edge_one)
        new_container.append(edge_two)

        # create a list where every other indexes are pairs:
        # container = [1, 2, 3, 4] would be [[1, 2], [3, 4]]

        return [new_container[n:n+2]
                for n in range(0, len(new_container), 2)]

class SortedList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sort()

    def append(self, item):
        super().append(item)
        self.sort()

    def extend(self, iterable):
        super().extend(iterable)
        self.sort()

    def insert(self, index, item):
        super().insert(index, item)
        self.sort()

    def __add__(self, other):
        result = super().__add__(other)
        result.sort()
        return result

    # +=
    def __iadd__(self, other):
        super().__iadd__(other)
        self.sort()

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        self.sort()

    def __mul__(self, scalar):
        super().__mul__(scalar)
        self.sort()
        return SortedList(self)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)



# Example usage:
sorted_list = SortedList([3, 1, 2])
print("Initial sorted list:", sorted_list)

sorted_list.append(4)
print("After appending 4:", sorted_list)

sorted_list.extend([0, 5])
print("After extending with [0, 5]:", sorted_list)

sorted_list.insert(2, 2.5)
print("After inserting 2.5 at index 2:", sorted_list)

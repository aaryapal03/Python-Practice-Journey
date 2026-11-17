'''
A custom iterator is a user-defined iterator.

Syntax:
class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
'''        


# Example 1 : Counting Numbers
class CountNumbers:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

counter = CountNumbers(1, 5)

for num in counter:
    print(num)

print()



# Example 2 : Even Numbers
class EvenNumbers:

    def __init__(self, limit):
        self.current = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            even = self.current
            self.current += 2
            return even
        else:
            raise StopIteration

even = EvenNumbers(10)

for num in even:
    print(num)

print()


#End of Program

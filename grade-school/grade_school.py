from collections import defaultdict


class School:
    def __init__(self):
        self.colegio = defaultdict(list)

    def add_student(self, name, grade):
        self.colegio[grade].append(name)
        self.colegio[grade] = sorted(self.colegio[grade])

    def roster(self):
        return [k for i, j in sorted(self.colegio.items()) for k in j]

    def grade(self, grade_number):
        return [i for i in sorted(self.colegio[grade_number])]

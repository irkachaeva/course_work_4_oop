class Vacancy:
    def __init__(self, name, salary, area, employer, experience, snippet, alternate_url, type_v):
        self.name = name
        self.salary = salary
        self.area = area
        self.employer = employer
        self.experience = experience
        self.type_v = type_v
        self.snippet = snippet
        self.alternate_url = alternate_url

    def __repr__(self):
        return [self.name, self.salary, self.area, self.employer, self.experience, self.snippet, self.alternate_url, self.type_v]

    def class_to_dict(obj):
        return obj.__dict__
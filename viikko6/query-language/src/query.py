from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn


class QueryBuilder:
    def __init__(self):
        self.matchers = [All()]

    def build(self):
        return And(*self.matchers)

    def plays_in(self, team):
        self.matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return self

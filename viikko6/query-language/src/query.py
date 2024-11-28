from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn


class QueryBuilder:
    def __init__(self, matchers=[All()]):
        self._matchers = matchers

    def build(self):
        return And(*self._matchers)

    def plays_in(self, team):
        return QueryBuilder(matchers=[*self._matchers, PlaysIn(team)])

    def has_at_least(self, value, attr):
        return QueryBuilder(matchers=[*self._matchers, HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(matchers=[*self._matchers, HasFewerThan(value, attr)])

    def one_of(self, *matchers):
        return QueryBuilder(matchers=[Or(*matchers)])

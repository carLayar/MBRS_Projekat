from stereotypes.backend.fetch_type import FetchType


class StereotypeManyToMany:

    def __init__(self, fetch_type: FetchType = FetchType.LAZY, joinTable: str = ''):
        self.fetch_type = fetch_type
        self.joinTable = joinTable

    def __str__(self):
        return '\t[StereotypeManyToMany] FetchType = {}; JoinTable = {};'.format(self.fetch_type.name, self.joinTable)


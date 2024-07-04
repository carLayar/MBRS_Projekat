from stereotypes.backend.fetch_type import FetchType


class StereotypeOneToOne:

    def __init__(self, fetch_type: FetchType = FetchType.LAZY, column_name: str = ''):
        self.fetch_type = fetch_type
        self.column_name = column_name

    def __str__(self):
        return '[StereotypeOneToOne] FetchType = {}; ColumnName = {};'.format(self.fetch_type, self.column_name)


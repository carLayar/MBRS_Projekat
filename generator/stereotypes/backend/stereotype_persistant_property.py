from stereotypes.backend.id_strategy import IdStrategy


class StereotypePersistantProperty:

    def __init__(self, columnName: str = '', length: str = '', precision: str = '', strategy: IdStrategy = IdStrategy.IDENTITY):
        self.columnName = columnName
        self.length = length
        self.precision = precision
        self.strategy = strategy

    def __str__(self):
        return '\t[StereotypePersistantProperty] ColumnName = {}; Length = {}; Precision = {}; Strategy = {}'.format(self.columnName, self.length, self.precision, self.strategy.name)

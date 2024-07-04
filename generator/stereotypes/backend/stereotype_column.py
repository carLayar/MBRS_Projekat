
class StereotypeColumn:

    def __init__(self, name: str = '', unique: bool = False, nullable: bool = False):
        self.name = name
        self.unique = unique
        self.nullable = nullable

    def __str__(self):
        return '\t[StereotypeColumn] Name = {}; Unique = {}; Nullable = {}'.format(self.name, self.unique, self.nullable)


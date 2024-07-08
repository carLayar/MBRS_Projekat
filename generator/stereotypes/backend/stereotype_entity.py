
class StereotypeEntity:

    def __init__(self, table_name: str):
        self.table_name = table_name

    def __str__(self):
        return '[StereotypeEntity] TableName = {};'.format(self.table_name)


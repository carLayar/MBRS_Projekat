from fmmodel.fm_visibility import FMVisibility


class FMAttribute:

    def __init__(self, id: str, name: str,
                 visibility: FMVisibility,
                 data_type: str):
        self.id = id
        self.name = name
        self.visibility = visibility
        self.data_type = data_type

    def __str__(self):
        return '[ATTRIBUTE] Visibility = {}; Name = {}; Id = {}; DataTypeID = {}'\
            .format(self.visibility.name, self.name, self.id, self.data_type)






from io import StringIO

from fmmodel.fm_visibility import FMVisibility


class FMAttribute:

    def __init__(self, id: str, name: str,
                 visibility: FMVisibility,
                 data_type: str):
        self.id = id
        self.name = name
        self.visibility = visibility
        self.data_type = data_type
        self.stereotypes = []

    def __str__(self):
        new_line = '\n'
        sb = StringIO()
        sb.write('[ATTRIBUTE] Visibility = {}; Name = {}; Id = {}; DataTypeID = {}'
                 .format(self.visibility.name, self.name, self.id, self.data_type))
        stereotypes_list = [f.__str__() for f in self.stereotypes]
        if len(stereotypes_list) != 0:
            sb.write(new_line)
        for i, s in enumerate(stereotypes_list):
            if i < len(stereotypes_list) - 1:
                sb.write(s + new_line)
            else:
                sb.write(s)
        return sb.getvalue()






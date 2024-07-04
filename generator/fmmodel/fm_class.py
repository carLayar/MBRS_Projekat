from io import StringIO


class FMClass:
    def __init__(self, id: str, name: str, attributes: []):
        self.id = id
        self.name = name
        self.attributes = attributes

    def __str__(self):
        new_line = '\n'
        sb = StringIO()
        sb.write("[CLASS] Class name = {}; Class id = {}"
                 .format(self.name, self.id))
        sb.write(new_line)
        fields_list = [f.__str__() for f in self.attributes]
        for f in fields_list:
            sb.write(f + new_line)
        return sb.getvalue()



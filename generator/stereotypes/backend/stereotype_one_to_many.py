from stereotypes.backend.cascade_type import CascadeType
from stereotypes.backend.fetch_type import FetchType


class StereotypeOneToMany:

    def __init__(self, fetch_type: FetchType = FetchType.LAZY, cascade_type: CascadeType = CascadeType.PERSIST):
        self.fetch_type = fetch_type
        self.cascade_type = cascade_type

    def __str__(self):
        return '\t[StereotypeOneToMany] FetchType = {}; CascadeType = {};'.format(self.fetch_type.name, self.cascade_type.name)


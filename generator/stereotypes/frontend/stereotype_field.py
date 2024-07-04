from stereotypes.frontend.component_type import ComponentType


class StereotypeField:

    def __init__(self, label: str = '', component: ComponentType = ComponentType.TEXT_FIELD, read_only: bool = True):
        self.label = label
        self.component = component
        self.read_only = read_only

    def __str__(self):
        return '\t[StereotypeField] Label = {}; Component = {}; ReadOnly = {};'\
            .format(self.label, self.component.name, self.read_only)

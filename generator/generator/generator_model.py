from stereotypes.backend.stereotype_entity import StereotypeEntity
from stereotypes.backend.stereotype_many_to_many import StereotypeManyToMany
from stereotypes.backend.stereotype_many_to_one import StereotypeManyToOne
from stereotypes.backend.stereotype_one_to_many import StereotypeOneToMany
from stereotypes.backend.stereotype_one_to_one import StereotypeOneToOne


class ClassGenerationModel:
    def __init__(self, generator_options, clas):
        self.generator_options = generator_options
        self.clas = clas

    @property
    def package(self):
        return self.generator_options.package_name

    @property
    def file_name(self):
        return self.clas.name

    @property
    def table_name(self):
        for stereotype in self.clas.stereotypes:
            if isinstance(stereotype, StereotypeEntity):
                return stereotype.table_name
        return ""

    @property
    def class_name(self):
        return self.clas.name

    @property
    def class_variable(self):
        return self.clas.name[0].lower() + self.clas.name[1:]

    @property
    def repository_class_name(self):
        return self.clas.name + "Repository"

    @property
    def repository_name(self):
        return self.clas.name[0].lower() + self.clas.name[1:] + "Repository"

    @property
    def service_class_name(self):
        return self.clas.name + "Service"

    @property
    def service_name(self):
        return self.clas.name[0].lower() + self.clas.name[1:] + "Service"

    @property
    def clas_properies(self):
        return self.clas.attributes

    @property
    def dto_class_name(self):
        return self.clas.name + "Dto"

    @property
    def non_connected_attributes(self):
        non_connected_attribs = []
        for attribute in self.clas.attributes:
            is_connected = False
            for stereotype in attribute.stereotypes:
                if isinstance(stereotype, StereotypeManyToOne) \
                        or isinstance(stereotype, StereotypeManyToMany)\
                        or isinstance(stereotype, StereotypeOneToMany)\
                        or isinstance(stereotype, StereotypeOneToOne):
                    is_connected = True
                    break
            if not is_connected:
                non_connected_attribs.append(attribute)
        return non_connected_attribs

    @property
    def connected_attributes(self):
        connected_attribs = []
        for attribute in self.clas.attributes:
            is_connected = False
            for stereotype in attribute.stereotypes:
                if isinstance(stereotype, StereotypeManyToOne) \
                        or isinstance(stereotype, StereotypeManyToMany) \
                        or isinstance(stereotype, StereotypeOneToMany) \
                        or isinstance(stereotype, StereotypeOneToOne):
                    is_connected = True
                    break
            if is_connected:
                connected_attribs.append(attribute)
        return connected_attribs


    @property
    def mapper_class_name(self):
        return self.clas.name + "Mapper"

    @property
    def list_variable(self):
        return self.clas.name[0].lower() + self.clas.name[1:] + "s"

    @property
    def list_class(self):
        return self.clas.name + "s"


class ClassesGenerationModel:
    def __init__(self, generator_options, classes: []):
        self.generator_options = generator_options
        self.classes = classes

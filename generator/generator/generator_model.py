from stereotypes.backend.stereotype_entity import StereotypeEntity


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
    def clas_properies(self):
        return self.clas.attributes

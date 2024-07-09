import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from fmmodel.fm_visibility import FMVisibility
from generator.generator_model import ClassGenerationModel
from stereotypes.backend.stereotype_column import StereotypeColumn
from stereotypes.backend.stereotype_many_to_one import StereotypeManyToOne
from stereotypes.backend.stereotype_one_to_many import StereotypeOneToMany
from stereotypes.backend.stereotype_persistant_property import StereotypePersistantProperty
from stereotypes.frontend.stereotype_field import StereotypeField


class ModelGenerator:
    def __init__(self, generator_options, classes):
        self.generator_options = generator_options
        self.classes = classes

        self.env = Environment(loader=FileSystemLoader(self.module_path('templates')))
        self.setup_filters()

    def setup_filters(self):
        # Define a function to convert visibility levels
        def convert_visibility(value):
            visibility_map = {
                FMVisibility.PRIVATE: 'private',
                FMVisibility.PUBLIC: 'public',
                FMVisibility.PROTECTED: 'protected',
                FMVisibility.UNSPECIFIED: '',
            }
            return visibility_map.get(value, value)

        def convert_stereotype(value, classname):
            if isinstance(value, StereotypeColumn):
                return '@Column(name = "{0}", nullable = {1}, unique = {2})'.format(value.name, str(value.nullable).lower(), str(value.unique).lower())
            if isinstance(value, StereotypePersistantProperty):
                return '@Id\n\t@GeneratedValue(strategy=GenerationType.{0})'.format(value.strategy.name)
            if isinstance(value, StereotypeField):
                return ""
            if isinstance(value, StereotypeManyToOne):
                return '@ManyToOne(fetch = FetchType.{0})\n\t@JoinColumn(name = "{1}")'.format(value.fetch_type.name, value.column_name)
            if isinstance(value, StereotypeOneToMany):
                return '@OneToMany(cascade = CascadeType.{0})\n\t@JoinColumn(name = "{1}")'.format(value.cascade_type.name, classname.lower() + "_id")

        # Add the filter to Jinja environment
        self.env.filters['convert_visibility'] = convert_visibility
        self.env.filters['convert_stereotype'] = convert_stereotype

    def generate(self):
        for clas in self.classes:
            generator_model = ClassGenerationModel(self.generator_options, clas)
            self.write_from_template(generator_model)

    def write_from_template(self, model):
        template = self.env.get_template(self.generator_options.template_name)
        output = template.render(model=model)

        current_directory = os.getcwd()
        parent_directory = os.path.dirname(current_directory)
        relative_output_path = self.generator_options.package_name.replace('.', os.sep)
        output_file_name = self.generator_options.output_file_name.format(model.file_name)
        path = os.path.join(parent_directory, self.generator_options.output_path, relative_output_path, output_file_name)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(output)

    def module_path(self, relative_path):
        return os.path.join(os.path.dirname(__file__), relative_path)


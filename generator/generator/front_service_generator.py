import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.generator_model import ClassGenerationModel


class FrontServiceGenerator:
    def __init__(self, generator_options, classes):
        self.generator_options = generator_options
        self.classes = classes

        self.env = Environment(loader=FileSystemLoader(self.module_path('templates')))
        self.setup_filters()

    def setup_filters(self):
        # Define a function to convert visibility levels
        pass

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
        output_directory = os.path.join(parent_directory, self.generator_options.output_path, relative_output_path)

        # Ensure the directory exists
        os.makedirs(output_directory, exist_ok=True)

        output_file_name = self.generator_options.output_file_name.format(model.file_name)
        path = os.path.join(output_directory, output_file_name)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(output)

    def module_path(self, relative_path):
        return os.path.join(os.path.dirname(__file__), relative_path)

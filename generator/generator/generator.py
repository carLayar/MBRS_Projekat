import os

from generator.config.generator_options import GeneratorOptions
from generator.model_generator import ModelGenerator


class Generator:

    def __init__(self, classes: []):
        self.classes = classes

    def generate(self):
        self.generate_model()

    def generate_model(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep), "jpatemplate.jinja", "./templates", "{0}.java", "ftn.backendservice.domain.entities")
        model_generator = ModelGenerator(generator_options, self.classes)
        model_generator.generate()




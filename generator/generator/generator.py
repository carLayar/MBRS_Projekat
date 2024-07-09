import os

from generator.config.generator_options import GeneratorOptions
from generator.model_generator import ModelGenerator
from generator.repository_generator import RepositoryGenerator
from generator.service_generator import ServiceGenerator


class Generator:

    def __init__(self, classes: []):
        self.classes = classes

    def generate(self):
        self.generate_model()
        self.generate_repository_layer()
        self.generate_service_layer()

    def generate_model(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep), "jpatemplate.jinja", "./templates", "{0}.java", "ftn.backendservice.domain.entities")
        model_generator = ModelGenerator(generator_options, self.classes)
        model_generator.generate()

    def generate_repository_layer(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "repository.jinja", "./templates", "{0}Repository.java",
                                             "ftn.backendservice.repositories")
        repository_generator = RepositoryGenerator(generator_options, self.classes)
        repository_generator.generate()

    def generate_service_layer(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "service.jinja", "./templates", "{0}Service.java",
                                             "ftn.backendservice.services")
        service_generator = ServiceGenerator(generator_options, self.classes)
        service_generator.generate()


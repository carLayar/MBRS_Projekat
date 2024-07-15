import os

from generator.config.generator_options import GeneratorOptions
from generator.controller_generator import ControllerGenerator
from generator.details_generator import DetailsGenerator
from generator.dto_generator import DtoGenerator
from generator.front_service_generator import FrontServiceGenerator
from generator.home_page_generator import HomePageGenerator
from generator.mapper_generator import MapperGenerator
from generator.model_generator import ModelGenerator
from generator.repository_generator import RepositoryGenerator
from generator.router_generator import RouterGenerator
from generator.service_generator import ServiceGenerator
from generator.simple_details_generator import SimpleDetailsGenerator
from generator.tables_generator import TablesGenerator


class Generator:

    def __init__(self, classes: []):
        self.classes = classes

    def generate(self):
        self.generate_backend_code()
        self.generate_frontend_code()

    def generate_backend_code(self):
        self.generate_model()
        self.generate_dtos()
        self.generate_mappers()
        self.generate_repository_layer()
        self.generate_service_layer()
        self.generate_controller_layer()

    def generate_frontend_code(self):
        self.generate_frontend_service()
        self.generate_simple_details_components()
        self.generate_details_components()
        self.generate_table_components()
        self.generate_home_page()
        self.generate_router()

    def generate_model(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "jpatemplate.jinja", "./templates", "{0}.java",
                                             "ftn.backendservice.domain.entities")
        model_generator = ModelGenerator(generator_options, self.classes)
        model_generator.generate()

    def generate_dtos(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "dtotemplate.jinja", "./templates", "{0}Dto.java",
                                             "ftn.backendservice.domain.dtos")
        dto_generator = DtoGenerator(generator_options, self.classes)
        dto_generator.generate()

    def generate_mappers(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "mappertemplate.jinja", "./templates", "{0}Mapper.java",
                                             "ftn.backendservice.domain.mappers")
        mapper_generator = MapperGenerator(generator_options, self.classes)
        mapper_generator.generate()

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

    def generate_controller_layer(self):
        generator_options = GeneratorOptions("generator_output\\backend-service\\src\\main\\java".replace("\\", os.sep),
                                             "controller.jinja", "./templates", "{0}Controller.java",
                                             "ftn.backendservice.controllers")
        controller_generator = ControllerGenerator(generator_options, self.classes)
        controller_generator.generate()

    def generate_frontend_service(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "front_service.jinja", "./templates", "{0}Service.js",
                                             "service")
        service_generator = FrontServiceGenerator(generator_options, self.classes)
        service_generator.generate()

    def generate_simple_details_components(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "simple_details.jinja", "./templates", "{0}SimpleDetails.vue",
                                             "components")
        simple_details_generator = SimpleDetailsGenerator(generator_options, self.classes)
        simple_details_generator.generate()

    def generate_details_components(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "details.jinja", "./templates", "{0}Details.vue",
                                             "components")
        details_generator = DetailsGenerator(generator_options, self.classes)
        details_generator.generate()

    def generate_table_components(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "tables.jinja", "./templates", "{0}Table.vue",
                                             "components")
        tables_generator = TablesGenerator(generator_options, self.classes)
        tables_generator.generate()

    def generate_home_page(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "homepage.jinja", "./templates", "HomePage.vue",
                                             "components")
        homepage_generator = HomePageGenerator(generator_options, self.classes)
        homepage_generator.generate()

    def generate_router(self):
        generator_options = GeneratorOptions("generator_output\\vue-template\\src".replace("\\", os.sep),
                                             "router.jinja", "./templates", "index.js",
                                             "router")
        router_generator = RouterGenerator(generator_options, self.classes)
        router_generator.generate()

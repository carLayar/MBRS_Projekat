import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.generator_model import ClassGenerationModel
from stereotypes.frontend.stereotype_field import StereotypeField
from stereotypes.frontend.stereotype_page import StereotypePage


class TablesGenerator:
    def __init__(self, generator_options, classes):
        self.generator_options = generator_options
        self.classes = classes

        self.env = Environment(loader=FileSystemLoader(self.module_path('templates')))
        self.setup_filters()

    def setup_filters(self):
        # Define a function to convert visibility levels
        def label_converter(value):
            for stereotype in value.stereotypes:
                if isinstance(stereotype, StereotypeField):
                    return stereotype.label
            return ""

        def attribute_class_name_converter(value):
            if "List" in value.data_type:
                return value.name[0].upper() + value.name[1:-1]
            return value.name[0].upper() + value.name[1:]

        def attribute_variable_name_converter(value):
            if "List" in value.data_type:
                return value.name[0].lower() + value.name[1:-1]
            return value.name[0].lower() + value.name[1:]

        def connected_attribute_label_converter(value):
            is_singular = True
            searched_data_type = value.data_type
            if "List" in value.data_type:
                splited_list = value.data_type.split("<")
                searched_data_type = splited_list[1].replace(">", "")
                is_singular = False

            connected_type = None
            for clas in self.classes:
                if clas.name == searched_data_type:
                    connected_type = clas
                    break
            if connected_type is None:
                return ""

            page_stereotype = None
            for stereotype in connected_type.stereotypes:
                if isinstance(stereotype, StereotypePage):
                    page_stereotype = stereotype
                    break
            if page_stereotype is not None:
                if is_singular:
                    return page_stereotype.singular_label
                else:
                    return page_stereotype.plural_label
            return ""

        def simple_details_component_converter(value, model):
            is_singular = True
            searched_data_type = value.data_type
            if "List" in value.data_type:
                splited_list = value.data_type.split("<")
                searched_data_type = splited_list[1].replace(">", "")
                is_singular = False

            if is_singular:
                return '<{0}SimpleDetails :id="{1}.{2}Id" />'.format(attribute_class_name_converter(value), model.class_variable, value.name)
            else:
                return '''
        <div v-for="item in {0}.{1}Ids" :key="item">
          <{2}SimpleDetails :id="item"/>
        </div>
                '''.format(model.class_variable, attribute_variable_name_converter(value), attribute_class_name_converter(value))

        def plural_label_converter(value):
            page_stereotype = None
            for stereotype in value.clas.stereotypes:
                if isinstance(stereotype, StereotypePage):
                    page_stereotype = stereotype
                    break
            if page_stereotype is not None:
                return page_stereotype.plural_label
            return ""

        def attribute_list_name_converter(value):
            is_singular = True
            searched_data_type = value.data_type
            if "List" in value.data_type:
                splited_list = value.data_type.split("<")
                searched_data_type = splited_list[1].replace(">", "")
                is_singular = False

            if is_singular:
                return value.name + "s"
            else:
                return value.name

        def generate_label_add_modal(attribute):
            field_stereotype = None
            for stereotype in attribute.stereotypes:
                if isinstance(stereotype, StereotypeField):
                    field_stereotype = stereotype
                    break
            if field_stereotype is not None:
                if not field_stereotype.read_only:
                    return True
            return False

        def attribute_is_singular(value):
            is_singular = True
            searched_data_type = value.data_type
            if "List" in value.data_type:
                splited_list = value.data_type.split("<")
                searched_data_type = splited_list[1].replace(">", "")
                is_singular = False

            return is_singular

        self.env.filters['label_converter'] = label_converter
        self.env.filters['attribute_class_name_converter'] = attribute_class_name_converter
        self.env.filters['connected_attribute_label_converter'] = connected_attribute_label_converter
        self.env.filters['simple_details_component_converter'] = simple_details_component_converter
        self.env.filters['plural_label_converter'] = plural_label_converter
        self.env.filters['attribute_list_name_converter'] = attribute_list_name_converter
        self.env.filters['attribute_variable_name_converter'] = attribute_variable_name_converter

        self.env.globals['generate_label_add_modal'] = generate_label_add_modal
        self.env.globals['attribute_is_singular'] = attribute_is_singular

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



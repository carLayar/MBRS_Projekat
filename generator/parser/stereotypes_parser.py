from stereotypes.backend.cascade_type import CascadeType
from stereotypes.backend.fetch_type import FetchType
from stereotypes.backend.id_strategy import IdStrategy
from stereotypes.backend.stereotype_column import StereotypeColumn
from stereotypes.backend.stereotype_entity import StereotypeEntity
from stereotypes.backend.stereotype_many_to_many import StereotypeManyToMany
from stereotypes.backend.stereotype_many_to_one import StereotypeManyToOne
from stereotypes.backend.stereotype_one_to_many import StereotypeOneToMany
from stereotypes.backend.stereotype_one_to_one import StereotypeOneToOne
from stereotypes.backend.stereotype_persistant_property import StereotypePersistantProperty
from stereotypes.frontend.component_type import ComponentType
from stereotypes.frontend.stereotype_field import StereotypeField
from stereotypes.frontend.stereotype_page import StereotypePage


class StereotypesParser:

    def __init__(self, root, parsed_classes):
        self.root = root
        self.parsed_classes = parsed_classes

        self.namespaces = {
            'uml': 'http://www.omg.org/spec/UML/20110701',
            'xmi': 'http://www.omg.org/spec/XMI/20110701',
            'DSL_Customization': 'http://www.magicdraw.com/schemas/DSL_Customization.xmi',
            'Validation_Profile': 'http://www.magicdraw.com/schemas/Validation_Profile.xmi',
            'MagicDraw_Profile': 'http://www.omg.org/spec/UML/20110701/MagicDrawProfile',
            'UIProfile': 'http://www.magicdraw.com/schemas/UIProfile.xmi',
            'BackEndProfile': 'http://www.magicdraw.com/schemas/BackEndProfile.xmi',
            'StandardProfileL3': 'http://www.omg.org/spec/UML/20110701/StandardProfileL3',
        }

    def parse(self):
        print("Stereotypes--------------------------")
        backend_elements = []
        frontend_elements = []
        for elem in self.root:
            tag_namespace = elem.tag.split('}')[0]  # Extract tag namespace
            tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
            if 'BackEndProfile' in tag_namespace:
                backend_elements.append(elem)
            elif 'UIProfile' in tag_namespace:
                frontend_elements.append(elem)
        print(len(backend_elements))
        print(len(frontend_elements))

        self.parse_backend_stereotypes(backend_elements)
        self.parse_frontend_stereotypes(frontend_elements)

    def parse_backend_stereotypes(self, backend_stereotypes):
        # Print BackEndProfile elements
        print("BackEndProfile Elements:")
        for elem in backend_stereotypes:
            tag_namespace = elem.tag.split('}')[0]  # Extract tag namespace
            tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
            # self.print_element(elem)
            self.parse_backend_stereotype(elem)
            # print("---")

    def parse_backend_stereotype(self, elem):
        tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
        match tag_name:
            case 'Entity':
                self.parse_entity(elem)
            case 'Column':
                self.parse_column(elem)
            case 'PersistantProperty':
                self.parse_persistant_property(elem)
            case 'ManyToOne':
                self.parse_many_to_one(elem)
            case 'OneToMany':
                self.parse_one_to_many(elem)
            case 'ManyToMany':
                self.parse_many_to_many(elem)
            case 'OneToOne':
                self.parse_one_to_one(elem)

    def parse_entity(self, elem):
        class_id = elem.attrib['base_Class']
        table_name = elem.attrib['tableName']

        stereotype_entity = StereotypeEntity(table_name)

        fmclass = self.find_class_by_id(class_id)
        fmclass.stereotypes.append(stereotype_entity)

    def parse_column(self, elem):
        property_id = elem.attrib['base_Property']
        name = elem.attrib['name']
        nullable = True if elem.attrib['nullable'] == 'true' else False
        unique = True if elem.attrib['unique'] == 'true' else False

        stereotype_column = StereotypeColumn(name, nullable, unique)

        fm_property = self.find_property_by_id(property_id)
        fm_property.stereotypes.append(stereotype_column)

    def parse_persistant_property(self, elem):
        property_id = elem.attrib['base_Property']
        columnName = elem.attrib['columnName']
        strategy_str = elem.attrib['strategy']
        strategy = IdStrategy[strategy_str]

        length = ''
        if 'length' in elem.attrib:
            length = elem.attrib['length']

        precision = ''
        if 'precision' in elem.attrib:
            precision = elem.attrib['precision']

        stereotype_persistant_property = StereotypePersistantProperty(columnName=columnName, length=length, precision=precision, strategy=strategy)

        fm_property = self.find_property_by_id(property_id)
        fm_property.stereotypes.append(stereotype_persistant_property)

    def parse_many_to_one(self, elem):
        property_id = elem.attrib['base_Property']
        fetch_type_str = elem.attrib['fetchType']
        fetch_type = FetchType[fetch_type_str]
        column_name = elem.attrib['columnName']

        stereotype_many_to_one = StereotypeManyToOne(fetch_type, column_name)

        fm_property = self.find_property_by_id(property_id)
        if fm_property is not None:
            fm_property.stereotypes.append(stereotype_many_to_one)

    def parse_one_to_many(self, elem):
        property_id = elem.attrib['base_Property']
        fetch_type = FetchType.LAZY
        cascade_type = CascadeType.PERSIST
        if 'fetchType' in elem.attrib:
            fetch_type_str = elem.attrib['fetchType']
            fetch_type = FetchType[fetch_type_str]
        if 'cascadeType' in elem.attrib:
            cascade_type_str = elem.attrib['cascadeType']
            cascade_type = CascadeType[cascade_type_str]

        stereotype_one_to_many = StereotypeOneToMany(fetch_type, cascade_type)

        fm_property = self.find_property_by_id(property_id)
        if fm_property is not None:
            fm_property.stereotypes.append(stereotype_one_to_many)

    def parse_many_to_many(self, elem):
        property_id = elem.attrib['base_Property']
        fetch_type = FetchType.LAZY
        if 'fetchType' in elem.attrib:
            fetch_type_str = elem.attrib['fetchType']
            fetch_type = FetchType[fetch_type_str]

        join_table = ''
        if 'joinTable' in elem.attrib:
            join_table = elem.attrib['joinTable']

        stereotype_many_to_many = StereotypeManyToMany(fetch_type, join_table)

        fm_property = self.find_property_by_id(property_id)
        if fm_property is not None:
            fm_property.stereotypes.append(stereotype_many_to_many)

    def parse_one_to_one(self, elem):
        property_id = elem.attrib['base_Property']
        fetch_type = FetchType.LAZY
        if 'fetchType' in elem.attrib:
            fetch_type_str = elem.attrib['fetchType']
            fetch_type = FetchType[fetch_type_str]

        column_name = ''
        if 'columnName' in elem.attrib:
            column_name = elem.attrib['columnName']

        stereotype_one_to_one = StereotypeOneToOne(fetch_type, column_name)

        fm_property = self.find_property_by_id(property_id)
        if fm_property is not None:
            fm_property.stereotypes.append(stereotype_one_to_one)

    def find_class_by_id(self, searched_id):
        for fmclass in self.parsed_classes:
            if fmclass.id == searched_id:
                return fmclass

    def find_property_by_id(self, property_id):
        for fmclass in self.parsed_classes:
            for fmproperty in fmclass.attributes:
                if fmproperty.id == property_id:
                    return fmproperty

    def parse_frontend_stereotypes(self, frontend_stereotypes):
        # Print UIProfile elements
        print("UIProfile Elements:")
        for elem in frontend_stereotypes:
            tag_namespace = elem.tag.split('}')[0]  # Extract tag namespace
            tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
            self.parse_frontend_stereotype(elem)
            # self.print_element(elem)
            # print("---")

    def parse_frontend_stereotype(self, elem):
        tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
        match tag_name:
            case 'Page':
                self.parse_page(elem)
            case 'Field':
                self.parse_filed(elem)

    def parse_page(self, elem):
        class_id = elem.attrib['base_Class']
        create = True if elem.attrib['create'] == 'true' else False
        update = True if elem.attrib['update'] == 'true' else False
        get_all = True if elem.attrib['getAll'] == 'true' else False
        get_by_id = True if elem.attrib['getById'] == 'true' else False
        singular_label = elem.attrib['singularLabel']
        plural_label = elem.attrib['pluralLabel']
        accusative_label = elem.attrib['accusativeLabel']

        stereotype_page = StereotypePage(create, update, get_all, get_by_id, singular_label, plural_label, accusative_label)

        fmclass = self.find_class_by_id(class_id)
        fmclass.stereotypes.append(stereotype_page)

    def parse_filed(self, elem):
        property_id = elem.attrib['base_Property']
        label = elem.attrib['label']
        read_only = True if elem.attrib['readOnly'] == 'true' else False

        component = ComponentType.TEXT_FIELD
        if 'component' in elem.attrib:
            component_str = elem.attrib['component']
            component = ComponentType[component_str]

        stereotype_field = StereotypeField(label, component, read_only)

        fm_property = self.find_property_by_id(property_id)
        fm_property.stereotypes.append(stereotype_field)

    def print_element(self, element):
        print(f"Tag: {element.tag}")
        for attr, value in element.attrib.items():
            # Remove namespace prefix if present
            if '}' in attr:
                attr = attr.split('}', 1)[1]
            print(f"{attr}='{value}'")

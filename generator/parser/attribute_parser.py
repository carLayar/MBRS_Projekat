from fmmodel.fm_attribute import FMAttribute
from parser.str_to_enum_converter import StrToEnumConverter


class AttributeParser:

    def __init__(self, root, fmclass):
        self.root = root
        self.parsed_class = fmclass

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

        # map for mapping uml to Java types, key is type in uml, value is Java type
        self.type_mapper = {
            'long': 'Long',
            'String': 'String',
            'string': 'String',
            'date': 'LocalDateTime',
            'Date': 'LocalDateTime',
            'double': 'Double',
        }

    def parse(self):
        attributes = []
        attributes_elements = self.parsed_class.findall(".//ownedAttribute", self.namespaces)
        for attribute in attributes_elements:
            parsed_attribute = self.parse_attribute(attribute)
            attributes.append(parsed_attribute)
        return attributes

    def parse_attribute(self, attribute):
        id = attribute.attrib['{' + self.namespaces['xmi'] + '}id']
        name = attribute.attrib['name']
        visibility = StrToEnumConverter.visibility_str_to_enum(attribute.attrib['visibility'])
        data_type = self.parse_data_type(attribute)
        fm_attribute = FMAttribute(id, name, visibility, data_type)
        return fm_attribute

    def parse_data_type(self, attribute):
        try:
            type_id = attribute.attrib['type']
            element = self.root.find(".//packagedElement[@xmi:id='{}']".format(type_id), self.namespaces)
            upper_value_element = attribute.find('.//upperValue[@value]')
            upper_value = upper_value_element.attrib['value']
            if upper_value == '*':
                data_type_name = 'List<{}>'.format(element.attrib['name'])
            else:
                data_type_name = element.attrib['name']
        except KeyError:
            element = attribute.find(".//type/xmi:Extension/referenceExtension", self.namespaces)
            type_string_raw = element.attrib['referentPath']
            uml_type = type_string_raw.split("::")[-1]
            data_type_name = self.convert_to_language_type(uml_type)
        # print(data_type_name)
        return data_type_name

    def convert_to_language_type(self, uml_type):
        return self.type_mapper[uml_type]

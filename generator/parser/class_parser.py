from fmmodel.fm_class import FMClass
from parser.attribute_parser import AttributeParser


class ClassParser:
    def __init__(self, root):
        self.root = root

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

    def parse_classes(self):
        parsed_classes = []
        print("Parsing Classes-----------------------")
        classes = self.root.findall(".//packagedElement[@xmi:type='uml:Class']", self.namespaces)
        for fmclass in classes:
            parsed_class = self.parse_class(fmclass)
            parsed_classes.append(parsed_class)

    def parse_class(self, fmclass):
        # self.print_element(fmclass)
        class_id = fmclass.attrib['{' + self.namespaces['xmi'] + '}id']
        class_name = fmclass.attrib['name']
        attributes_parser = AttributeParser(self.root, fmclass)
        attributes = attributes_parser.parse()
        fmclass = FMClass(class_id, class_name, attributes)
        print(fmclass)
        return fmclass

    def print_element(self, element):
        print(f"Tag: {element.tag}")
        for attr, value in element.attrib.items():
            # Remove namespace prefix if present
            if '}' in attr:
                attr = attr.split('}', 1)[1]
            print(f"{attr}='{value}'")

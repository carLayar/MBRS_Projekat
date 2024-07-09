import xml.etree.ElementTree as ET

from parser.class_parser import ClassParser
from parser.stereotypes_parser import StereotypesParser


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None
        self.parsed_classes = []

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
        self._open_file()
        self.parse_classes()
        self.parse_stereotypes()
        return self.parsed_classes

    def _open_file(self):
        try:
            tree = ET.parse(self.file_path)
            self.root = tree.getroot()
        except FileNotFoundError:
            print('File could not be found!')
            exit(-1)

    def parse_classes(self):
        class_parser = ClassParser(self.root)
        parsed = class_parser.parse_classes()
        self.parsed_classes.extend(parsed)

    def parse_associations(self):
        print("Associations------------------")
        associations = self.root.findall(".//packagedElement[@xmi:type='uml:Association']", self.namespaces)
        print(len(associations))

    def parse_stereotypes(self):
        stereotypes_parser = StereotypesParser(self.root, self.parsed_classes)
        stereotypes_parser.parse()

    def parsing_examplpes(self):
        # Find and print the value of the <xmi:exporter> element
        exporter = self.root.find('.//xmi:exporter', self.namespaces)
        if exporter is not None:
            print(exporter.text)
        else:
            print("Exporter element not found")

        print("MODEL-------------------------")
        model = self.root.find('.//uml:Model', self.namespaces)
        self.print_element(model)

        print("Profiles----------------------")
        profiles = self.root.findall(".//packagedElement[@xmi:type='uml:Profile']", self.namespaces)
        for profile in profiles:
            self.print_element(profile)

    def print_element(self, element):
        print(f"Tag: {element.tag}")
        for attr, value in element.attrib.items():
            # Remove namespace prefix if present
            if '}' in attr:
                attr = attr.split('}', 1)[1]
            print(f"{attr}='{value}'")

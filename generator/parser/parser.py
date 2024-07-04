import xml.etree.ElementTree as ET


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None

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
        # self.parsing_examplpes()
        self.parse_classes()
        # self.parse_associations()
        # self.parse_tags()

    def _open_file(self):
        try:
            tree = ET.parse(self.file_path)
            self.root = tree.getroot()
        except FileNotFoundError:
            print('File could not be found!')
            exit(-1)

    def parse_classes(self):
        print("Classes-----------------------")
        classes = self.root.findall(".//packagedElement[@xmi:type='uml:Class']", self.namespaces)
        print(len(classes))
        for fmclass in classes:
            self.print_element(fmclass)

    def parse_associations(self):
        print("Associations------------------")
        associations = self.root.findall(".//packagedElement[@xmi:type='uml:Association']", self.namespaces)
        print(len(associations))

    def parse_tags(self):
        print("Tags--------------------------")
        backend_elements = []
        ui_elements = []
        for elem in self.root:
            tag_namespace = elem.tag.split('}')[0]  # Extract tag namespace
            tag_name = elem.tag.split('}')[1]  # Extract tag name without namespace
            if 'BackEndProfile' in tag_namespace:
                backend_elements.append(elem)
            elif 'UIProfile' in tag_namespace:
                ui_elements.append(elem)
        print(len(backend_elements))
        print(len(ui_elements))
        # Print BackEndProfile elements
        # print("BackEndProfile Elements:")
        # for elem in backend_elements:
        #     self.print_element(elem)
        #     print("---")
        # Print UIProfile elements
        # print("UIProfile Elements:")
        # for elem in ui_elements:
        #     self.print_element(elem)
        #     print("---")

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

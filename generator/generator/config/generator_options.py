

class GeneratorOptions:
    def __init__(self, output_path: str, template_name: str, template_dir: str, output_file_name: str, package_name: str):
        self.output_path = output_path
        self.template_name = template_name
        self.template_dir = template_dir
        self.output_file_name = output_file_name
        self.package_name = package_name

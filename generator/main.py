# This is a sample Python script.
from generator.generator import Generator
from parser.parser import Parser


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = '../dijagrami/MBRS.xml'
    parser = Parser(path)
    parsed_classes = parser.parse()
    for c in parsed_classes:
        print(c)
    generator = Generator(parsed_classes)
    generator.generate()


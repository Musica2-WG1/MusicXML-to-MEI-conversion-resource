import verovio
import xml.etree.ElementTree as ET
import os

def check_composer_name(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    for creator in root.findall(".//creator"):
        if creator.attrib.get('type') == 'composer' and 'Mozart' in creator.text:
            return True
    return False

def convert_to_mei(xml_file_path, output_folder):
    if check_composer_name(xml_file_path):
        tk = verovio.toolkit()
        tk.loadFile(xml_file_path)
        base_name = os.path.basename(xml_file_path)
        mei_file_path = os.path.join(output_folder, base_name.replace('.xml', '.mei'))
        mei_data = tk.getMEI()
        with open(mei_file_path, 'w', encoding=’utf-8’) as mei_file:
            mei_file.write(mei_data)

input_folder = "Path/to/input/folder"# here, add an input folder
output_folder = "Path/to/ouput/folder"# here, add an output folder
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".xml"):
        xml_file_path = os.path.join(input_folder, file_name)
        convert_to_mei(xml_file_path, output_folder)

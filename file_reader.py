import json
from xml_property_parser import parse_xml_list

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_lines_without_at(self):
        lines_without_at = []
        with open(self.file_path, 'r') as file:
            for line in file:
                if not line.startswith('@'):
                    # Remove leading/trailing whitespaces and append to the list
                    lines_without_at.append(line.strip())
        return lines_without_at

    def get_lines_with_at(self):
        lines_with_at = []
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('@'):
                    # Remove leading/trailing whitespaces and append to the list
                    lines_with_at.append(line.strip())
        return lines_with_at

    def get_props_obj(self):
        xml_list = [line.replace('@','') for line in self.get_lines_with_at()]
        props_obj = parse_xml_list(xml_list)
        
        # strip white-spaces from each value
        # original_dict = {"name": " John ", "age": 25, "city": " New York ", "country": " United States "}
        return {key: value.strip('"') if isinstance(value, str) else value for key, value in props_obj.items()}
    
    def get_json_obj(self):
        return json.loads(''.join(self.get_lines_without_at()))
    


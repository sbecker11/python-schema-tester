import json

class JSONParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.json_object = {}
        self.xml_properties = []

    def parse(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                # Check if the line starts with '@' indicating an XML-style property
                if line.startswith('@'):
                    # Extract the property name and value
                    property_name, property_value = line[1:].strip().split('=')
                    # Add the property to the JSON object
                    self.json_object[property_name] = property_value
                    # Add the property name to the list of XML-style properties
                    self.xml_properties.append(property_name)
                else:
                    # If the line does not start with '@', assume it's a regular JSON property
                    # and add it to the JSON object
                    self.json_object.update(json.loads(line))

        return self.json_object, self.xml_properties

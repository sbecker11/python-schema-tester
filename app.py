import json
import jsonschema

from file_reader import FileReader
from xml_property_parser import parse_xml_list

def main():
    file_reader = FileReader('data.json')
    props_obj = file_reader.get_props_obj()
    json_obj = file_reader.get_json_obj()

    print(f"props_obj:{json.dumps(props_obj)}")
    print(f"json_obj:{json.dumps(json_obj)}")

if __name__ == '__main__':
    main()


# # Load JSON Schema from schema.json
# with open('schema.json', 'r') as schema_file:
#     schema_data = json.load(schema_file)
#     schema = jsonschema.Draft7Validator(schema_data)

# # Load JSON data from data.json
# with open('data.json', 'r') as data_file:
#     data = json.load(data_file)

# # read the relative location of the schema file
# # from a commented line in the JSON dat file
# # <schema-file>"./schema.json"</schema-file>

# xml_props = scanner.get_xml_style_properties('data.json')

# print(xml_props)

# # Validate JSON data against JSON Schema
# if schema.is_valid(data):
#     print("JSON data is valid against the JSON Schema.")
# else:
#     print("JSON data is not valid against the JSON Schema.")
#     print("Validation errors:")
#     for error in schema.iter_errors(data):
#         print(error)

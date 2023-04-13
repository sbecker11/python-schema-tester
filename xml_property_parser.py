import xml.etree.ElementTree as ET

def parse_xml_list(xml_list):
    """
    Parses a list of XML-formatted strings and returns a dictionary object with property-value pairs.

    Args:
        xml_list (list): A list of XML-formatted strings.

    Returns:
        dict: A dictionary object with property-value pairs.
    """
    # Create a dictionary to store the property-value pairs
    result = {}

    # Iterate through the XML-formatted strings in the list
    for xml_string in xml_list:
        # Parse the XML string into an ElementTree object
        root = ET.fromstring(xml_string)

        # Extract the property name and value from the XML element
        prop_name = root.tag
        prop_value = root.text

        # Add the property-value pair to the dictionary
        result[prop_name] = prop_value

    return result


# Test case for a valid list of XML-formatted strings
xml_list_valid = ["<prop1>val1</prop1>", "<prop2>val2</prop2>"]
result_valid = parse_xml_list(xml_list_valid)
expected_result_valid = {"prop1": "val1", "prop2": "val2"}
assert result_valid == expected_result_valid, f"Assertion failed: expected {expected_result_valid}, but got {result_valid}"

# Test case for an invalid list of XML-formatted strings
xml_list_invalid = ["<prop1>val1</prop1>", "<prop2>val2</prop2", "<prop3>val3</prop3>"]  # missing closing tag for prop2
try:
    result_invalid = parse_xml_list(xml_list_invalid)
except ET.ParseError:
    # Expected ParseError to be raised
    pass
else:
    assert False, "Assertion failed: expected ParseError to be raised, but no error was raised"

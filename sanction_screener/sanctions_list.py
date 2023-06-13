import xmltodict
from sanctsanctions_data import xml_data
from datetime import datetime

def convert_string_to_date(date_string):
    # Specify the format of the input string
    input_format = "%Y-%m-%d-%H:%M"

    # Parse the string and convert it to a datetime object
    date = datetime.strptime(date_string, input_format).date()

    return date

def xml_to_dict_constructor(x):
    dict_object = {
        "first_name": x.get('FIRST_NAME').capitalize() if x.get('FIRST_NAME') else x.get('FIRST_NAME'),
        "second_name": x.get('SECOND_NAME').capitalize() if x.get('SECOND_NAME') else x.get('SECOND_NAME'),
        "third_name": x.get('THIRD_NAME').capitalize() if x.get('THIRD_NAME') else x.get('THIRD_NAME'),
        #"sanction_id": x['DATAID'],
        "list_type": x['UN_LIST_TYPE'],
        "reference_number": x["REFERENCE_NUMBER"],
        "date_listed": ["LISTED_ON"],
        "comments1": x["COMMENTS1"],
        "designation": x.get("DESIGNATION"),
        "nationality": x.get("NATIONALITY"),
        "list_type": x["LIST_TYPE"],
        "last_day_updated": x["LAST_DAY_UPDATED"],
        "individual_alias": x["INDIVIDUAL_ALIAS"],
        "individual_address": x["INDIVIDUAL_ADDRESS"],
        "date_of_birth": x["INDIVIDUAL_DATE_OF_BIRTH"],
        "place_of_birth": x["INDIVIDUAL_PLACE_OF_BIRTH"],
        "individual_document": x["INDIVIDUAL_DOCUMENT"]
    }
    return dict_object


def xml_to_dict(xml_string):
    xml_dict = xmltodict.parse(xml_string)
    return xml_dict

# Convert XML to dictionary
result = xml_to_dict(xml_data)

# Print the resulting dictionary
individuals = result['INDIVIDUALS']['INDIVIDUAL']
for x in individuals:
    print(xml_to_dict_constructor(x))


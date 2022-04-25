import json
import os
import utils.config_reader as cf


def open_budget():
    """Opens the YNAB4 budget file and sends each entity to another function to create
        a newline JSON file.
    """
    with open(cf.get_value('BudgetFile')) as json_file:
        data = json.load(json_file)

        for entity in cf.get_entities():
            convert_to_newline_json(entity, data[entity])


def convert_to_newline_json(entity: str, data: list):
    """Write each record from YNAB4's budget for this entity into a new line
        in JSON, named after the entity. This will just write to your local disk.

    Args:
        entity (str): Name of this entity, e.g. 'accounts', 'transactions'.
        data (list): List of records from the YNAB4 budget file for this entity.
    """
    with open(''.join((entity, '.json')), 'w') as f:
        for line in data:
            json.dump(line, f)
            f.write('\n')


def clean_up_files():
    """Iterate through each YNAB4 entity and delete the JSON file named after it from 
        your local disk.
    """
    for entity in cf.get_entities():
        filename = ''.join((entity, '.json'))
        os.remove(filename)
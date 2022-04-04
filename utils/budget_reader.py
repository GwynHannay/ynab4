import json


def open_budget():
    with open('dev_files/Budget.yfull') as json_file:
        data = json.load(json_file)
        process_categories(data['masterCategories'])


def process_categories(masters):
    for cat in masters:
        print(cat)
        print(type(cat))
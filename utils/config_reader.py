import configparser

config = configparser.ConfigParser()
config.read('config/bigquery.ini')
ynab_config = config['YNAB']



def get_value(key):
    return ynab_config[key]


def get_entities():
    entities = [
        'accountMappings',
        'accounts',
        'masterCategories',
        'monthlyBudgets',
        'payees',
        'scheduledTransactions',
        'transactions'
    ]

    return entities
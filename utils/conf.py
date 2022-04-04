import configparser

config = configparser.ConfigParser()
conf_folder = 'config'
dropbox_file = 'keys.ini'
ynab_file = 'budget.ini'


def fetch_config(file, item, env=None):
    filename = choose_file(file)

    if env is not None:
        section = choose_section(env)
    else:
        section = choose_section(file)
    
    config = get_conf_file(filename)
    config_value = config[section][item]

    return config_value


def get_conf_file(filename):
    conf_location = '/'.join((conf_folder, filename))
    config.read(conf_location)

    return config


def choose_file(file):
    files = {
        'Dropbox': 'keys.ini',
        'YNAB': 'budget.ini'
    }

    return files[file]


def choose_section(section):
    sections = {
        'Dropbox': 'DROPBOX',
        'DEV': 'DEV'
    }

    return sections[section]
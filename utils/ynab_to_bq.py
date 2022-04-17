import json
import os
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'config/ynab4_gcp_key.json')
client = bigquery.Client('pandademic', credentials)

entities = [
    'accountMappings',
    'accounts',
    'masterCategories',
    'monthlyBudgets',
    'payees',
    'scheduledTransactions',
    'transactions'
]


def open_budget():
    """Opens the YNAB4 budget file and sends each entity to another function to create
        a newline JSON file.
    """
    with open('Budget.yfull') as json_file:
        data = json.load(json_file)

        for entity in entities:
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


def upload_to_bq():
    """Uploads each JSON file for YNAB4 entities into BigQuery. Presets are:
        Dataset: 'ynab'
        Location: 'australia-southeast2'
        Write Disposition: WRITE_TRUNCATE
        Schema: Auto-detect

    Raises:
        Exception: Throw an exception if the JSON file can't be uploaded and tell us
            which entity threw the error.
    """
    dataset_ref = client.dataset('ynab')
    job_config = bigquery.LoadJobConfig()

    for entity in entities:
        filename = ''.join((entity, '.json'))
        if os.stat(filename).st_size == 0:
            continue

        table_ref = dataset_ref.table(entity)
        job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        job_config.autodetect = True

        try:
            with open(filename, 'rb') as source_file:
                job = client.load_table_from_file(
                    source_file,
                    table_ref,
                    location="australia-southeast2",
                    job_config=job_config
                )
        except Exception as e:
            msg = "Problem with entity: {}. {}".format(entity, e)
            raise Exception(msg)

        job.result()

        print("Loaded {} rows into {}:{}".format(
            job.output_rows, 'ynab', entity))


def clean_up_files():
    """Iterate through each YNAB4 entity and delete the JSON file named after it from 
        your local disk.
    """
    for entity in entities:
        filename = ''.join((entity, '.json'))
        os.remove(filename)

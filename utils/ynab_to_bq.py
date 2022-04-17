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
    with open('dev_files/Budget.yfull') as json_file:
        data = json.load(json_file)

        for entity in entities:
            convert_to_newline_json(entity, data[entity])


def convert_to_newline_json(entity, data):
    with open(''.join((entity, '.json')), 'w') as f:
        for line in data:
            json.dump(line, f)
            f.write('\n')


def upload_to_bq():
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

        print("Loaded {} rows into {}:{}".format(job.output_rows, 'ynab', entity))



def clean_up_files():
    for entity in entities:
        filename = ''.join((entity, '.json'))
        os.remove(filename)
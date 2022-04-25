import utils.config_reader as cf
import os
from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file(
    cf.get_value('ServiceAccountKey'))
client = bigquery.Client(cf.get_value('ProjectID'), credentials)


def upload_to_bq():
    """Uploads each JSON file for YNAB4 entities into BigQuery. Presets are:
        Write Disposition: WRITE_TRUNCATE
        Schema: Auto-detect

    Raises:
        Exception: Throw an exception if the JSON file can't be uploaded and tell us
            which entity threw the error.
    """
    dataset = cf.get_value('Dataset')
    dataset_ref = client.dataset(dataset)
    job_config = bigquery.LoadJobConfig()

    for entity in cf.get_entities():
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
                    location=cf.get_value('Location'),
                    job_config=job_config
                )
        except Exception as e:
            msg = "Problem with entity: {}. {}".format(entity, e)
            raise Exception(msg)

        job.result()

        print("Loaded {} rows into {}:{}".format(
            job.output_rows, dataset, entity))


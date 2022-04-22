import utils.ynab_to_bq as bq


def main():
    """Imports YNAB4 data into BigQuery in three steps:
        1. Generate newline JSON files for each entity in YNAB.
        2. Uploads JSON files to BigQuery.
        3. Removes the JSON files from your local disk.
    """
    bq.open_budget()
    bq.upload_to_bq()
    bq.clean_up_files()


if __name__ == "__main__":
    main()

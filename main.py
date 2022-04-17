import utils.ynab_to_bq as bq


def main():
    bq.open_budget()
    bq.upload_to_bq()
    bq.clean_up_files()


if __name__ == "__main__":
    main()
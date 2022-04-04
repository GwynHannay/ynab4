import utils.conf as conf
import utils.dbox as dbox
import utils.budget_reader as br


def main():
    # token = conf.fetch_config('YNAB', 'BUDGET_FOLDER', 'DEV')
    # print(token)
    #dbox.get_files_list(token, 'Name')
    br.open_budget()


if __name__ == "__main__":
    main()
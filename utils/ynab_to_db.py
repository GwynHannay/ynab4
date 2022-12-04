import sqlite3
import utils.config_reader as cf


def create_connection(db_file='ynab.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_file, isolation_level=None)
    except Exception as e:
        msg = 'Trouble creating database: {}. Error: {}'.format(db_file, e)
        raise Exception(msg)
    
    query = (
        "SELECT name FROM sqlite_master WHERE type = 'table';"
    )

    results = conn.execute(query)

    tables = results.fetchall()

    if tables:
        for table in tables:
            print(table)
    else:
        table_create = """
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                account_name TEXT,
                account_type TEXT,
                on_budget INTEGER,
                sortable_index INTEGER,
                hidden INTEGER,
                last_entered_check_number INTEGER,
                last_reconciled_balance REAL,
                last_reconciled_date TEXT
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS master_categories (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                name TEXT,
                type TEXT,
                is_tombstone INTEGER,
                sortable_index INTEGER,
                deleteable INTEGER,
                expanded INTEGER
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS sub_categories (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                name TEXT,
                type TEXT,
                is_tombstone INTEGER,
                sortable_index INTEGER,
                master_categoryid TEXT,
                cached_balance INTEGER,
                note BLOB
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS monthly_budgets (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                month TEXT,
                is_resolved_conflict INTEGER,
                note BLOB
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS monthly_sub_category_budgets (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                categoryid TEXT,
                overspending_handling TEXT,
                is_tombstone INTEGER,
                is_resolved_conflict INTEGER,
                parent_monthly_budgetid TEXT,
                budgeted REAL
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS payees (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                target_accountid TEXT,
                auto_fill_categoryid TEXT,
                auto_fill_memo TEXT,
                auto_fill_amount REAL,
                name TEXT,
                is_tombstone INTEGER,
                is_resolved_conflict INTEGER,
                enabled INTEGER
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                is_tombstone INTEGER,
                longitude INTEGER,
                latitude INTEGER,
                parent_payeeid TEXT
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS rename_conditions (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                is_tombstone INTEGER,
                operator INTEGER,
                operand INTEGER,
                parent_payeeid TEXT
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                accountid TEXT,
                categoryid TEXT,
                payeeid TEXT,
                target_accountid TEXT,
                transfer_transactionid TEXT,
                date TEXT,
                amount REAL,
                memo TEXT,
                accepted INTEGER,
                cleared INTEGER,
                is_tombstone INTEGER,
                is_resolved_conflict INTEGER,
                flag TEXT
            );
        """

        conn.execute(table_create)
        conn.commit()

        table_create = """
            CREATE TABLE IF NOT EXISTS sub_transactions (
                id INTEGER PRIMARY KEY,
                entityid TEXT,
                entity_type TEXT,
                entity_version TEXT,
                categoryid TEXT,
                amount REAL,
                memo TEXT,
                is_tombstone INTEGER,
                parent_transactionid TEXT
            );
        """

        conn.execute(table_create)
        conn.commit()
    
    return conn
import sqlite3

use_lite = True

if use_lite:
    db_file = 'budget.db'


def create_connection(db_file):
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
            CREATE TABLE IF NOT EXISTS categories (
                id integer PRIMARY KEY,
                master_category text,
                master_type text,
                master_id text,
                sub_category text,
                category_type text,
                category_id text,
                cached_balance real
            );
        """

        conn.execute(table_create)
        conn.commit()
    
    return conn
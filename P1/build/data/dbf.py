import sqlite3
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent.parent
APP_PATH = OUTPUT_PATH / "data"
DB_PATH = APP_PATH / "transaction.db"

def add_transaction(table: str, name: str, amount: float, date: str) -> None:
    """
    Add a transaction to the database.

    Parameters:
    - name (str): The name of the transaction.
    - amount (float): The amount of the transaction.
    - date (str): The date and time of the transaction in the format 'YYYY-MM-DD HH:MM:SS'.

    Returns:
    - None
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Create the table if it doesn't exist, with columns id, name, amount, and date
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                (id INTEGER PRIMARY KEY, name TEXT, amount REAL, date TEXT)''')

    # Insert a new row into the table with the provided name, amount and date
    c.execute(f"INSERT INTO {table} (name, amount, date) VALUES (?, ?, ?)", (name, f"{amount:.2f}", date))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()

#add_transaction("transactions1", "Spesa", 138.76, "06/05/2024 16:34:45")


def edit_transaction_attribute(table: str, attribute: str, primary_key: str, new_value: str) -> None:
    """
    Edit a specific attribute in a table using the primary key.

    Parameters:
    - table (str): The name of the table where the attribute is located.
    - attribute (str): The name of the attribute to edit.
    - new_value (str): The new value to assign to the attribute.
    - primary_key (str): The value of the primary key to identify the row to edit.

    Returns:
    - None
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Execute the SQL query to update the attribute using the primary key with parameters (new_value)
    c.execute(f"UPDATE {table} SET {attribute} = ? WHERE rowid = ?", (new_value, primary_key))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()


def delete_transaction(table: str, primary_key: str) -> None:
    """
    Delete a row from a table in the SQLite database based on its primary key value.

    Parameters:
    - table (str): The name of the table from which to delete the row.
    - primary_key (str): The value of the primary key of the row to delete.

    Returns:
    - None
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Execute the SQL query to delete the row using the primary key
    c.execute(f"DELETE FROM {table} WHERE rowid = ?", (primary_key,))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()

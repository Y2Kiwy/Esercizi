from pathlib import Path

# Define all usefull path for the code
PROJECT_DIR = Path(__file__).parent.parent.parent            # Project directory path
ASSETS_DIR = PROJECT_DIR / "build" / "assets" / "frame0"     # Assets directory path
DBF_PATH = PROJECT_DIR / "build" / "data"                    # Database functions lib directory
DB_PATH = PROJECT_DIR / "build" / "data" / "transactions.db" # Database path

from dbf import *

from tkinter import *

from datetime import datetime

def normalize_textbox_values(txn_name: str, txn_amount: str, txn_date: str):
    """
    Normalizes the values of transaction amount, and date and check for hidden codes in transaction name.

    Args:
    - txn_name (str): The name of the transaction.
    - txn_amount (str): The amount of the transaction.
    - txn_date (str): The date and time of the transaction.

    Returns:
    - str, float, datetime: The three values normalized
    """
    # Check for hidden code in 'txn_name'
    if txn_name != "":
        print("'txn_name is not empty")
        hidden_code_handler(txn_name)

    # Normalize 'txn_amount' to float if not empty
    if txn_amount != "":
        print("'txn_amount is not empty")
        txn_amount: float = float(txn_amount.replace(",", "."))

    # Normalize 'txn_date' to datetime if not empty
    if txn_date != "":
        try:
            print("'txn_date is not empty")
            txn_date: datetime = datetime.strptime(txn_date, "%Y-%m-%d %H:%M")

        except ValueError:
            print("'txn_date is not with '%Y-%m-%d %H:%M' format trying '%Y-%m-%d'")
            txn_date: datetime = datetime.strptime(txn_date, "%Y-%m-%d").date()




    # Return the normalized values of transaction name, amount, and date
    return txn_name, txn_amount, txn_date


# Build assets path
def asset_path_build(path: str) -> Path:
    return ASSETS_DIR / Path(path)







'''
# Initialize variables to collect transaction amount
transaction_expense: float = 0.00
transaction_income: float = 0.00

# Handles submission of transaction amounts and updates global variables and canvas display accordingly
def submit_transaction() -> None:

    global transaction_expense
    global transaction_income

    # Retrieve the new transaction name, amount and data entered by the user
    newT_name = entry_1.get()
    newT_amount = float(entry_2.get().replace(",", ".")) # Format amount for Python decimals declaration standard
    newT_date = entry_3.get()

    hidden_code_handler(newT_name)
    
    last_balance_raw: list[tuple] = collect_balance("transactions1")
    last_balance: float = last_balance_raw[0]

    # Check if the transaction amount is positive (income)
    if newT_amount > 0:
        total_income_raw: float = collect_income_total("transactions1")
        total_income: float = [float(value[0]) for value in total_income_raw]
        total_income: float = sum(total_income)
        # If positive, add it to the transaction income
        total_income += newT_amount
        # Update the displayed income on the canvas
        canvas.itemconfig(tagOrId=income, text=f"{total_income:,.2f}€")

    # Check if the transaction amount is negative (expense)
    elif newT_amount < 0:
        total_expense_raw: float = collect_expense_total("transactions1")
        total_expense: float = [float(value[0]) for value in total_expense_raw]
        total_expense: float = sum(total_expense)
        # If negative, add it to the transaction expense
        total_expense += newT_amount
        # Update the displayed expense on the canvas
        canvas.itemconfig(tagOrId=expense, text=f"{total_expense:,.2f}€")

    # Update the balance label by adding income and subtracting expenses
    update_balance = last_balance + newT_amount

    # Update the displayed balance on the canvas
    canvas.itemconfig(tagOrId=balance, text=f"{update_balance:,.2f}€")

    # Add the new transaction to the database
    add_transaction(table="transactions1", name=newT_name, amount=newT_amount, date=newT_date)
'''

















































# Function to handle hidden code in a string
def hidden_code_handler(code_str: str) -> None:
    # Define special identifiers for specific actions
    balance_id: str = "!balance:"
    delete_id: str = "!delete:"
    edit_id: str = "!edit:"
    pdf_id: str = "!pdf:"

    # Check if the string contains the balance_id
    if balance_id in code_str:
        # If so, call the balance_hidden_code function
        print(f"Label 'name' contains '!balance:' hidden code, calling 'balance_hidden_code()'...")
        balance_hidden_code(code_str)
    elif pdf_id in code_str:
        # If so, call the generate_pdf_from_db function
        print(f"Label 'name' contains '!pdf:' hidden code, calling 'generate_pdf_from_db()'...")
        generate_pdf_from_db()

# Function to handle hidden code related to balance
def balance_hidden_code(code_str: str) -> None:
    # Count the number of rows in the transactions table in the database
    db_rows: int = count_item("transactions1")
    print(f"Checking if the database is empty...")

    # If there is only one row in the database
    if db_rows == 1:
        # Extract the new balance from the code string
        new_balance: int = int(code_str.split(":")[1])
        # Edit the 'balance' attribute of the first transaction in the database
        edit_transaction_attribute("transactions1", "balance", 1, new_balance)
        print(f"Attribute 'balance' edited correctly to {new_balance}")
    else:
        # If the database is not empty, print a message indicating failure
        print(f"The database is not empty, failed to edit 'balance'")


import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

# Generate a PDF file with all the database transactions
def generate_pdf_from_db() -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Execute a query to select data from the table
    cursor.execute("SELECT * FROM transactions1;")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Create the PDF document
    pdf_path = "transactions1.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    data = []

    # Add the table header
    header = ["id", "name", "amount", "balance"]
    data.append(header)

    # Add the data rows to the table
    for row in rows:
        data.append(row)

    # Create the table in the PDF document
    table = Table(data)
    table.setStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Add the table to the document
    doc.build([table])

    print("PDF file successfully created:", pdf_path)

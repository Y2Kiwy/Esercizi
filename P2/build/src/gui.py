from pathlib import Path

# Define all usefull path for the code
PROJECT_DIR = Path(__file__).parent.parent.parent            # Project directory path
ASSETS_DIR = PROJECT_DIR / "build" / "assets" / "frame0"     # Assets directory path
DBF_PATH = PROJECT_DIR / "build" / "data"                    # Database functions lib directory
DB_PATH = PROJECT_DIR / "build" / "data" / "transactions.db" # Database path

import sys
sys.path.append(str(DBF_PATH))

from dbf import *

# Check if the database exists to initialize it if not
if not DB_PATH.exists():
    initialize_db("transactions1", 1_000)

from functions import *

# Handles submission of transaction amounts and updates global variables and canvas display accordingly
def submit_transaction() -> None:

    # Get values from texboxes and normalize it
    txn_name, txn_amount, txn_date = normalize_textbox_values(name_textbox.get(), amount_textbox.get(), date_textbox.get())

    print(f"\nCollected: \n\t{txn_name} {type(txn_name)}\n\t{txn_amount} {type(txn_amount)}\n\t{txn_date} {type(txn_date)}")

    # Collect income and expense total and the last known balance
    income_total: float = collect_income_total("transactions1")
    balance_last: float = collect_balance("transactions1")
    expense_total: float = collect_expense_total("transactions1")

    # Check if 'txn_amount' is not empty
    if txn_amount:

        # Check if 'txn_amount' is income
        if txn_amount > 0:
            # Recalculate the income total
            income_total += txn_amount
            # Update the displayed income on the canvas
            canvas.itemconfig(tagOrId=income, text=f"{income_total:,.2f}€")

        # Check if 'txn_amount' is expense
        elif txn_amount < 0:
            # Recalculate the expense total
            expense_total += txn_amount
            # Update the displayed income on the canvas
            canvas.itemconfig(tagOrId=expense, text=f"{expense_total:,.2f}€")

        # Update the balance label by adding income and subtracting expenses
        update_balance = balance_last + txn_amount

        # Update the displayed balance on the canvas
        canvas.itemconfig(tagOrId=balance, text=f"{update_balance:,.2f}€")

        # Add the new transaction to the database
        add_transaction(table="transactions1", name=txn_name, amount=txn_amount, date=txn_date)

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Start of GUI ----------------------------------------------------------------

# Create new tkinter graphic window
window = Tk()

# Set window size 
window.geometry("640x480")

# Set window background color
window.configure(bg = "#FFFFFF")



# Create new canva over the tkinter window
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Blu rectangle on the top screen
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    640.0,
    96.0,
    fill="#00317B",
    outline="")

# Title of the app in the top-left corner
canvas.create_text(
    24.0,
    29.0,
    anchor="nw",
    text="Balance Tracker",
    fill="#FFFFFF",
    font=("Ubuntu", 32 * -1, "bold")
)


# 'income' background rectangle
income_bg_rect_obj = PhotoImage(
    file=asset_path_build("income_bg_rect.png"))
income_bg_rect_canvas = canvas.create_image(
    176.0,
    160.0,
    image=income_bg_rect_obj
)

# 'balance' background rectangle
balance_bg_rect_obj = PhotoImage(
    file=asset_path_build("balance_bg_rect.png"))
balance_bg_rect_canvas = canvas.create_image(
    320.0,
    240.0,
    image=balance_bg_rect_obj
)

# 'expenses' background rectangle
expense_bg_rect_obj = PhotoImage(
    file=asset_path_build("expense_bg_rect.png"))
expense_bg_rect_canvas = canvas.create_image(
    464.0,
    160.0,
    image=expense_bg_rect_obj
)

# Logo of the app in the top-right corner
logo_obj = PhotoImage(
    file=asset_path_build("logo.png"))
logo_canvas = canvas.create_image(
    590.0,
    48.0,
    image=logo_obj
)



# 'income' title text
canvas.create_text(
    72.0,
    137.0,
    anchor="nw",
    text="Income",
    fill="#604500",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'balance' title text
canvas.create_text(
    72.0,
    217.0,
    anchor="nw",
    text="Balance",
    fill="#0A4B00",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'expenses' title text
canvas.create_text(
    360.0,
    137.0,
    anchor="nw",
    text="Expenses",
    fill="#660000",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'income' value text
income = canvas.create_text(
    72.0,
    152.0,
    anchor="nw",
    text=f"0€",
    fill="#4F4500",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'balance' value text
balance = canvas.create_text(
    72.0,
    232.0,
    anchor="nw",
    text=f"0€",
    fill="#0A4B00",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'expenses' value text
expense = canvas.create_text(
    360.0,
    152.0,
    anchor="nw",
    text=f"0€",
    fill="#660000",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'add transaction' title text
canvas.create_text(
    250.0,
    310.0,
    anchor="nw",
    text="Add Transaction\n",
    fill="#00317B",
    font=("Ubuntu", 16 * -1, "bold")
)

# 'name' title text
canvas.create_text(
    72.0,
    334.0,
    anchor="nw",
    text="Name\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'amount' title text
canvas.create_text(
    344.0,
    334.0,
    anchor="nw",
    text="Amount (€)\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'date' title text
canvas.create_text(
    488.0,
    335.0,
    anchor="nw",
    text="Date\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)


# 'name' background rectangle, textbox
name_bg_rect_obj = PhotoImage(
    file=asset_path_build("name_bg_rect.png"))
name_bg_rect_canvas = canvas.create_image(
    176.0,
    368.0,
    image=name_bg_rect_obj
)
name_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
name_textbox.place(
    x=64.0,
    y=352.0,
    width=224.0,
    height=30.0
)

# 'amount' background rectangle, textbox
amount_bg_rect_obj = PhotoImage(
    file=asset_path_build("amount_bg_rect.png"))
amount_bg_rect_canvas = canvas.create_image(
    384.0,
    368.0,
    image=amount_bg_rect_obj
)
amount_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
amount_textbox.place(
    x=336.0,
    y=352.0,
    width=96.0,
    height=30.0
)

# 'date' background rectangle, textbox
date_bg_rect_obj = PhotoImage(
    file=asset_path_build("date_bg_rect.png"))
date_bg_rect_canvas = canvas.create_image(
    528.0,
    368.0,
    image=date_bg_rect_obj
)
date_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
date_textbox.place(
    x=480.0,
    y=352.0,
    width=96.0,
    height=30.0
)



# 'submit' background rectangle, button
submit_bg_rect_obj = PhotoImage(
    file=asset_path_build("submit_button.png"))
submit_button = Button(
    image=submit_bg_rect_obj,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit_transaction(),
    relief="flat"
)
submit_button.place(
    x=48.0,
    y=400.0,
    width=544.0,
    height=48.0
)

# 'settings' background rectangle, button
settings_bg_rect_obj = PhotoImage(
    file=asset_path_build("settings_button.png"))
settings_button = Button(
    image=settings_bg_rect_obj,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings_button clicked"),
    relief="flat"
)
settings_button.place(
    x=616.0,
    y=456.0,
    width=16.0,
    height=16.0
)

income_total: float = collect_income_total("transactions1")
canvas.itemconfig(tagOrId=income, text=f"{income_total:,.2f}€")

balance_last: float = collect_balance("transactions1")
canvas.itemconfig(tagOrId=balance, text=f"{balance_last:,.2f}€")

expense_total: float = collect_expense_total("transactions1")
canvas.itemconfig(tagOrId=expense, text=f"{expense_total:,.2f}€")

# Deactivate window resize
window.resizable(False, False) 

# Start the mainloop of the window
window.mainloop() 

# End of GUI ------------------------------------------------------------------
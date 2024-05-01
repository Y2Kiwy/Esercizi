import os
import pandas as pd
from random import randint

# Get current path and csv path for codes and accounts memorizzation
current_directory: str = os.path.dirname(os.path.abspath(__file__))
code_csv_path: str = os.path.join(current_directory, "codes.csv")
accounts_csv_path: str = os.path.join(current_directory, "accounts.csv")


def holder_code() -> int:

    ''' 
    Create a unique code to pair with each account holder
    and save it into a CSV file.
    '''

    # Check if the CSV file exists
    if not os.path.exists(code_csv_path):
        # Create it if it doesn't exist, with the header 'code'
        with open(code_csv_path, "w") as file:
            file.write('code')
    
    # If the file exists, read it
    with open(code_csv_path, "r") as file:

        # Initialize a list to store already-existing codes
        codes_list: list = []

        # Skip the header
        next(file)  
        
        # Store all the codes in the 'codes_list' list
        for line in file:
            code: int = line.strip()
            codes_list.append(int(code))

        # Generate a new code and check if it already exists
        while True:
            new_code: int = randint(999, 9999)

            # If the code already exists, restart the loop
            if new_code in codes_list:
                continue 

            # If the new code does not already exist, write it into the 'codes.csv' file
            else:
                with open(code_csv_path, "a") as file:
                    file.write("\n" + str(new_code))
                return new_code


def new_balance(account_holder: str, balance: float = 1_000.00) -> None:

    '''
    Uses pandas dataframe to write a csv file with a new balance
    
    Parameters:
        -account_holder: str -> name to attribuite to the balance
        -balance: float -> how many money does the account has. 1_000 by default
    '''

    # Create new dict with the account infos
    balance_dict: dict = {
        "code": holder_code(),
        "name": account_holder,
        "balance": balance
    }

    # Create the dataframe with the account infos
    balance_df = pd.DataFrame([balance_dict])

    # If the csv file do not exist, create it
    if not os.path.exists(accounts_csv_path):
        with open(accounts_csv_path, 'w') as file:
            file.write('code,name,balance\n')

    # Write the dataframe into the csv file
    balance_df.to_csv(accounts_csv_path, mode='a', index=False, header=False)

    print("New balance correctly created")


def remove_balance(code_to_remove) -> None:
    """
    Remove one account by its unique code
    
    Args:
        code_to_remove: int -> The code to be removed from the DataFrames.

    Returns:
        None
    """
    # Read accounts and codes DataFrames from CSV files
    accounts_df: pd.DataFrame = pd.read_csv(accounts_csv_path)
    codes_df: pd.DataFrame = pd.read_csv(code_csv_path)

    # Find indices of rows with the specified code in both DataFrames
    account_index = accounts_df.index[accounts_df['code'] == code_to_remove].tolist()
    code_index = codes_df.index[codes_df['code'] == code_to_remove].tolist()

    # If matching indices exist in both DataFrames, remove corresponding rows
    if account_index and code_index:
        accounts_df.drop(account_index, inplace=True)
        codes_df.drop(code_index, inplace=True)

        # Save updated DataFrames back to CSV files
        accounts_df.to_csv(accounts_csv_path, index=False)
        codes_df.to_csv(code_csv_path, index=False)

        print(f"Balance with code: {code_to_remove} correctly removed")
    else:
        print(f"Code {code_to_remove} not found")
    

def deposit(account_code: int, deposit_amount: int) -> None:

    """
    Deposit funds into an account with the specified account code.

    Args:
        account_code: int -> The unique code identifying the account.
        deposit_amount: float -> The amount to deposit into the account.

    Returns:
        None
    """
    # Error handling
    if not type(deposit_amount) is int:
        raise TypeError("'deposit_amount' must be int")
    if deposit_amount <= 0:
        raise ValueError("'deposit_amount' cannot be 0 or lower")

    # Read accounts and codes DataFrames from CSV files
    accounts_df: pd.DataFrame = pd.read_csv(accounts_csv_path)

    # Find indices of rows with the specified code in the DataFrames
    account_index: int = accounts_df.index[accounts_df['code'] == account_code]

    if not account_index.empty:
        # Update the balance
        accounts_df.loc[account_index, "balance"] += deposit_amount

        # Save updated DataFrames back to CSV files
        accounts_df.to_csv(accounts_csv_path, index=False)

        print(f"{deposit_amount}$ have been deposited into account {account_code}.")
    else:
        print(f"Code {account_code} not found")


def withdraw(account_code: int, withdraw_amount: int) -> None:

    """
    Withdraw funds into an account with the specified account code.

    Args:
        account_code: int -> The unique code identifying the account.
        withdraw_amount: float -> The amount to withdraw into the account.

    Returns:
        None
    """

    # Error handling
    if not type(withdraw_amount) is int:
        raise TypeError("'deposit_amount' must be int")
    if withdraw_amount <= 0:
        raise ValueError("'deposit_amount' cannot be 0 or lower")

    # Read accounts and codes DataFrames from CSV files
    accounts_df: pd.DataFrame = pd.read_csv(accounts_csv_path)

    # Find indices of rows with the specified code in the DataFrames
    account_index: int = accounts_df.index[accounts_df['code'] == account_code]

    if not account_index.empty:
        # Update the balance
        accounts_df.loc[account_index, "balance"] -= withdraw_amount

        # Save updated DataFrames back to CSV files
        accounts_df.to_csv(accounts_csv_path, index=False)

        print(f"{withdraw_amount}$ have been withdrawn from account {account_code}.")
    else:
        print(f"Code {account_code} not found")


def check_balance(account_code: int) -> None:

    """
    Withdraw funds into an account with the specified account code.

    Args:
        account_code: int -> The unique code identifying the account.
        withdraw_amount: float -> The amount to withdraw into the account.

    Returns:
        None
    """

    # Error handling
    if not type(account_code) is int:
        raise TypeError("'deposit_amount' must be int")

    # Read accounts DataFrame from CSV file
    accounts_df: pd.DataFrame = pd.read_csv(accounts_csv_path)

    # Find the row with the specified code in the DataFrame
    account_row: int = accounts_df[accounts_df['code'] == account_code]

    if not account_row.empty:
        # Get the balance from the account row
        current_balance: int = account_row.iloc[0]["balance"]
        print(f"The balance of account {account_code} is ${current_balance:.2f}")
    else:
        print(f"Account with code {account_code} not found")
~~Managing the data storage process and interaction with the application.~~ -> **Correct on 06/05/2024 22:53**
    Add options to edit the database data (start balance above all)

Finding a way to address the application's blur issue caused by window scaling, for example on laptops (HP 250 15.6-inch G9 Notebook PC by default has a scaling of 125%).

~~Handling the case where commas are used instead of periods for decimals.~~ -> **Correct on 06/05/2024 14:49**

Adding the options screen.
    Temporaly made this through hidden commands in 'name' label:
        - '!balance:*balance_amount*' -> Edit the start balance, only possible at the first launch of the app
        - '!delete:*rowid*' -> Delete the specific transaction from the database
        - '!edit:*rowid*:*attribute*:*new_value* -> Edit specific data about specific transaction
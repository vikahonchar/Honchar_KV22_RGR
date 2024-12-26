from tabulate import tabulate

class View:
    def show_message(self, message):
        print(message)

    def show_data(self, data, columns, query=None):
        if query:
            print(f"SQL query used: {query}")  # Log the SQL query used
        print(tabulate(data, headers=columns, tablefmt="psql"))

    def get_table_name(self):
        return input("Enter table name: ")

    def get_columns_input(self):
        columns = input("Enter columns separated by space: ").split()
        return columns

    def get_condition_input(self):
        condition = input("Enter condition in PostgreSQL syntax (... WHERE [condition]). If none, leave empty: ")
        return condition if condition else None

    def get_insert_input(self):
        table = input("Enter table name: ")
        columns = input("Enter columns separated by space: ").split()
        data = input("Enter data separated by space: ").split()
        return table, columns, data

    def get_update_input(self):
        table = input("Enter table name: ")
        data = input("Enter data separated by space: ").split()
        condition = input("Enter condition in PostgreSQL syntax (... WHERE [condition]). If none, leave empty: ")
        return table, data, condition if condition else None

    def get_delete_input(self):
        table = input("Enter table name: ")
        condition = input("Enter condition in PostgreSQL syntax (... WHERE [condition]). Can not be empty: ")
        if not condition:
            raise ValueError("Condition cannot be empty!")
        return table, condition

    def get_create_input(self):
        table = input("Enter table name: ")
        columns = input("Enter columns separated by space: ").split()
        data_types = input("Enter data types separated by space: ").split()
        return table, columns, data_types

    def get_drop_input(self):
        table = input("Enter table name: ")
        return table

    def get_generate_random_input(self):
        table = input("Enter table name: ")
        columns = input("Enter columns separated by space: ").split()
        data_types = input("Enter data types separated by space: ").split()
        parameters = input("Enter parameters separated by space: ").split()
        parameters = [tuple(parameter.split(",")) for parameter in parameters]
        rows_number = int(input("Enter number of rows: "))
        text_len = int(input("Enter length of text columns (optional, press Enter to skip): ") or 0)
        return table, columns, data_types, parameters, rows_number, text_len

    def get_find_input(self):
        table = input("Enter table name: ")
        column = input("Enter column name: ")
        t = input("Enter search type (number, string, boolean, date): ")
        condition = ""

        if t == "number":
            left = input("Enter left bound: ")
            right = input("Enter right bound: ")
            condition = f"{column} BETWEEN {left} AND {right}"
        elif t == "string":
            string = input("Enter substring or pattern: ")
            condition = f"{column} LIKE '%{string}%'"
        elif t == "boolean":
            boolean = input("Enter boolean value (True/False): ")
            condition = f"{column} = {boolean}"
        elif t == "date":
            left = input("Enter start date (YYYY-MM-DD): ")
            right = input("Enter end date (YYYY-MM-DD): ")
            condition = f"{column} BETWEEN '{left}' AND '{right}'"

        return table, column, condition if condition else None

    def get_pay_systems_total_income_input(self):
        left = input("Enter left bound: ")
        right = input("Enter right bound: ")
        return left, right

    def get_company_orders_thru_period_input(self):
        left = input("Enter start date (YYYY-MM-DD): ")
        right = input("Enter end date (YYYY-MM-DD): ")
        return left, right

    def get_top_5_orders_total_price_input(self):
        company = input("Enter company name: ")
        return company
from model import Model
from view import View

class Controller:
    def __init__(self, db_name, user, password, host):
        self.model = Model(db_name, user, password, host)
        self.view = View()

    def run(self):
        while True:
            self.show_tables()
            choice = self.show_menu()
            if choice == "1":
                self.insert_data()
            elif choice == "2":
                self.view_data()
            elif choice == "3":
                self.update_data()
            elif choice == "4":
                self.delete_data()
            elif choice == "5":
                self.create_table()
            elif choice == "6":
                self.drop_table()
            elif choice == "7":
                self.generate_random_data()
            elif choice == "8":
                self.find_data()
            elif choice == "9":
                self.show_algorithms()
            elif choice == "0":
                break
            else:
                self.view.show_message("Invalid choice!")

    def show_tables(self):
        tables = self.model.get_tables()
        tables = [table[0] for table in tables] if tables else None
        self.view.show_message(f"Available tables: {tables if tables else 'None'}")

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Insert Data")
        self.view.show_message("2. View Data")
        self.view.show_message("3. Update Data")
        self.view.show_message("4. Delete Data")
        self.view.show_message("5. Create Table")
        self.view.show_message("6. Drop Table")
        self.view.show_message("7. Generate Random Data")
        self.view.show_message("8. Find Data")
        self.view.show_message("9. Algorithms")
        self.view.show_message("0. Quit")
        return input("Enter your choice: ")

    def insert_data(self):
        table, columns, data = self.view.get_insert_input()
        if self.model.insert_data(table, columns, data):
            self.view.show_message("Data inserted successfully!")
        else:
            self.view.show_message("Failed to insert data.")

    def view_data(self):
        table = self.view.get_table_name()
        columns = self.model.get_columns(table)
        if columns is None:
            self.view.show_message("Failed to retrieve column names.")
            return
        columns = [column[0] for column in columns]
        self.view.show_message(f"Available columns: {', '.join(columns)}")
        selected_columns = self.view.get_columns_input()
        condition = self.view.get_condition_input()
        data = self.model.get_data(table, selected_columns, condition)
        query = f"SELECT {', '.join(selected_columns)} FROM {table} WHERE {condition}" if condition else f"SELECT {', '.join(selected_columns)} FROM {table}"
        if data is not None:
            self.view.show_data(data, selected_columns, query)
        else:
            self.view.show_message("Failed to retrieve data.")

    def update_data(self):
        table, data, condition = self.view.get_update_input()
        if self.model.update_data(table, data, condition):
            self.view.show_message("Data updated successfully!")
        else:
            self.view.show_message("Failed to update data.")

    def delete_data(self):
        table, condition = self.view.get_delete_input()
        if self.model.delete_data(table, condition):
            self.view.show_message("Data deleted successfully!")
        else:
            self.view.show_message("Failed to delete data.")

    def create_table(self):
        table, columns, data_types = self.view.get_create_input()
        if self.model.create_table(table, columns, data_types):
            self.view.show_message("Table created successfully!")
        else:
            self.view.show_message("Failed to create table.")

    def drop_table(self):
        table = self.view.get_drop_input()
        if self.model.drop_table(table):
            self.view.show_message("Table dropped successfully!")
        else:
            self.view.show_message("Failed to drop table.")

    def generate_random_data(self):
        table, columns, data_types, parameters, rows_number, text_len = self.view.get_generate_random_input()
        if self.model.generate_random_data(table, columns, data_types, parameters, rows_number, text_len):
            self.view.show_message("Random data generated successfully!")
        else:
            self.view.show_message("Failed to generate random data.")

    def find_data(self):
        table, column, condition = self.view.get_find_input()
        data = self.model.get_data(table, [column], condition)
        if data is not None:
            self.view.show_data(data, [column])
        else:
            self.view.show_message("Failed to retrieve data.")

    def show_algorithms(self):
        self.view.show_message("\nAlgorithms:")
        self.view.show_message("1. Calculate Total Income")
        self.view.show_message("2. Orders Within a Period")
        self.view.show_message("3. Top 5 Orders by Total Price")
        self.view.show_message("0. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.calculate_total_income()
        elif choice == "2":
            self.orders_within_period()
        elif choice == "3":
            self.top_5_orders()

    def calculate_total_income(self):
        left, right = self.view.get_pay_systems_total_income_input()
        data = self.model.pay_systems_total_income(left, right)
        if data:
            self.view.show_data(data, ["ID", "Name", "Count", "Total Income"])
        else:
            self.view.show_message("Failed to calculate total income.")

    def orders_within_period(self):
        left, right = self.view.get_company_orders_thru_period_input()
        data = self.model.company_orders_thru_period(left, right)
        if data:
            self.view.show_data(data, ["ID", "Company", "Orders"])
        else:
            self.view.show_message("Failed to retrieve orders within period.")

    def top_5_orders(self):
        company = self.view.get_top_5_orders_total_price_input()
        data = self.model.top_5_orders_total_price(company)
        if data:
            self.view.show_data(data, ["Order ID", "Total Price"])
        else:
            self.view.show_message("Failed to retrieve top 5 orders.")

import json
from prettytable import PrettyTable
def create_table(data):
    # Create a table
    table = PrettyTable()
    table.field_names = ["Product Name", "Price", "Mobile Internet", "TV", "Internet Speed", "Minutes"]

    # Add each product as a row in the table
    for product_name, product_details in data.items():
        price = product_details.get("product_price", "")
        mobile_internet = product_details.get("product_mobile_internet", "")
        tv = product_details.get("product_TV", "")
        internet_speed = product_details.get("product_intenet_speed", "")
        minutes = product_details.get("product_minutes", "")

        # Add the row to the table
        table.add_row([product_name, price, mobile_internet, tv, internet_speed, minutes])

    # Convert the table to JSON
    table_data = {
        'table_header': table.field_names,
        'table_rows': table.get_string().split("\n")[3:-1]
    }

    # Write the table data to a JSON file
    with open("../parser_MTS/data/table_output.json", "w", encoding = 'utf-8') as file:
        json.dump(table_data, file, indent=4, ensure_ascii=False)


    print(table)




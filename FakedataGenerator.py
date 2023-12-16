import os
import pandas as pd
from faker import Faker

def generate_custom_fake_data(columns, rows):
    fake = Faker()
    data = {column: [] for column in columns}

    for _ in range(rows):
        for column in columns:
            if "name" in column.lower():
                data[column].append(fake.name())
            elif "email" in column.lower():
                data[column].append(fake.email())
            elif "country" in column.lower():
                data[column].append(fake.country())
            elif "address" in column.lower():
                data[column].append(fake.address())
            elif "date_of_birth" in column.lower():
                data[column].append(fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'))            
            else:
                print(f"Invalid column name: {column}")

    return pd.DataFrame(data)

def save_to_file(dataframe, filename, file_format):
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    if file_format == "csv":
        output_path = os.path.join(output_folder, f"{filename}.csv")
        dataframe.to_csv(output_path, index=False)
    elif file_format == "xlsx":
        output_path = os.path.join(output_folder, f"{filename}.xlsx")
        dataframe.to_excel(output_path, index=False)
    elif file_format == "json":
        output_path = os.path.join(output_folder, f"{filename}.json")
        dataframe.to_json(output_path, orient="records")
    else:
        print(f"Unsupported file format: {file_format}")
        return

    print(f"File '{output_path}' created successfully.")

def main():
    # User input
    columns_input=[]
    columns_input = input("Enter column names (comma-separated): ").split(",")
    rows_input = int(input("Enter the number of rows: "))
    filename_input = input("Enter the filename (without extension): ")
    file_format_input = input("Enter the file format (csv, xlsx, json): ").lower()

    # Generate custom fake data
    custom_fake_data = generate_custom_fake_data(columns_input, rows_input)

    # Save to CSV file
    if custom_fake_data is not None:
        save_to_file(custom_fake_data, filename_input, file_format_input)

if __name__ == "__main__":
    main()

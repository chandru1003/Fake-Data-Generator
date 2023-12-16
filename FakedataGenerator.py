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
            elif "address" in column.lower():
                data[column].append(fake.address())
            elif "date_of_birth" in column.lower():
                data[column].append(fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'))
            else:
                print(f"Invalid column name: {column}")

    return pd.DataFrame(data)

def save_to_csv(dataframe, filename):
    dataframe.to_csv(f"{filename}.csv", index=False)
    print(f"File '{filename}.csv' created successfully.")

def main():
    # User input
    columns_input=[]
    columns_input = input("Enter column names (comma-separated): ").split(",")
    rows_input = int(input("Enter the number of rows: "))
    filename_input = input("Enter the filename (without extension): ")

    # Generate custom fake data
    custom_fake_data = generate_custom_fake_data(columns_input, rows_input)

    # Save to CSV file
    if custom_fake_data is not None:
        save_to_csv(custom_fake_data, filename_input)

if __name__ == "__main__":
    main()

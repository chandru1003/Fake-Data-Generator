import os
import json
import pandas as pd
import requests

def generate_custom_fake_data(api_key, fields, rows, file_format):
    # Construct the Mockaroo API URL
    url = f'https://api.mockaroo.com/api/generate.json?key={api_key}'
            

    # Send the request to the Mockaroo API
    response = requests.post(url, json={'fields': fields, 'count': rows})

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print(f"Failed to fetch fake data. Status code: {response.status_code}")
        return None

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
    api_key_input = "<apiKey>"

    # User input for fields
    fields_input = []
    while True:
        field_name = input("Enter column name (or type 'done' to finish): ")
        if field_name.lower() == 'done':
            break

        field_type = input("Enter data type: ")
        field = {"name": field_name, "type": field_type}

        # Additional parameters based on data type
        if field_type == 'Custom List':
            values = input("Enter values (comma-separated): ").split(",")
            field["values"] = values

        fields_input.append(field)  # This line should be inside the while loop

    
    rows_input = int(input("Enter the number of rows: "))
    filename_input = input("Enter the filename (without extension): ")
    file_format_input = input("Enter the file format (csv, xlsx, json): ").lower()

    # Generate JSON representation of fields
    fields_json = json.dumps(fields_input)

    # Generate custom fake data
    custom_fake_data = generate_custom_fake_data(api_key_input, fields_json, rows_input, file_format_input)

    # Save to file
    if custom_fake_data is not None:
        save_to_file(custom_fake_data, filename_input, file_format_input)

if __name__ == "__main__":
    main()

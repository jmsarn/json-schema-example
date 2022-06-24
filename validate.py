import csv
import json

from jsonschema import validate, ValidationError


def main():
    """Validate CSV of addresses"""
    with open("schema.json") as f:
        schema = json.load(f)

    with open("addresses.csv") as f:
        data = [{k: v for k, v in row.items()} for row in csv.DictReader(f)]

    for i, row in enumerate(data):
        try:
            validate(row, schema)
        except ValidationError as e:
            print(f"Error in row {i+1}")
            print(e)
            print(row)


if __name__ == "__main__":
    main()

import csv
from faker import Faker

def generate_csv(schema, num_rows=100):
    fake = Faker()
    column_generators = {
        "string": fake.name,
        "integer": fake.random_int,
        "date": fake.date,
    }

    output = []
    for _ in range(num_rows):
        row = {col.name: column_generators[col.data_type]() for col in schema.columns.all()}
        output.append(row)

    return output

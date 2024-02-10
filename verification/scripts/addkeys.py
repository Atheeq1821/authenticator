import csv
from verification.models import SerialKey
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'keys.csv')
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    s=0
    for row in reader:
        key_value = row['Keys']
        s+=1
        if s==5:
            exit()
        # Create SerialKey object and save to the database
        SerialKey.objects.create(key=key_value, used_time=0)

print("Keys imported successfully.")
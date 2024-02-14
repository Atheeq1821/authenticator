import csv
from verification.models import SerialKey
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'keys.csv')
def run():
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        s=0
        for row in reader:
            try:
                key_value = row['Keys']
                SerialKey.objects.create(key=key_value, used_time=0)
                s+=1
            except :
                continue    
            # Create SerialKey object and save to the database
        

    print("Keys imported successfully.")
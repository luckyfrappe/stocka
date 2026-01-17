import os
import csv
from django.utils.dateparse import parse_datetime
from products.models import Product

# Entire file is Written by Gemini AI by Google
# I added more logging and error handling for debugging and different attempts

print("Script Started: Checking files...")

PRODUCT_CSV = 'dataset/outfits.csv'

if not os.path.exists(PRODUCT_CSV):
    print(f"ERROR: File not found at {PRODUCT_CSV}")
else:
    with open(PRODUCT_CSV, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        reader.fieldnames = [n.strip().replace('\ufeff', '') for n in reader.fieldnames if n]
        
        print(f"Headers found: {reader.fieldnames}")
        print("Patching database records (this is much faster than the first import)...")
        
        count = 0
        for row in reader:
            sku = row.get('id')
            raw_date = row.get('timeCreated') 
            
            if sku and raw_date:
                dt = parse_datetime(raw_date.strip())
                if dt:
                    Product.objects.filter(sku=sku).update(time_created=dt)
                    count += 1
            
            if count % 2000 == 0 and count > 0:
                print(f"Progress: {count} timestamps updated")
    print(f"---")
    print(f"FINISHED! Updated {count} products with their original creation dates.")
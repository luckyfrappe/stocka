import os
import csv
import ast

# Entire file is written by Gemini AI by Google
# I added more logging and error handling for debugging and different attempts


def import_data():
    # 1. PRE-FLIGHT CHECK
    print("--- 1. PRE-FLIGHT CHECK ---")
    current_dir = os.getcwd()
    print(f"Current Working Directory: {current_dir}")

    product_path = os.path.join(current_dir, 'dataset', 'outfits.csv')
    image_path = os.path.join(current_dir, 'dataset', 'picture_triplets.csv')

    print(f"Checking for Product CSV at: {product_path}")
    print(f"Found Product CSV? {os.path.exists(product_path)}")
    print(f"Checking for Image CSV at: {image_path}")
    print(f"Found Image CSV? {os.path.exists(image_path)}")

    if not os.path.exists(product_path):
        print("ABORTING: Cannot find outfits.csv")
        return

    # 2. DELAYED IMPORTS (Prevents script from dying if models aren't ready)
    print("\n--- 2. LOADING DJANGO MODELS ---")
    try:
        from django.utils.text import slugify
        from django.db import transaction
        from products.models import (
            Product,
            AttributeType,
            AttributeValue,
            ProductAttribute,
            ProductImage
        )
        print("Models loaded successfully")
    except ImportError as e:
        print(f"ERROR: Could not import models. Is your app name correct? {e}")
        return

    # 3. MAP IMAGES
    image_map = {}
    with open(image_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            row = {k.strip(): v for k, v in row.items() if k}
            oid = row.get('outfit.id')
            if oid:
                if oid not in image_map:
                    image_map[oid] = []
                image_map[oid].append({
                    'file': row.get('file_name'),
                    'order': int(row.get('displayOrder', 0))
                })
    print(f"Mapped {len(image_map)} images.")

    print("\n--- 3. IMPORTING DATA ---")
    with open(product_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        # Clean the headers
        reader.fieldnames = [
            n.strip().replace('\ufeff', '') for n in reader.fieldnames if n
        ]

        with transaction.atomic():
            count = 0
            for row in reader:
                # Clean row
                row = {k.strip(): v.strip() for k, v in row.items() if k}
                sku = row.get('id')

                if not sku:
                    continue

                product, _ = Product.objects.update_or_create(
                    sku=sku,
                    defaults={
                        'name': row.get('name', 'No Name'),
                        'description': row.get('description', ''),
                        'retail_price': float(row.get('retailPrice') or 0),
                        'price_per_week': float(row.get('pricePerWeek') or 0),
                    }
                )

                # Attributes
                try:
                    tags = ast.literal_eval(row.get('outfit_tags', '[]'))
                    cats = ast.literal_eval(row.get('tag_categories', '[]'))
                    for c_name, t_val in zip(cats, tags):
                        t_obj, _ = AttributeType.objects.get_or_create(
                            name=c_name,
                            defaults={'slug': slugify(c_name)}
                        )
                        v_obj, _ = AttributeValue.objects.get_or_create(
                            attribute_type=t_obj,
                            value=t_val,
                            defaults={'slug': slugify(t_val)}
                        )
                        ProductAttribute.objects.get_or_create(
                            product=product,
                            attribute_value=v_obj
                        )
                except Exception as e:
                    print(f"Error processing attributes for SKU {sku}: {e}")

                # Images
                if sku in image_map:
                    for img in image_map[sku]:
                        ProductImage.objects.get_or_create(
                            product=product,
                            image=img['file'],
                            defaults={
                                'sort_order': img['order'],
                                'is_primary': (img['order'] == 0)
                            }
                        )

                count += 1
                if count % 100 == 0:
                    print(f"Progress: {count} items imported")

    print(f"FINISHED! Total imported: {count}")


import_data()

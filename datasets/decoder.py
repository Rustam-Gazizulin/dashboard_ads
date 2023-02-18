import csv
import json

def convert_to_json(csv_file, json_file, model_name):
    mydata = []

    with open(csv_file, encoding='utf-8') as csvfile:
        for row in csv.DictReader(csvfile):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}

            if 'Id' in row:
                del row['Id']
            else:
                del row['id']

            if 'price' in row:
                row['price'] = int(row['price'])
            if "is_published" in row:
                if row["is_published"] == 'TRUE':
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if 'age' in row:
                row['age'] = int(row['age'])
            # if 'location_id' in row:
            #     row['location_id'] = int(row['location_id'])
            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])
            # if 'category_id' in row:
            #     row['category_id'] = int(row['category_id'])
            if 'lat' in row:
                row['lat'] = float(row['lat'])
            if 'lng' in row:
                row['lng'] = float(row['lng'])


            to_add['fields'] = row
            mydata.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, ensure_ascii=False))


ads_csv = r'ads.csv'
ads_json = r'ads.json'

model = 'ads.ads'
model_cat = 'ads.category'
model_user = 'users.user'
model_location = 'users.location'

categories_csv = r'categories.csv'
categories_json = r'categories.json'

location_csv = r'location.csv'
location_json = r'location.json'

user_csv = r'user.csv'
user_json = r'user.json'

# convert_to_json(location_csv, location_json, model_location)
# convert_to_json(user_csv, user_json, model_user)
convert_to_json(ads_csv, ads_json, model)
convert_to_json(categories_csv, categories_json, model_cat)
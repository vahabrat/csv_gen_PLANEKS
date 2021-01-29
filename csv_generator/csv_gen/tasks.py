from __future__ import absolute_import, unicode_literals
import random
import uuid
from celery import shared_task
import csv
from .models import DataSet, Schema, Column, FakeDate, FakeIpAddress, FakeCompanyName, FakePhoneNumber


@shared_task
def generate_csv(row_number,schema_id, set_id):
    unique_filename = str(uuid.uuid4())
    print(unique_filename)
    columns = Column.objects.filter(schema=schema_id,).order_by('column_order')
    schema = Schema.objects.get(id = schema_id)
    write = []
    rows = 1
    while rows <= row_number:
        rows += 1
        row = []
        for column in columns:

            if column.column_type == 'integer':
                random_number = random.randint(int(column.column_type_option_from), int(column.column_type_option_to))
                row.append(random_number)
            elif column.column_type == 'company_name':
                random_company_name = random.choice(FakeCompanyName.objects.all())
                row.append(random_company_name.fake_company_name)
            elif column.column_type == 'phone_number':
                random_phone_number = random.choice(FakePhoneNumber.objects.all())
                row.append(random_phone_number.fake_phone_number)
            elif column.column_type == 'address':
                random_ip_address = random.choice(FakeIpAddress.objects.all())
                row.append(random_ip_address.fake_ip_address)
            elif column.column_type == 'data':
                random_date = random.choice(FakeDate.objects.all())
                row.append(random_date.fake_date)
        write.append(row)
        print(write)
        print(row_number)
    with open(f'/code/csv_generator/media/csvs/{unique_filename}.csv', 'wt', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=f'{schema.schema_delimiter}', quotechar=f'{schema.schema_string_character}')

        writer.writerow([column.column_name for column in columns])
        writer.writerows(write)
    DataSet.objects.filter(id=set_id).update(csv_file = f'/code/csv_generator/media/csvs/{unique_filename}.csv', is_ready = True)
                #writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])




        #print(random.choice(column.column_type_option_from))
        #print(random.randint(foo))
    '''
    with open('/code/csv_generator/media/csvs/FAKE_DATA.csv', 'rt') as fout:
        spamreader = csv.reader(fout, delimiter=' ', quotechar='|')
        for row in spamreader:
            to_string = ', '.join(row)
            extracted_items = to_string.split(',')
            FakeDate.objects.create(date=extracted_items[0])
            FakeIpAddress.objects.create(fake_ip_address=extracted_items[1])
            FakeCompanyName.objects.create(company_name=extracted_items[2])
            FakePhoneNumber.objects.create(phone_number=extracted_items[3])
            print(extracted_items[3])
            #list_updated=[', '.join(row).split(',') for row in spamreader]
    '''


        # a context manager
        #filename = "%s.csv" % generate_file.request.id
        #cout = csv.DictWriter(fout, ['first', 'last'])
        #cout.writeheader()
        #cout.writerows(villains)

        #csvout = csv.writer(fout)

        #csvout.writerows(villains)


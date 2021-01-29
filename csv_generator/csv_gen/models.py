from django.db import models
from django.contrib.auth import get_user_model

class Schema(models.Model):

    COMMA = ','
    PERCENTAGE = '%'
    SLASH = '/'
    EXCLAMATION_MARK = '!'
    DOUBLE_QUOTE = '"'
    COMMERCIAL_AT = '@'
    AMPERSAND = '&'

    DELIMITER_GROUP = {
        (COMMA, ','),
        (SLASH, '/'),
        (PERCENTAGE, "%"),
        (EXCLAMATION_MARK, '!'),
    }
    CHARACTER_GROUP = {
        (DOUBLE_QUOTE, '"'),
        (COMMERCIAL_AT, '@'),
        (AMPERSAND, '&'),
    }
    schema_name=models.CharField(max_length=50,)
    schema_delimiter=models.CharField(max_length=1, choices=DELIMITER_GROUP, null=True)
    schema_string_character=models.CharField(max_length=1, choices=CHARACTER_GROUP, null=True)
    date_creation = models.DateTimeField('Дата создания схемы', auto_now_add=True)
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='schemas')


class Column(models.Model):

    INTEGER = 'integer'
    PHONE_NUMBER = 'phone_number'
    COMPANY_NAME = 'company_name'
    ADDRESS = 'address'
    DATE = 'date'

    TYPES = {

        ('integer', 'integer'),
        ('phone_number', 'phone_number'),
        ('company_name', 'company_name'),
        ('address', 'address'),
        ('date', 'date'),
    }
    column_name = models.CharField(max_length=50, null=False)
    column_type = models.CharField(max_length=30,
                                   choices = (('integer', 'integer'),
                                    ('phone_number', 'phone_number'),
                                    ('company_name', 'company_name'),
                                    ('address', 'address'),
                                    ('date', 'date')),
                                   null=False)

    column_type_option_from=models.IntegerField(blank=True, null=True)
    column_type_option_to=models.IntegerField(blank=True, null=True)

    column_order=models.IntegerField(get_user_model())
    schema=models.ForeignKey(Schema, on_delete=models.CASCADE,related_name='columns')

class DataSet(models.Model):
    creation_date=models.DateTimeField('Дата создания сэта', auto_now_add=True)
    csv_file=models.FileField(upload_to='csvs/',blank=True)
    is_ready=models.BooleanField(default=False)
    schema=models.ForeignKey(Schema, on_delete=models.CASCADE,related_name='sets')


class FakePhoneNumber(models.Model):
    fake_phone_number=models.CharField("номер_телефона", max_length=20)

class FakeDate(models.Model):
    fake_date=models.CharField("дата", max_length=10)

class FakeIpAddress(models.Model):
    fake_ip_address = models.CharField("дата", max_length=15)

class FakeCompanyName(models.Model):
    fake_company_name = models.CharField("название_компании", max_length=50)
# Create your models here.

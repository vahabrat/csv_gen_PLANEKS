from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ColumnForm
from .models import Schema,Column,DataSet

from .tasks import generate_csv

def data_schemas(request):
    context={}
    schemas=Schema.objects.filter(user_id=request.user)
    context['schemas'] = schemas

    #generate_csv()

    return render(request,'csv_gen/data_schemas.html',context)


def edit_schema(request, schema_id):
    context = {}
    schema=Schema.objects.get(pk=schema_id)
    columns=Column.objects.filter(schema=schema_id)
    column_form = ColumnForm()
    context['schema'] = schema
    context['columns'] = columns
    context['column_form'] = column_form
    print(context)
    #generate_csv()
    return render(request,'csv_gen/edit_schema.html',context)


@login_required
def new_schema(request):
    context={}
    column_form = ColumnForm()
    context['column_form'] = column_form
    if request.method == 'POST':
        column_numbers = request.POST.getlist('column_numbers[]')  # [1,2,4]
        print(column_numbers)
        schema = Schema.objects.create(schema_name = request.POST['schema_name'], schema_delimiter = request.POST['delimiter'], schema_string_character = request.POST['string_character'], user=request.user)
        for column_number in column_numbers:
            column_name = request.POST[f'column_name_{column_number}']
            column_type = request.POST[f'type_{column_number}']

            try:
                column_option_from = int(request.POST[f'option_from_{column_number}'])
            except ValueError:
                column_option_from = None
            try:
                column_option_to = int(request.POST[f'option_to_{column_number}'])
            except ValueError:
                column_option_to = None
            except KeyError:
                print('нет такого ключа')




            column_order = request.POST[f'order_{column_number}']
            Column.objects.create(column_name = column_name, column_type = column_type, column_type_option_from = column_option_from, column_type_option_to = column_option_to, column_order = column_order, schema = schema)





    return render(request,'csv_gen/new_schema.html', context)


def create_data_sets(request,schema_id):
    context={}
    sets=DataSet.objects.filter(schema=schema_id)
    context['sets'] = sets



    if request.method == 'POST':
        row_number = int(request.POST['number_of_rows'])
        print(row_number)
        set=DataSet.objects.create(schema_id=schema_id)

        generate_csv(row_number,schema_id, set.id)
    return render(request,'csv_gen/data_sets.html', context)

def delete_data_set(request, set_id):
    #print(set_id)
    context = {}
    #set = DataSet.objects.filter(id=set_id)
    #print(set_id)
    DataSet.objects.filter(id=set_id).delete()
    #schema = Schema.objects.get(sets__in=set)
    #sets = DataSet.objects.filter(schema=schema.id)
    #context['sets'] = sets

    #set = DataSet.objects.filter(id=set_id)

    #print(schema.id)
    return HttpResponseRedirect("/data_schemas")

def log_in(request):
    context = {}
    return render(request,'csv_gen/login.html', context)
# Create your views here.

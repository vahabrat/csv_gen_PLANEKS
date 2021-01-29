from django.urls import path
from . import views

app_name = 'csv'

urlpatterns = [

    path('data_schemas', views.data_schemas, name='data_schemas'),
    path('new_schema', views.new_schema, name='new_schema'),
    path('<int:schema_id>/create_data_sets', views.create_data_sets, name='create_data_sets'),
    path('<int:schema_id>/edit_schema/', views.edit_schema, name='edit_schema'),
    path('<int:set_id>/delete/', views.delete_data_set, name='delete_data_set'),
    #path('post/<int:post_id>', views.post, name='post'),
    #path('post/<int:post_id>', views.NewPost.as_view(), name='post'),

]
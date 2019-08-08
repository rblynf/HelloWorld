from django.urls import path
from . import view,testdb
 
urlpatterns = [
    path('hello/', view.hello),
    path('testdb/show', testdb.show),
    path('testdb/create', testdb.create),
    path('testdb/update', testdb.update),
    path('testdb/delete', testdb.delete),
]
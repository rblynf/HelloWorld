from django.urls import path
from . import view,testdb,search,search2
 
from django.contrib import admin

urlpatterns = [
    path('hello/', view.hello),
    path('testdb/show', testdb.show),
    path('testdb/create', testdb.create),
    path('testdb/update', testdb.update),
    path('testdb/delete', testdb.delete),
    path('search_get/', search.search),
    # path('search_post/', search2.search_post),
    path('search_post/', search.search_post),

    #自带
    path('admin/', admin.site.urls)
]
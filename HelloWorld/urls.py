# from django.conf.urls import url
 
# from . import view
 
# urlpatterns = [
#     url(r'^$', view.hello),
# ]



from django.urls import path
 
from . import view
 
urlpatterns = [
    path('hello/', view.hello),
]
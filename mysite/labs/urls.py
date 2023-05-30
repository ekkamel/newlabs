from django.contrib import admin
from django.urls import path
from . import views

app_name = 'labs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.labs_list, name='labs_list')
]
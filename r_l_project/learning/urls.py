# Workflow 4 -> urls.py/project for workflow 5
from django.conf.urls import url
from learning import views

app_name = 'learning'

urlpatterns = [
    url('register/$', views.register,name='register'),
    url('user_login/',views.user_login,name="user_login"),
]
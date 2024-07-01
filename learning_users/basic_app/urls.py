from django.urls import path,re_path
from basic_app import views

#TEMPLATE URLS!
app_name='basic_app'

urlpatterns=[
   re_path('^register/',views.register,name='register'),
   re_path('^userlogin/',views.user_login,name='userlogin')
]
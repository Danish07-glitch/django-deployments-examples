from django.conf.urls import url
from tester import views

urlpatterns = [
    url(r'^$',views.users,name='users')
]

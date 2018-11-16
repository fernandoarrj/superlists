from accounts import views 

from django.conf.urls import url

urlpatterns = [
    url('^send_login_email$', views.send_login_email, name='send_login_email'  ),
    url('^login$', views.login, name='login')
]

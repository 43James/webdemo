from users import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('add_user/', views.add_user, name='add_user'),
    path('logout/', views.logout_user, name='logout'),
    

]
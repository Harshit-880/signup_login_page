from django.urls import path
from .views import signup_view, login_view, dashboard_view,logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

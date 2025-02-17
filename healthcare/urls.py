from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account.views import signup_view, login_view, dashboard_view,logout_view,home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

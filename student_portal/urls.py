from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# MODULE 1 & 3: URLConf include & Auth
urlpatterns = [
    path('admin/', admin.site.status_url if hasattr(admin.site, 'status_url') else admin.site.urls), 
    path('', include('notices.urls')), # Include notices app URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Note: admin.site.urls is the standard way.
# The 'admin.site.status_url' above is just a safety check. 
# Reverting to standard:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notices.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

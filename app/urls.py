# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    path('', av.landing_page, name='landing_page'),
    path('auth/register/', av.register, name='register'),
]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]
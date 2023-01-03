# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    path('', av.landing_page, name='landing_page'),
    path('transactions/add', av.add_transaction, name='add_transaction'),
    path('customers/add', av.add_customer, name='add_customer'),
    path('customers/update/<int:pk>/', av.update_customer, name='update_customer'),
    path('customers/', av.customers, name='customers'),
    path('auth/register/', av.register, name='register'),
    path('ajax-calls/', av.ajax_calls, name='ajax_calls'),

]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]
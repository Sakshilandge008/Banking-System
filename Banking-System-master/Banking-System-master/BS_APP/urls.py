from django.urls import path
from .views import home, user, transfer, add_transfer, history, add_user

urlpatterns = [
    path('', home, name='home'),
    path('users/', user, name='users'),
    path('transfer/<int:pk>', transfer, name='transfer'),
    path('add_transfer/<int:pk>', add_transfer, name='add_transfer'),
    path('history/', history, name='history'),

    # ✅ ADD USER PAGE
    path('add-user/', add_user, name='add_user'),
]

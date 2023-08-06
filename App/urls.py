from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('see_profile/<int:id>/', see_profile, name='see_profile'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
    path('delete/<int:id>', delete, name='delete'),

]

from .views import *
from django.urls import path
from .views import Users_View

urlpatterns = [
    path('', index),
    path('reg/', reg),
    path('auth/', auth),
    path('users/', Users_View),

]

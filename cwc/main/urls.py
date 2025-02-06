from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home_page'),
    
    path('login/', login, name='login_page'),
    path('register/', register, name='register_page'),
    path('logout/', logout, name='logout'),
    
    path('add-criminal/', add_criminal, name='add_criminal'),
    path('edit-criminal/', edit_criminal, name='edit_criminal'),
    path('view-criminal/', view_criminal, name='view_criminal'),
    
    path('dashboard/', dashboard, name='dashboard'),
    
    path('lodge-complaint/', lodge_complaint, name='lodge_complaint'),
    path('view-complaint/', view_complaint, name='view_complaint'),
    path('update-complaint/', update_complaint, name='update_complaint'),
]

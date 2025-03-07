from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home_page'),
    
    path('login/', login_user, name='login_page'),
    path('register/', register_user, name='register_page'),
    path('logout/', logout_user, name='logout'),
    
    path('add-criminal/', add_criminal, name='add_criminal'),
    path('edit-criminal/<int:criminal_id>/', edit_criminal, name='edit_criminal'),
    path('view-criminal/', view_criminal, name='view_criminal'),
    
    path('dashboard/', dashboard, name='dashboard'),
    
    path('lodge-complaint/', lodge_complaint, name='lodge_complaint'),
    path('view-complaint/', view_complaint, name='view_complaint'),
    path('update-complaint/<int:complaint_id>', update_complaint, name='update_complaint'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import register_page, login_page, logout_view
from django.contrib.admin.views.decorators import staff_member_required
app_name = 'accounts'

urlpatterns = [
    path('register/', staff_member_required(register_page, login_url='accounts:login'), name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout')
]

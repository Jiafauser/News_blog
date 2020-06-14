from django.urls import path
from . import views
app_name = 'verifications'
urlpatterns = [
    path('image_codes/<uuid:image_code_id>/', views.ImageCode.as_view(), name='image_codes'),

]
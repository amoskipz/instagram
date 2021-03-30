from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('messages/', views.messages,name='messages'),
    path('newprofile/',views.profile, name ='profile'),
    path('showprofile/<int:pk>/', views.display_profile,name = 'showprofile'),
    path('image/', views.add_image, name='upload_image'),
    path('search/',views.search, name='search'),
    path('explore/', views.explore, name='explore'),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('like/<int:pk>/', views.like, name='like'),
    path('follow/<int:pk>/', views.follow, name='follow')
 
]
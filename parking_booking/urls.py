# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.user_login, name='login'),
#     path('booking/', views.booking, name='booking'),
#     path('logout/' , views.user_logout , name = "logout"),
#    path('ticket/<int:booking_id>/', views.payment_success, name='payment_success'),
# ]



# new code  and logic start from here 

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.user_login, name='login'),
#     path('booking/', views.booking, name='booking'),
#     path('logout/', views.user_logout, name='logout'),
#     path('ticket/<int:booking_id>/', views.payment_success, name='payment_success'),
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('booking/', views.booking, name='booking'),
    path('logout/', views.user_logout, name='logout'),
    path('ticket/<int:booking_id>/', views.payment_success, name='payment_success'),
    
]



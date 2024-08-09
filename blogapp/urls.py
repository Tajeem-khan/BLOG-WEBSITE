
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>', views.single, name='single'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('author_reg/', views.author_reg, name='author_reg'),
    path('author_dashboard', views.author_dashboard, name='dashboard'),
    path('author_add_blog', views.author_add_blog, name='author_add_blog'),
    path('author_update_blog/<int:pk>', views.author_update_blog, name='author_update_blog'),
    path('author_delete_blog/<int:pk>', views.author_delete_blog, name='author_delete_blog'),
    path('category/<str:name>', views.category_wise),
    
    
      
]

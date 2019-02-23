from django.urls import path


from blog import views

urlpatterns = [

    path('',views.all_blogs , name='blog'),
    path('<int:blog_id>/', views.details, name='detail'),

]
from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_list,name="user_list"),
    path('add/',views.user_add,name="user_add"),
    path('edit/<int:uid>/',views.user_edit,name="user_edit"),
    path('update/', views.user_update, name="user_update"),
    path('del/<int:uid>/',views.user_del,name="user_del"),

]

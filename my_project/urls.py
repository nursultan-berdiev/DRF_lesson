from django.contrib import admin
from django.urls import path
from quickstart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.CustomerListCreateAPIView.as_view()),
    path('api/comments/', views.comment_list),
    path('api/comments/<int:pk>/', views.comment_detail),
]

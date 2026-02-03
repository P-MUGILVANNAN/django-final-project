from django.urls import path
from .views import RegisterView,LoginView,BookCreateView,BookUpdateDeleteView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='Register'),
    path('login/',LoginView.as_view(),name='Login'),
    path('books/',BookCreateView.as_view(),name='Books'),
    path('books/<int:id>/',BookUpdateDeleteView.as_view(),name="BookUpdateDelete"),
]
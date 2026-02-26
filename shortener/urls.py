from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # <str:short_code> captures whatever is typed in the URL and passes it to the view
    path('<str:short_code>/', views.redirect_url, name='redirect'),
]
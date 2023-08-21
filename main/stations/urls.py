from django.urls import path
from . import views
urlpatterns = [
    path('fortosiMain', views.fortosi, name='fortosi'),
    path('patrasMain', views.patras, name='patras'),
    path('kosmiraMain', views.kosmira, name='kosmira'),


]

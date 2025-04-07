from django.urls import path
from .views import homepage, properties, clients, calendar, profile, add_properties

urlpatterns = [
    path('', homepage, name='homepage'),  # Page d'accueil
    path('biens', properties, name='properties'),  # Page des biens immobiliers
    path('biens/ajout_bien', add_properties, name='add_properties'),  # Page des biens immobiliers
    path('clients', clients, name='clients'),  # Page des clients
    path('calendrier', calendar, name='calendar'),  # Page du calendrier
    path('profil', profile, name='profile'),  # Page du profil
]

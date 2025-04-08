from django.urls import path
from .views import homepage, properties, clients, calendar, profile, add_property, delete_property, update_property

urlpatterns = [
    path('', homepage, name='homepage'),  # Page d'accueil
    path('clients', clients, name='clients'),  # Page des clients
    path('calendrier', calendar, name='calendar'),  # Page du calendrier
    path('profil', profile, name='profile'),  # Page du profil
    ### Pages de gestion des biens immobiliers ###
    path('biens', properties, name='properties'),  # Page des biens immobiliers
    path('biens/ajout_bien', add_property, name='add_property'),  # Page d'ajout d'un bien immobiliers
    path('biens/supprimer/<int:property_id>/', delete_property, name='delete_property'), # Page de suppression d'un bien immobilier
    path('biens/modifier/<int:property_id>/', update_property, name='update_property'), # Page de modification d'un bien immobilier
]

from django.db import models

# Create your models here.


class TestTable(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.CharField(max_length=255)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
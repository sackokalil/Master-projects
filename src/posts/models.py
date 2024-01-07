from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")# verbose_name permet de donner un label qui doit s'afficher dans les formulaires
    slug = models.CharField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(
            self):  # cette fonction permet d'envoyer le titre de l'article comme l'element a afficher par defaut quand on appelle un article
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author if self.author else "L'auteur inconnu"
        # ici self.author renvoi automatiquement le username(ici l'email) de l'utilisateur, à cause du fait
        # que la fonction __str__ defini dans la class AbstractBaseUser de django du quel notre model
        # utilisateur personalisé herite, pointe sur username_field comme l'element à afficher par defaut.
        #alors que dans notre model personalisé, ce champs(username_fiels) est pointé sur l'attribu "email".
        #ce n'est donc pas la peine de dire "return self.author.email" car la fonction __str__ pointe deja sur ce champs(email)
        # "return self.author" suffit donc.

    def get_absolute_url(self):
        return reverse('posts:home')
        # cette fonction get_absolute_url permet de rediriger vers une urls donnée, elle est implicitement appélé
        # lors de la création d'une instance à partir dun formulaire
        # la fonction reverse permet de recuperer une url à partir de son nom et du space name(app_name) qui sont definis
        # dans urls.py de l'application.

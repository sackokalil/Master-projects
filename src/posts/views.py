from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    # ici on a pas besoin d'indiquer quel template il doit afficher les article.
    # par defaut, les ListView cherche un template dont le nom est composé du nom de notre application et celui
    # de notre model suivi de "_list.html" comme ceci: posts/blogpost_list. il suffit donc de creer ce fichier html
    # dans un dossier portant le nom de l'app, et le tout dans un dossier appélé "templates".

    def get_queryset(self):  # ici on verifie si le user est connecté pour lui envoyer tous les article, sinon seulement ceux publiés.
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)
        # cette fonction est celle qui est automatiquement et implicitement appélée par ListView pour recuperer les donnees de la base
        # il s'agit ici donc d'une surcharge de cette fonction.


@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content', ]
    # la variable "form" utilisée dans le template blogpost_create est implicite, c'est à dire qu'il est automatiquement
    # envoyée par le CreateView sur le template, on pourra donc y acceder.


@method_decorator(login_required, name="dispatch")
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"


@method_decorator(login_required, name="dispatch")
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")  # permet de rediriger vers la home page après la suppression.
    # cette classe DeleteView cherche automatiquement un template dont le nom est composé du nom du model et
    # le suffix "_confirm_delete.html", comme ceci "blogpost_confirm_delete.html", il suffi donc de créer ce tempate
    # dans un dossier portant le nom de l'application le tout dans le dossier "templates" de l'application.
    # sinon on aurait tout simplement pu indiquer le nom de template à chercher comme on l'a fait dans la CreateView.


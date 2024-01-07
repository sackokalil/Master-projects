from django.urls import path

from traps.views import google_show, amazon_offer_show, ListTrapShow, homeView, DeleteElement

app_name = "traps"

urlpatterns = [
    # path('', TrapHome.as_view(), name="traphome"),
    path('home/', homeView, name="home"),
    path('google/', google_show, name="google"),
    path('amazon/', amazon_offer_show, name="amazon"),
    path('list-trap/', ListTrapShow.as_view(), name="list-trap"),
    path('delete/<slug:email_slug>/', DeleteElement.as_view(), name="delete"),# pour mieux comprendre cette ligne, voire la vue de suppression


]

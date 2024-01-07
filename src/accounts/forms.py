from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", )
        #notre classe formulaire hérite de la classe formulaire "UserCreationForm", qui a pour role, qui a pour
        #role la gestion des mots de passe, c'est pourquoi on ne passe a notre formulaire que le champ "email" comme
        # champ obligatoir et le champ mot de passe sera implicitement envoyer sur le template dû au fait que le
        #formulaire hérite de ce formulaire de gestion des mots de passe.

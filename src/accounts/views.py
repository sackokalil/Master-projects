from django.shortcuts import render, redirect

from accounts.forms import UserRegistrationForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           # form.instance.zip_code = 12345
            form.save()
            return redirect("posts:home")
    else:
        form = UserRegistrationForm()

    return render(request,"accounts/signup.html", {"form": form})
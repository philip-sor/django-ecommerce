from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .forms import RegistrationForm
from .models import CustomAccount
from .tokens import account_activation_token
# Create your views here.


def register_account(request):
    if request.user.is_authenticated:
        return redirect("/")

    registration_form = RegistrationForm()
    context = {'form': registration_form}
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        context["form"] = registration_form
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.set_password(registration_form.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('templates/accounts/register/account_activation.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            print(message)
            user.email_user(subject='Activate your account', message=message)
    return render(request, 'templates/accounts/register/login_register.html', context)


def login_account(request):
    page = 'login'
    context = {
        'page': page
    }
    if request.user.is_authenticated:
        return redirect("shop:home")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomAccount.objects.get(email=email)
        except:
            messages.error(request, 'User with such email does not exist')
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('shop:home')
            else:
                messages.error(request, 'Invalid Email OR Password')
        else:
            messages.error(request, 'Invalid Email OR Password')
    return render(request, 'templates/accounts/register/login_register.html', context)


def account_activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = CustomAccount.objects.get(id=uid)
    except(ValueError, TypeError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/accounts/login')
    else:
        return render(request, 'templates/accounts/register/activation_invalid.html')



# def logout_account(request):
#     if not request.user.is_authenticated:
#         return redirect('/')
#
#
#     return render(request, 'templates/accounts/_logout.html')

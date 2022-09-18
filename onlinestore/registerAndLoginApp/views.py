from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from store.models import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegistrationForm()
        category = Category.objects.all()
        context = {'category': category, 'form': form}
        return render(request, 'registerAndLoginApp/register.html', context=context)


def login(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'registerAndLoginApp/login.html', context=context)

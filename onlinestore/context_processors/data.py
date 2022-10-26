from django.template.context_processors import *
from store.models import *
from userEnvironment.models import *


def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return context


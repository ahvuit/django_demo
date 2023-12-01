from django.http import HttpResponse
from django.template import loader
from .models import User


def user(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    users = User.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Linus',
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'users': users,
    }
    return HttpResponse(template.render(context, request))

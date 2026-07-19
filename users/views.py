from django.shortcuts import render
from .models import User

def home(request):
    return render(request, "users/home.html")


def create_user(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")

        User.objects.create(
            name=name,
            age=age
        )

        return render(request, "users/create_user.html", {
            "message": "User Created Successfully!"
        })

    return render(request, "users/create_user.html")

def show_users(request):

    if request.method == "POST":

        age = request.POST.get("age")

        users = User.objects.filter(age__gte=age)

    else:

        users = User.objects.all()

    return render(request, "users/show_users.html", {
        "users": users
    })

def filter_users(request):

    users = []

    if request.method == "POST":

        age = request.POST.get("age")

        users = User.objects.filter(age__gte=age)

    return render(request, "users/filter_users.html", {
        "users": users
    })


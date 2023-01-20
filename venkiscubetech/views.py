from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        "title": "home page new",
        "bdata": "welcome to vtech",
        "clist": ["php", "django", "c", "c++"],
        "numbers": [100, 1, 200, 305, 40, 50, 60],
        "student_details": [
            {"name": "venki", "phone": 1234567891},
            {"name": "anamika", "phone": 1234567981}
        ]
    }
    return render(request, "home.html")


def login(request):
    return render(request, "index.html")


def aboutUs(request):
    return HttpResponse("welcome to venki's about us....thanks!!")


def blogs(request):
    return HttpResponse("welcome to our blogs section...thank for visiting..!!")


def users(request):
    return HttpResponse("theree is all the users list presents!!")


def blogsDetails(request, blogid):
    return HttpResponse(blogid)


def register(request):
    return render(request, "register.html")

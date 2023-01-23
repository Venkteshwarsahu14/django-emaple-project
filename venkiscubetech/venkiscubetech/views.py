from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UsersForm
from service.models import Service
from news.models import News


def homePage(request):
    # data = {
    #     "title": "home page new",
    #     "bdata": "welcome to vtech",
    #     "clist": ["php", "django", "c", "c++"],
    #     "numbers": [100, 1, 200, 305, 40, 50, 60],
    #     "student_details": [
    #         {"name": "venki", "phone": 1234567891},
    #         {"name": "anamika", "phone": 1234567981}
    #     ]
    # }
    service_data = Service.objects.all()
    if request.method == "GET":
        st = request.GET.get("servicename")
        if st != None:
            service_data = Service.objects.filter(service_title__icontains=st)
    new_data = News.objects.all()
    data = {
        "service_data": service_data,
        "news_data": new_data
    }
    return render(request, "home.html", data)


def submitform(request):
    finalans = 0
    try:
        if request.method == "POST":
            n1 = int(request.POST["num1"])
            n2 = int(request.POST["num2"])
            print(n1 + n2)
            finalans = n1+n2
            return HttpResponse(finalans)

    except:
        pass
    return HttpResponse(request)


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


def thanku(request):
    output = 0
    if request.method == "GET":
        output = request.GET.get("output")
    return render(request, "thanku.html", {"output": output})


def userform(request):
    finalans = 0
    fn = UsersForm()
    data = {'form': fn}

    try:
        n1 = int(request.POST["num1"])
        n2 = int(request.POST["num2"])
        print(n1 + n2)
        finalans = n1+n2
        data = {
            "form": fn,
            "output": finalans
        }
        url = "/thanku/?output={}".format(finalans)
        return redirect(url)

    except:
        pass

    return render(request, "userform.html", data)


def calculator(request):
    data = {}
    try:
        if request.method == "POST":
            num1 = eval(request.POST.get("num1"))
            num2 = eval(request.POST.get("num2"))
            operation = request.POST.get("operation")
            if operation == "+":
                c = num1 + num2
            elif operation == "-":
                c = num1 - num2
            elif operation == "*":
                c = num1*num2
            else:
                c = num1 / num2
        data = {
            "num1": num1,
            "num2": num2,
        }
    except:

        c = "invalid operaiton...."

    data["result"] = c
    return render(request, "calculator.html", data)


def evenodd(request):
    c = ''
    number = 0
    data = {}
    if request.method == "POST":
        if request.POST.get("number") == "":
            return render(request, "evenodd.html", {"error": True})
        number = eval(request.POST.get("number"))
        if number % 2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
    data["number"] = number
    data['result'] = c
    return render(request, "evenodd.html", data)


def marksheet(request):
    total = 0
    data = {}
    if request.method == "POST":
        if request.POST.get("subject1") == "" or request.POST.get("subject2") == "" or request.POST.get("subject3") == "" or request.POST.get("subject4") == "" or request.POST.get("subject5") == "":
            return render(request, "marksheet.html", {"error": True})

        sub1 = eval(request.POST.get("subject1"))
        sub2 = eval(request.POST.get("subject2"))
        sub3 = eval(request.POST.get("subject3"))
        sub4 = eval(request.POST.get("subject4"))
        sub5 = eval(request.POST.get("subject5"))
        total = sub1+sub2+sub3+sub3+sub4+sub5
        print(total)
        percentage = total*100/500
        if percentage >= 60:
            division = "first division"
        elif percentage >= 45:
            division = "second division"
        elif percentage >= 35:
            division = "third division"
        else:
            division = "fail.."
        data = {
            "total": total,
            "percentage": percentage,
            "division": division
        }
        return render(request, "marksheet.html", data)

    return render(request, "marksheet.html")


def newsdeatils(request, newsid):
    newsDetails = News.objects.get(id=newsid)
    data = {
        "newsdetails": newsDetails
    }
    return render(request, "newsdetails.html", data)

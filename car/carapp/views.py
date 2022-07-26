from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Max
from django.db.models.functions import Coalesce
from django.db.models.functions import Lower
from django.forms.models import model_to_dict
from django.utils import  timezone
import requests, json
# from .forms import TestBookForm, TestBookFormOne
from .models import BooksModel, TestBook, Result, Question, TodoList, CreateTodo, WeatherData
import urllib.request as httprequest
import json

#  <<<<<<<<<------ weather API ------->>>>>>>>>>>

import datetime as dt
import json
import datetime
from datetime import datetime

import requests


# Create your views here.


# <<<<<<------ QUIZ API TEST ------->>>>>>>

def apitest(request):
    qno = 0
    qnumber = 0
    result = []
    # dresult = {}
    option = ""
    session = request.session
    # result = dresult

    response = requests.get('https://gist.githubusercontent.com/champaksworldcreate/320e5af5ea9dbd31597d220637885587/raw/99f8f7a4df34ae477dcceb62598aa0bdde9ef685/tfquestions.json')
    data = response.json()
    data = data.get("questions")
    q = data[qno]['question']

    if request.GET:
        qno = int(request.GET['qno'])
        option = request.GET['option']
        qno += 1
        result.append(option)
        # dresult[qnumber] = option
        qnumber = qno + 1
        if qnumber > len(data):
            print(session.get(qnumber))
            return HttpResponse("Test End")
        q = data[qno]['question']
    session[qnumber] = result
    return render(request, "apitest.html", {"data":q, "qnumber": qno + 1, "qno": qno, "result": result,  "session": request.session.items()})

# <<<-------- Set, Get, & Remove session ------->>>>

def setsession(request):
    session= request.session
    session["1"]="Shivam"
    return HttpResponse(session.get("1"))

def getsession(request):
    session= request.session
    data=session.get(str(1))
    return HttpResponse(data)

def removesession(request):
    # session = request.session
    del request.session["1"]
    return HttpResponse("You are Logged out")

# <<<<<------- Session Quiz ------>>>>>>
def sessionquiz(request):
    data = {"A":a, "B":b}
    session = request.session
    session[1] = "One"
    return render(request, "sessionquiz.html", {"data":data})







# <<<<<----- QUIZ 2 TRUE FLASE ------>>>>>>

def tfquiz(request):
    url = 'https://gist.githubusercontent.com/champaksworldcreate/320e5af5ea9dbd31597d220637885587/raw/99f8f7a4df34ae477dcceb62598aa0bdde9ef685/tfquestions.json'
    resp = requests.get(url)
    questions = json.loads(resp.text)
    print(questions)

    qno = 0
    result = ""
    if request.POST:
        option = request.POST["option"]
        givenanswer = True
        if option == "False":
            givenanswer = False
        if givenanswer == questions["correctanswer"]:
            result = "right"
        else:
            result = "wrong"
        qno = int(request.POST["qno"])
        qno += 1

    if qno >= len(questions):
        return Httpresponse("Test Over")


    # question = questions[qno]
    return render(request, "tfquiz.html", {"qno": qno, "qnumber": qno +1, "questions": questions, "result": result})



# <<<<<----- QUIZ TRUE FLASE ------>>>>>>

def quiztf(request):
    url = 'https://gist.githubusercontent.com/champaksworldcreate/320e5af5ea9dbd31597d220637885587/raw/99f8f7a4df34ae477dcceb62598aa0bdde9ef685/tfquestions.json'
    resp = requests.get(url)
    data = json.loads(resp.text)
    # q1 = data["questions"]["question"]
    print(data)
    return render(request, "quiztf.html", {"data": data})









#<<<<---- weather API function -------->>>>>>>>
def weathercity(request):

    date_time_str = '2018-09-22 11:00:00'
    print("Timezone.now()")
    print (timezone.now())
    date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    print("Date time")

    print(date_time)
    current_time = datetime.datetime.now().time()
    print("current time")
    print(current_time)

    city="Enter"
    temp = 0
    feels_like = 0
    temp_max = 0
    temp_min = 0
    humidity = 0
    data = ""

    if request.GET:
        city = request.GET['city']
        report = {}
        print(dt.datetime.fromtimestamp(1624491535))
        appid = "c9088325fd9ad3cbfac170d0a827ab54"
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4a1f8a61b74546825af1e0be106e797b&units=metric"
        response = requests.get(url)
        data=json.loads(response.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        value = WeatherData(city = city, temp = temp, feels_like = feels_like, temp_min = temp_min, temp_max = temp_max, humidity = humidity)
        value.save()

    report = {
        "city": city,
        "temp": temp,
        "feels_like": feels_like,
        "temp_min" : temp_min,
        "temp_max" : temp_max,
        "humidity": humidity,
    }

    return render(request, "weathercity.html",{"data":data, "report": report})














def weather(request):
    api_key = "c9088325fd9ad3cbfac170d0a827ab54"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = "delhi"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    print (response)
    data=json.loads(request.body)
    return render(request, "weather.html", {"data": data})
    # x = response.json()
    # if x["cod"] != "404":
    #     y = x["main"]
    #     current_temperature = y["temp"]
    #     current_pressure = y["pressure"]
    #     current_humidity = y["humidity"]
    #     z = x["weather"]
    #     weather_description = z[0]["description"]





    # data = {}
    # if request.POST:
    #     city = request.POST['city']
    #     # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={c9088325fd9ad3cbfac170d0a827ab54}').read()
    #     source = urllib.request.urlopen(
    #         'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={c9088325fd9ad3cbfac170d0a827ab54}').read()
    #     print (source)
    #     list_of_data = json.loads(source)
    #     data = {
    #         "country_code": str(list_of_data['sys']['country']),
    #         "coordinate": str(list_of_data['coord']['lat']),
    #     }
    #     print(city)
    #     print(data)
    # 
    # return render(request, "weather.html", {"data": data})


def home(request):
    links = ["home", "search", "searchor", "avg", "againsearch", "Searchbybook", "SearchbyInput",
             "Inputsearchbyprice", "Between", "allbooks", "base", "bootstrap", "header", "quiz", "quizpage", "session",
             "validation", "quiztf", "tfquiz", "sessionquiz"]
    return render(request, "home.html", {'name': 'shivam', "links": links})


# def index(request):
#     return HttpResponse("You're at the Books index.")


def all(request):
    books = TestBook.objects.all()
    return render(request, "filter.html", {"books": books, "title": "All"})


def search(request):
    books = TestBook.objects.filter(subject="2")
    return render(request, "filter.html", {"books": books, "title": "Search Subject = 2"})


def searchbybook(request):
    books = TestBook.objects.filter(bookname="Basic Java")
    return render(request, "filter.html", {"books": books, "title": "Search by Bookname"})


def inputsearchbybook(request):
    bk = 0
    if request.GET:
        bk = request.GET["book"]
    books = TestBook.objects.filter(bookname=bk)
    return render(request, "filter.html", {"books": books, "title": "Search by Input"})


def inputsearchbyprice(request):
    fr = 0
    to = 0
    if request.POST:
        fr = int(request.POST["from"])
        to = int(request.POST["to"])
    if fr <= 0 & to <= 0:
        books = TestBook.objects.all()
    else:
        books = TestBook.objects.filter(price__gte=fr) & TestBook.objects.filter(price__lte=to)
    return render(request, "pricefilter.html", {"to": to, "from": fr, "books": books, "title": "Search by Input"})


def allbooks(request):
    data = BooksModel1.objects.all().order_by('bookname')
    return render(request, "filter.html", {'Books': data, "title": "all books"})


def between(request):
    avg = 0
    data = BooksModel.objects.filter(price__lt=1000) & BooksModel.objects.filter(price__gt=100).order_by(
        'bookname').reverse()
    avg = (BooksModel.objects.filter(price__lt=1000) & BooksModel.objects.filter(price__gt=100).order_by(
        'bookname').reverse()).aggregate(Avg('price'))
    return render(request, "filter.html", {"average": avg, "books": data, "title": "All Books"})


def allbooks(request):
    # data = BooksModel.objects.all().order_by('bookname')
    # data = BooksModel.objects.all().order_by('bookname').reverse()
    # data = BooksModel.objects.all().order_by(Coalesce('bookname','bookname').desc())
    data = BooksModel.objects.all().order_by(Lower('bookname').desc())
    return render(request, "filter.html", {'books': data, "title": "All Books"})


def base(request):
    return render(request, "base.html")


def bootstrap(request):
    return render(request, "bootstrap.html")


"""

def allbooks(request):
    # data = BooksModel.objects.all().order_by('bookname')
    data = BooksModel.objects.all().order_by('bookname').reverse()
    # data = BooksModel.objects.all().order_by(Coalesce('bookname','bookname').desc())
    # data = BooksModel.objects.all().order_by(Lower('bookname').desc())
    return render(request, "filter.html", {'books': data, "title": "All Books"})
"""


def searchbooks(request):
    data = BooksModel.objects.filter(subject="2")
    return render(request, "filter.html", {'books': data, "title": "Search Subject"})


def searchor(request):
    data = BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")
    return render(request, "filter.html", {'books': data, "title": "Search Subject Or"})


# <<<This avg method not return any value
def avg(request):
    avg = 0
    data = BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")
    avg = (BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")).aggregate(Avg('price'))
    return render(request, "filter.html", {"average": avg, 'books': data, "title": "Avg Price"})


# def showForm(request):
#     return render(request, "testformbook.html", {'testform': TestBookForm(), "title": "Form"})

"""
def showFormInitial(request):
    book = TestBook.objects.get(pk=1)
    print(book.bookname)
    f = TestBookFormOne(initial={"bookname":book.bookname,"subject":book.subject,"price":book.price})
    # print(f)
    # f.save()
    # print(f.is_bound)

    print(f.is_valid())
    if f.is_valid():
        f.save()
    return render(request, "testformbook.html", {'testform': f, "title": "Form with Initial"})


def showForm1(request):
    book = TestBook.objects.get(pk=1)
    f = TestBookFormOne(instance=book)
    # print(f)
    # f.save()
    # print(f.is_bound)

    print(f.is_valid())
    if f.is_valid():
        f.save()
    return render(request, "testformbook.html", {'testform': f, "title": "Form with Instance"})
"""


def project1(request):
    links = ["project"]
    return render(request, "header.html", {'name': 'shivam', "links": links})


def header(request):
    links = ["project"]
    return render(request, "header.html", {'name': 'shivam', "links": links})


def session(request):
    submit = ""
    key = ""
    value = ""
    if request.GET:
        submit = request.GET["submit"]
        key = request.GET["key"]
        value = request.GET["value"]
    session = request.session
    session[key] = value

    return render(request, "session.html", {"session": session, "key": key, "value": value})


def validation(request):
    uname = ""
    pswd = ""
    data = {}
    if request.GET:
        uname = request.GET["uname"]
        pwd = request.GET["pswd"]
    data[uname] = pswd
    return render(request, "validation.html", {"data": data})


# <<<<<<<<-------- Quiz Starts Here --------->>>>>>>>>>


class QuizResponse:
    def __init__(self, qno, question, correctanswer, useranswer):
        self.qno = qno
        self.question = question
        self.correctanswer = correctanswer
        self.useranswer = useranswer


def quizhome(request):
    return render(request, "quizhome.html")


userans = []
userdata = {}


# def quizpage(request):
#     data = 0
#     n = 1
#     maxno = 1
#     next = ""
#     pre = ""
#     queno = 1
#     option = 1
#     testover = ""
#     value = ""
#     f = 0
#
#     if request.GET:
#         next = request.GET["next"]
#         option = request.GET["option"]
#         queno = int(request.GET["questionno"])
#         testover = request.GET["testover"]
#         userans.append(option)
#     session = request.session
#     if f > 0:
#         queno = queno + 1
#         maxno = Question.objects.all().aggregate(Max('questionno'))
#         data = Question.objects.get(id=queno)
#         qr = QuizResponse(queno, data.question, data.answer, option)
#
#
#         r = Result()
#         r.questionno = queno
#         r.option = option
#         r.question = data.question
#         r.name = "candidatename"
#         r.answer = data.answer
#         r.save()
#         value = Result.objects.all()
#
#     else:
#         data = Question.objects.get(id=queno)
#         qr = QuizResponse(queno, data.question, data.answer, option)
#         f = f + 1
#         print("else ")
#         r = Result()
#         r.questionno = queno
#         r.option = option
#         r.question = data.question
#         r.name = "candidatename"
#         r.answer = data.answer
#         r.save()
#         value = Result.objects.all()
#
#
#
#     if ((testover == "over") | (queno == 5)):
#         return render(request, "result.html", {"value": value})
#     else:
#         return render(request, "quizpage.html",
#                       {"data": data, "questionno": queno, "maxno": maxno, "option": option, "userans": userans,
#                        "session": session})

def result(request):
    return render(request, "result.html", {"session": session})


def quizpage(request):
    data = 0
    n = 1
    maxno = 1
    next = ""
    pre = ""
    queno = 1
    option = 1
    testover = ""
    value = ""

    if request.GET:
        next = request.GET["next"]
        option = request.GET["option"]
        queno = int(request.GET["questionno"])
        testover = request.GET["testover"]
        userans.append(option)
    session = request.session
    if next == "next":
        queno = queno + 1
        maxno = Question.objects.all().aggregate(Max('questionno'))
        data = Question.objects.get(id=queno)

        qr = QuizResponse(queno, data.question, data.answer, option)

        r = Result()
        r.questionno = queno
        r.option = option
        r.question = data.question
        r.name = "candidatename"
        r.answer = data.answer
        r.save()
        value = Result.objects.all()


    else:
        data = Question.objects.get(id=queno)
        qr = QuizResponse(queno, data.question, data.answer, option)
        print("else ")
        r = Result()
        r.questionno = queno
        r.option = option
        r.question = data.question
        r.name = "candidatename"
        r.answer = data.answer
        r.save()
        value = Result.objects.all()

    if ((testover == "over") | (queno == 5)):
        return render(request, "testresult.html", {"value": value})
    else:
        return render(request, "quizpage.html",
                      {"data": data, "questionno": queno, "maxno": maxno, "option": option, "userans": userans,
                       "session": session})


def testresult(request):
    return render(request, "testresult.html", {"session": session})


# <<<<< COOKIES  >>>>>>

def setcookies(request):
    response = render(request, 'setcookies.html')
    response.set_cookie('name', 'abhi')
    return response


def getcookies(request):
    name = request.COOKIES['name']
    return render(request, "getcookies.html", {'name': name})


def todohome(request):
    return render(request, "todohome.html")


def todocreate(request):
    # <<<--- Create refernce by Home ----->>>

    # create = ''
    # if request.GET:
    #     create = request.GET['create']
    # if create == "create":

    edit = ''
    toedit = ''
    value = ''
    if request.GET:
        toedit = request.GET['edit']

    if toedit == "edit":
        pass
    edit = TodoList.objects.filter(id=5)

    # cr = TodoList(edit.id, edit.taskname, edit.details, edit.status)
    # r = CreateTodo()
    # r.taskno = edit.id
    # r.taskname = edit.taskname
    # r.details = edit.details
    # r.status = edit.status
    # r.save()
    # value = TodoList.objects.all()

    print(edit)
    return render(request, "todocreate.html", {"edit": edit, "value": value})


def tododesign(request):
    data = ''
    data = TodoList.objects.all()
    print(data)
    return render(request, "tododesign.html", {"data": data})

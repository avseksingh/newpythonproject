from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Max
from django.db.models.functions import Coalesce
from django.db.models.functions import Lower
from django.forms.models import model_to_dict

# from .forms import TestBookForm, TestBookFormOne
from .models import BooksModel, TestBook, Result, Question


# Create your views here.

def home(request):
    links = ["index", "home", "search", "searchor", "avg", "againsearch", "Searchbybook", "SearchbyInput",
             "Inputsearchbyprice", "Between", "allbooks", "base", "bootstrap", "header", "quiz", "quizpage", "session",
             "validation"]
    return render(request, "home.html", {'name': 'shivam', "links": links})


def index(request):
    return HttpResponse("You're at the Books index.")


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